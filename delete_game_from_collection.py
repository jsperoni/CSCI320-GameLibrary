from db_config import execute_query

def delete_game_from_collection(collection_id, game_id):
    query = f"""DELETE FROM game_collection WHERE collection_id = '{collection_id}' AND game_id = '{game_id}'"""

    execute_query(query, params=(collection_id, game_id), fetch_results=False)

if __name__ == '__main__':
    delete_game_from_collection(collection_id=371, game_id=114)