from db_config import execute_query

def add_game_to_collection(collection_id, player_id, video_game_id):
    query = "INSERT INTO game_collection VALUES (%s, %s, %s)"
    execute_query(query, params=(collection_id, player_id, video_game_id), fetch_results=False)

if __name__ == '__main__':
    add_game_to_collection(collection_id=371, video_game_id=115)