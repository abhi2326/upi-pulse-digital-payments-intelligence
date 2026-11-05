-- UPI Pulse: India's Digital Payments Intelligence Platform | PostgreSQL-compatible starter analysis
SELECT city, segment, category,
       COUNT(*) AS records,
       ROUND(SUM(amount),2) AS total_value,
       ROUND(AVG(amount),2) AS average_value
FROM analytics_events
GROUP BY 1,2,3
ORDER BY total_value DESC;

-- Monthly trend
SELECT DATE_TRUNC('month', event_time) AS month,
       COUNT(*) AS records, SUM(amount) AS total_value
FROM analytics_events
GROUP BY 1 ORDER BY 1;
