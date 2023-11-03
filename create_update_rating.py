from db_config import execute_query

# Updates a player rating and creates a new rating entry if one does not
# already exist for a game.
def rate(player_id, game_id, rating):
    sql_command_1 = f"""
    SELECT player_id, game_id
    FROM rates
    WHERE player_id = {player_id} AND
    game_id = {game_id}
    """

    sql_command_2 = f"""
    INSERT INTO rates(player_id, game_id, rating)
    VALUES({player_id}, {game_id}, {rating})
    """

    sql_command_3 = f"""
    UPDATE rates
    SET rating = {rating}
    WHERE player_id = {player_id} AND
    game_id = {game_id}
    """

    result = execute_query(sql_command_1, fetch_results=False)
    # print(result)

    if not result:
        # print('DEBUG: Result was empty. Inserting new rating entry.')
        # print(execute_query(sql_command_2))
        execute_query(sql_command_2, fetch_results=False)
    else:
        # print ('DEBUG: Result was not empty. Updating existing rating entry.')
        # print(execute_query(sql_command_3))
        execute_query(sql_command_3, fetch_results=False)


if __name__ == '__main__':
    rate(1597, 6, 4)