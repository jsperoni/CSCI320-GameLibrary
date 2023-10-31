from db_config import execute_query

def delete_game_from_collection(collection_id, name):
    query = f"""UPDATE collection SET name = '{name}' WHERE collection_id = '{collection_id}'"""

    execute_query(query, params=(collection_id, name), fetch_results=False)

if __name__ == '__main__':
    delete_game_from_collection(collection_id = 1, name = "CC")