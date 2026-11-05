-- Generic landing schema. Adapt types/columns to the source contract.
CREATE TABLE IF NOT EXISTS analytics_events (
  record_id BIGINT PRIMARY KEY,
  event_time TIMESTAMP,
  city VARCHAR(100),
  segment VARCHAR(50),
  category VARCHAR(100),
  amount NUMERIC(18,2)
);
