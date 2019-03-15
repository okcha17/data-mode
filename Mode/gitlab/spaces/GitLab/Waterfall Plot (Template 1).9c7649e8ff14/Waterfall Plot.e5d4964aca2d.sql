    SELECT category,
           value,
           CASE WHEN category != 'Total' AND value >= 0 THEN value
                ELSE 0 END AS revenue_y,
           CASE WHEN category!= 'Total' AND value < 0 THEN value*-1
                ELSE 0 END AS cost_y,
           CASE WHEN category != 'Total' THEN 0
                ELSE value END AS total_y,
           '$'||value||'k' AS text
      FROM modeanalytics.sample_ds5 