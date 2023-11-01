from db_config import execute_query


def add_game_to_library(player_id, game_id):
    query = f"""
            INSERT INTO owns(player_id, game_id)
            VALUES (%s, %s)
            """
    execute_query(query, params=(player_id, game_id), fetch_results=False)


if __name__ == '__main__':
    add_game_to_library(player_id=371, video_game_id=115)