# Model selection
Model selection

# The question

The model predicts whether a customer is likely to leave the service (customer churn). A false negative may cause the company to lose a customer, while a false positive may waste resources on unnecessary retention offers.

# Candidates

Candidate| Why I tried it| AUC| F1| F1 per slice (lowest)| p95 latency (ms)| Size (KB)| MLflow run ID
Logistic Regression| Simple and fast baseline| 0.778| 0.3600| 0.0000 (Two-year)| 11.42| 4| c3ec147bb86a4ed5a7aa62d2bbf3b2f8
Random Forest| Ensemble model that captures non-linear patterns| 0.7689| 0.4231| 0.0000 (Two-year)| 55.96| 3098| 1d93793c757d47f38adc21bf585e56f6
Gradient Boosting| Boosting model that improves predictions sequentially| 0.779| 0.4444| 0.0000 (Two-year)| 11.49| 141| 4674002ecab14b56a466d579f333ff21

# The champion

I selected Gradient Boosting as the champion.

It achieved the highest overall F1 (0.4444) and AUC (0.779). It also achieved the best F1 for One-year contracts (0.4211).

Random Forest performed slightly better on Month-to-month contracts (0.475 vs 0.4706), but Gradient Boosting offered a better overall trade-off.

I accepted a slightly lower Month-to-month F1 in exchange for better overall performance, lower latency, and a much smaller model size than Random Forest.

All three models achieved an F1 score of zero for Two-year contracts, which remains a limitation.

# My promotion rules

- Latency budget (p95): 100 ms, because it provides enough room for prediction latency while keeping the service responsive.
- Minimum gain to replace the champion (F1 points): 0.01, because a new model should improve F1 by at least one percentage point to justify replacing the current champion.

# What I would check next

I would investigate the Two-year contract customer group because all three models achieved an F1 score of zero for this slice. I would also check whether the dataset contains enough customers from this group and monitor performance when new customer data becomes available.