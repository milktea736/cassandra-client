from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

def create_keyspace_and_table():
    CASSANDRA_NODES = ['127.0.0.1'] 
    CASSANDRA_USERNAME = 'cassandra'
    CASSANDRA_PASSWORD = 'cassandra'

    auth_provider = PlainTextAuthProvider(username=CASSANDRA_USERNAME, password=CASSANDRA_PASSWORD)
    cluster = Cluster(contact_points=CASSANDRA_NODES, auth_provider=auth_provider)
    session = cluster.connect()

    session.execute("""
        CREATE KEYSPACE IF NOT EXISTS sample
        WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}
    """)

    session.set_keyspace('sample')

    session.execute("""
        CREATE TABLE IF NOT EXISTS sample_table (
            id UUID PRIMARY KEY,
            name TEXT,
            age INT
        )
    """)

    print("Keyspace and table created successfully")

    cluster.shutdown()

if __name__ == "__main__":
    create_keyspace_and_table()
