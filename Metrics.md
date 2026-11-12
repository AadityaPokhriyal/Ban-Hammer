# MODEL COMPARISON 1 (550 records) (Not Threshold Tuned)
## features:
["kills_per_round",
"deaths_per_round",
"kd_ratio",
"headshot_rate",
"has_kills",
"avg_speed",
"avg_accuracy_penalty"]

              Model  Accuracy  Precision  Recall  F1 Score  ROC-AUC
Logistic Regression    0.8455     0.9375  0.4839    0.6383   0.9081
      Random Forest    0.8455     1.0000  0.4516    0.6222   0.9283
            XGBoost    0.8545     1.0000  0.4839    0.6522   0.9204

# MODEL COMPARISON 2 (550 records) (Threshold Tuned on F1 Score)
## features:
["kills_per_round",
"deaths_per_round",
"kd_ratio",
"headshot_rate",
"has_kills",
"avg_speed",
"avg_accuracy_penalty",]

              Model  Accuracy  Precision  Recall  F1 Score  ROC-AUC
Logistic Regression    0.8455     0.9375  0.4839    0.6383   0.9081
      Random Forest    0.8636     0.9444  0.5484    0.6939   0.9283
            XGBoost    0.8818     0.9091  0.6452    0.7547   0.9204

# MODEL COMPARISON 3 (1760 records) (Threshold Tuned on F1 Score)
## features:
["kills_per_round",
"deaths_per_round",
"kd_ratio",
"headshot_rate",
"has_kills",
"avg_speed",
"avg_accuracy_penalty"]

              Model  Accuracy  Precision  Recall  F1 Score  ROC-AUC
Logistic Regression    0.9111     0.8182  0.7297    0.7714   0.9259
      Random Forest    0.9167     0.8793  0.6892    0.7727   0.9407
            XGBoost    0.9250     0.8406  0.7838    0.8112   0.9393

# MODEL COMPARISON 4 (1760 records) (Not Threshold Tuned)
## features:
["kills_per_round",
"deaths_per_round",
"kd_ratio",
"headshot_rate",
"has_kills",
"avg_speed",
"avg_accuracy_penalty",
"damage_per_round"]

              Model  Accuracy  Precision  Recall  F1 Score  ROC-AUC
Logistic Regression    0.9056     0.9348  0.5811    0.7167   0.9407
      Random Forest    0.9139     0.9057  0.6486    0.7559   0.9599
            XGBoost    0.9194     0.9091  0.6757    0.7752   0.9571

# MODEL COMPARISON 5 (1760 records) (Threshold Tuned on F1 Score)
## features:
["kills_per_round",
"deaths_per_round",
"kd_ratio",
"headshot_rate",
"has_kills",
"avg_speed",
"avg_accuracy_penalty",
"damage_per_round"]

              Model  Accuracy  Precision  Recall  F1 Score  ROC-AUC
Logistic Regression    0.9278     0.9138  0.7162    0.8030   0.9407
      Random Forest    0.9139     0.8644  0.6892    0.7669   0.9599
            XGBoost    0.9167     0.8056  0.7838    0.7945   0.9571

# MODEL COMPARISON 6 (1760 records) (Threshold Tuned on F1 Score)
## features:
["kills_per_round",
"deaths_per_round",
"kd_ratio",
"headshot_rate",
"has_kills",
"avg_speed",
"avg_accuracy_penalty",
"damage_per_round",
"damagepr_and_headshotrate_interaction"]

              Model  Accuracy  Precision  Recall  F1 Score  ROC-AUC
Logistic Regression    0.9167     0.9400  0.6351    0.7581   0.9502
      Random Forest    0.9167     0.8793  0.6892    0.7727   0.9510
            XGBoost    0.9194     0.9091  0.6757    0.7752   0.9550

# MODEL COMPARISON 7 (1760 records) (Threshold Tuned on F1 Score)
## features:
["kills_per_round",
"deaths_per_round",
"kd_ratio",
"headshot_rate",
"has_kills",
"avg_speed",
"avg_accuracy_penalty",
"damage_per_round",
"air_kill_ratio"]

              Model  Accuracy  Precision  Recall  F1 Score  ROC-AUC
Logistic Regression    0.9306     0.9016  0.7432    0.8148   0.9423
      Random Forest    0.9139     0.8772  0.6757    0.7634   0.9569
            XGBoost    0.9278     0.8636  0.7703    0.8143   0.9606

# MODEL COMPARISON 8 (1760 records) (Threshold Tuned on F1 Score)
## features:
["kills_per_round",
"deaths_per_round",
"kd_ratio",
"headshot_rate",
"has_kills",
"avg_speed",
"avg_accuracy_penalty",
"damage_per_round",
"damagepr_and_headshotrate_interaction"
"air_kill_ratio"]

              Model  Accuracy  Precision  Recall  F1 Score  ROC-AUC
Logistic Regression    0.9194     0.9412  0.6486    0.7680   0.9521
      Random Forest    0.9139     0.8209  0.7432    0.7801   0.9532
            XGBoost    0.9250     0.9123  0.7027    0.7939   0.9554

# MODEL COMPARISON 9 (1760 records) (Threshold Tuned on F1 Score)
## features:
["kills_per_round",
"deaths_per_round",
"kd_ratio",
"headshot_rate",
"has_kills",
"avg_speed",
"avg_accuracy_penalty",
"damage_per_round",
"damagepr_and_headshotrate_interaction"
"smoke_kill_ratio",	
"blind_kill_ratio",
"air_kill_ratio"]

              Model  Accuracy  Precision  Recall  F1 Score  ROC-AUC
Logistic Regression    0.9028     0.7746  0.7432    0.7586   0.9493
      Random Forest    0.9139     0.8909  0.6622    0.7597   0.9516
            XGBoost    0.9083     0.9020  0.6216    0.7360   0.9548