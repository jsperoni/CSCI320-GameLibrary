from db_config import execute_query


def play_game(player_id, game_id):
    sql_command_1 = f"""
    SELECT title, NOW()
    FROM game
    WHERE game_id = {game_id}
    """

    results = execute_query(sql_command_1)
    print(f"Playing '{results[0][0]}'...")
    print(f"Press ENTER to end game")

    input()

    sql_command_2 = f"""
    INSERT INTO plays(player_id, game_id, start_time, end_time)
    VALUES ( {player_id}, {game_id}, '{results[0][1]}', NOW() )
    """

    print(execute_query(sql_command_2))


def play_random_in_collection(collection_id, player_id):
    sql_command = f"""
    SELECT game_id
    FROM (
        SELECT game_id
        FROM game_collection
        WHERE collection_id = '{collection_id}' ) AS c
    ORDER BY RANDOM()
    LIMIT 1
    """

    game_to_play = execute_query(sql_command)[0][0]
    play_game(player_id, game_to_play)


if __name__ == '__main__':
    print(play_random_in_collection(4, 1699))
