from db_config import execute_query


def create_play_session(player_id, game_id, start_time, end_time):
    sql_command = f"""
    INSERT INTO plays(player_id, game_id, start_time, end_time)
    VALUES ( {player_id}, {game_id}, '{start_time}', '{end_time}' )
    """

    execute_query(sql_command, fetch_results=False)


if __name__ == '__main__':
    create_play_session(4, 1699)
