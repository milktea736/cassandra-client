import random
from uuid import uuid4
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

def insert_data():
    CASSANDRA_NODES = ['127.0.0.1']
    CASSANDRA_USERNAME = 'cassandra'
    CASSANDRA_PASSWORD = 'cassandra'

    auth_provider = PlainTextAuthProvider(username=CASSANDRA_USERNAME, password=CASSANDRA_PASSWORD)
    cluster = Cluster(contact_points=CASSANDRA_NODES, auth_provider=auth_provider)
    session = cluster.connect()

    session.set_keyspace('sample')

    for _ in range(100):
        user_id = uuid4()
        name = 'user_' + str(random.randint(1, 1000)) 
        age = random.randint(1, 100) 
        
        session.execute(
            "INSERT INTO sample_table (id, name, age) VALUES (%s, %s, %s)",
            (user_id, name, age)
        )

    print("100 rows inserted successfully")

    cluster.shutdown()

if __name__ == "__main__":
    insert_data()
