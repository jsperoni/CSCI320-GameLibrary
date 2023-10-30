from db_config import execute_query

def create_collection(player_id, collection_name):
    query = "INSERT INTO collection (player_id, name) VALUES (%s, %s)"
    execute_query(query, params=(player_id, collection_name), fetch_results=False)

if __name__ == '__main__':
    create_collection(player_id=2596, collection_name='My Collection')