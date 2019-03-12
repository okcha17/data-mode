SELECT MRR_MONTH, 
      count(distinct OLDEST_SUBSCRIPTION_IN_COHORT) as count_of_subscriptions, 
      count(distinct SFDC_ACCOUNT_ID) as count_of_accounts, 
      count(distinct ULTIMATE_PARENT_ACCOUNT_ID) as count_of_parent_accounts
FROM ANALYTICS.ANALYTICS.MRR_TOTALS_LEVELLED
WHERE mrr_month < date_trunc('month', CURRENT_DATE)
GROUP BY 1
ORDER BY 1 DESC