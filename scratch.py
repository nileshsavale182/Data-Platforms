import duckdb

con = duckdb.connect("playground.duckdb")

con.execute("""
CREATE TABLE IF NOT EXISTS employees(
    id INTEGER,
    name VARCHAR,
    salary INTEGER
)
""")

con.execute("""
INSERT INTO employees VALUES
(1,'Alice',50000),
(2,'Bob',60000)
""")

result = con.execute("SELECT * FROM employees").fetchall()

print(result)

con.close()