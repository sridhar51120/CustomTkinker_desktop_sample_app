from cassandra_utils import get_cassandra_connections, close_cassandra_connections
from config_utils import get_config

def perform_cassandra_query():
    session = get_cassandra_session()
    
    # Your Cassandra queries go here
    rows = session.execute("SELECT * FROM your_table")
    for row in rows:
        print(row)

    close_cassandra_session(session)

if __name__ == "__main__":
    perform_cassandra_query()
