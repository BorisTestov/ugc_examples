from clickhouse_driver import Client

client = Client(host="localhost")
client.execute("SHOW DATABASES")
client.execute("CREATE DATABASE IF NOT EXISTS example ON CLUSTER company_cluster")
client.execute(
    "CREATE TABLE IF NOT EXISTS example.regular_table ON CLUSTER company_cluster (id Int64, x Int32) Engine=MergeTree() ORDER BY id"
)
client.execute("INSERT INTO example.regular_table (id, x) VALUES (1, 10), (2, 20)")
print(client.execute("SELECT * FROM example.regular_table"))
