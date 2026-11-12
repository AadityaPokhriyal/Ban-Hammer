import pandas as pd
import numpy as np
import json
from pathlib import Path

# Folders containing your Parquet and JSON files of with_cheaters and without_cheaters
DATA_FOLDERS = [
    # Path("datasets/with_cheaters"),
    # Path("datasets/without_cheaters")
    Path("datasets/test")
]


def process_match(parquet_path,with_cheaters):

    # Get corresponding JSON file
    json_path = parquet_path.with_suffix(".json")

    if not json_path.exists():
        print(f"Skipping {parquet_path.name}: JSON file not found")
        return None

    # Read files
    df = pd.read_parquet(parquet_path)

    with open(json_path, "r") as f:
        events = json.load(f)

    # Extract match ID from filename
    match_id = parquet_path.stem

    if(with_cheaters):
        # Get cheater IDs from JSON
        cheater_ids = {
            player["steamid"]
            for player in events["cheaters"]
        }
        print(cheater_ids)
    else:
        cheater_ids = set()
    

    # Calculate actual speed
    df["actual_speed"] = np.sqrt(
        df["velocity_X"]**2 +
        df["velocity_Y"]**2 +
        df["velocity_Z"]**2
    )

    # Calculate cumulative player statistics
    player_stats = df.groupby("steamid").agg(
        kills=("kills_total", "max"),
        deaths=("deaths_total", "max"),
        headshot_kills=("headshot_kills_total", "max"),
        rounds=("total_rounds_played", "max")
    )

    # Calculate behavioural statistics using alive,
    # non-warmup observations
    active_df = df[
        (df["is_alive"] == True) &
        (df["is_warmup_period"] == False)
    ]

    behaviour_stats = active_df.groupby("steamid").agg(
        avg_speed=("actual_speed", "mean"),
        avg_accuracy_penalty=("accuracy_penalty", "mean")
    )

    # Combine statistics
    player_stats = player_stats.join(behaviour_stats)

    # Calculate derived features
    player_stats["kills_per_round"] = (
        player_stats["kills"] /
        player_stats["rounds"].replace(0, np.nan)
    )

    player_stats["deaths_per_round"] = (
        player_stats["deaths"] /
        player_stats["rounds"].replace(0, np.nan)
    )

    player_stats["kd_ratio"] = (
        player_stats["kills"] /
        player_stats["deaths"].replace(0, 1)
    )

    player_stats["has_kills"] = (
        player_stats["kills"] > 0
    ).astype(int)

    player_stats["headshot_rate"] = (
        player_stats["headshot_kills"] /
        player_stats["kills"].replace(0, np.nan)
    ) * 100
    
    # Calculate total damage dealt by each player
    damage = {}

    for event in events["player_hurt"]:
        attacker = event["attacker_steamid"]
        damage[attacker] = (
            damage.get(attacker, 0) + event["dmg_health"]
        )

    player_stats["total_damage"] = (
        pd.Series(damage).reindex(player_stats.index).fillna(0)
    )

    # Damage per round
    player_stats["damage_per_round"] = (
    player_stats["total_damage"] /
    player_stats["rounds"].replace(0, np.nan)
    )

    # Damage Per Round and headshot rate interaction
    # Very High damage but very low headshot rate -> more suspicious 
    # Low Damage and Low headshot -> safer
    # High Damage and High headshot rate -> Other Features excell
    player_stats["damagepr_and_headshotrate_interaction"] = (
    player_stats["damage_per_round"] *
    (1-player_stats["headshot_rate"] / 100)
    )

    # Assign labels
    player_stats["is_cheater"] = (
        player_stats.index.isin(cheater_ids).astype(int)
    )

    # Add match ID
    player_stats["match_id"] = match_id

    # Create a DataFrame from player death events
    death_events = pd.DataFrame(events["player_death"])

    # Group by attacker
    combat_stats = death_events.groupby("attacker_steamid").agg(
        total_kills=("attacker_steamid", "count"),
        smoke_kills=("thrusmoke", "sum"),
        blind_kills=("attackerblind", "sum"),
        air_kills=("attackerinair", "sum")
    )

    # Calculate ratios
    combat_stats["smoke_kill_ratio"] = (
        combat_stats["smoke_kills"] / combat_stats["total_kills"]
    )

    combat_stats["blind_kill_ratio"] = (
        combat_stats["blind_kills"] / combat_stats["total_kills"]
    )

    combat_stats["air_kill_ratio"] = (
        combat_stats["air_kills"] / combat_stats["total_kills"]
    )

    # Merge with existing player statistics
    player_stats = player_stats.join(
        combat_stats.drop(columns=["total_kills", "smoke_kills", "blind_kills", "air_kills"]),
        how="left"
    )

    # Players with no kills receive zero for these features
    player_stats[
        ["smoke_kill_ratio", "blind_kill_ratio", "air_kill_ratio"]
    ] = player_stats[
        ["smoke_kill_ratio", "blind_kill_ratio", "air_kill_ratio"]
    ].fillna(0)

    # Keep steamid as an identifier
    player_stats = player_stats.reset_index()

    return player_stats


match_dataframes = []

for folder in DATA_FOLDERS:
    with_cheaters = True
    #folder.name == "with_cheaters"
    for parquet_file in folder.glob("*.parquet"):
        try:
            match_stats = process_match(parquet_file,with_cheaters)

            if match_stats is not None:
                match_dataframes.append(match_stats)

        except Exception as e:
            print(f"Error processing {parquet_file}: {e}")

# Combine all matches
if match_dataframes:

    all_matches = pd.concat(
        match_dataframes,
        ignore_index=True
    )

    all_matches.to_csv("datasets/extracted/test.csv", index=False)

    print("\nDataset created successfully!")
    print("Total matches:", all_matches["match_id"].nunique())
    print("Total player records:", len(all_matches))

    print("\nDataset preview:")
    print(all_matches.head())

else:
    print("No matches were successfully processed.")