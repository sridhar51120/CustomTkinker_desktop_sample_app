from cassandra.cluster import Cluster

def get_cassandra_connections():
    cluster = Cluster([get_config('cassandra_host')])
    session = cluster.connect()
    return session

def close_cassandra_connections(session):
    session.cluster.shutdown()
    session.shutdown()
