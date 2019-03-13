SELECT concat(concat(SPLIT_PART(gitlab_version, '.', 1), '.'), SPLIT_PART(gitlab_version, '.', 2))::text AS major_version,
       DATE_TRUNC('month', created_at) AS MONTH,
       COUNT (distinct host_id) AS UUID
FROM ANALYTICS.PINGS_VERSION_CHECKS
WHERE GITLAB_VERSION ILIKE '%ee%'
GROUP BY 1, 2 
HAVING COUNT (distinct host_id) > 1
ORDER BY 3 DESC