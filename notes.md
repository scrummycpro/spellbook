For SQLite, the syntax for date arithmetic is slightly different compared to other SQL databases like MySQL. In SQLite, you can use the `DATE` function to manipulate dates. Here's an alternative way to write your query using SQLite syntax:

```sql
SELECT *
FROM quarks
WHERE timestamp >= datetime('now', '-1 day');
```

This query selects all rows from the `quarks` table where the `timestamp` is greater than or equal to the current date minus 1 day.

Make sure that the `timestamp` column in your `quarks` table is in the correct date format for comparison. If it's stored as text, you might need to convert it to a proper date format using SQLite's date conversion functions.


## Requirements
- SQLite3
- Bash

## Note
- The `spellbook` Bash script is assumed to be available in your system and properly configured to cast spells on quarks.
- Adjust the path to the `whispers.db` database file and the `spellbook` script if necessary.

## Author
Nicholas Franklin

It appears that the installation of `wordcloud` using pipx was successful, but Python is unable to locate the `wordcloud` module when you run your script.

This issue might occur if the Python interpreter is not aware of the pipx-managed virtual environment where `wordcloud` is installed.

To resolve this, you need to ensure that the Python interpreter used to run your script is aware of the virtual environment created by pipx.

Here's what you can do:

1. Activate the pipx-managed virtual environment:
   ```bash
   source ~/.local/pipx/venvs/wordcloud/bin/activate
   ```

2. Run your script again:
   ```bash
   python3 mind-map.py
   ```

If this works, it means that your script can now access the `wordcloud` module installed in the virtual environment.

If you want to avoid manually activating the virtual environment every time you run your script, you can modify the shebang line at the beginning of your script to point to the Python interpreter within the virtual environment. For example:
```python
#!/Users/richmack/.local/pipx/venvs/wordcloud/bin/python3
```
Replace the path with the actual path to the Python interpreter in your virtual environment.

Let me know if you need further assistance!
