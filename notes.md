For SQLite, the syntax for date arithmetic is slightly different compared to other SQL databases like MySQL. In SQLite, you can use the `DATE` function to manipulate dates. Here's an alternative way to write your query using SQLite syntax:

```sql
SELECT *
FROM quarks
WHERE timestamp >= datetime('now', '-1 day');
```

This query selects all rows from the `quarks` table where the `timestamp` is greater than or equal to the current date minus 1 day.

Make sure that the `timestamp` column in your `quarks` table is in the correct date format for comparison. If it's stored as text, you might need to convert it to a proper date format using SQLite's date conversion functions.