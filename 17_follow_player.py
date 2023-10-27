from db_config import execute_query


# follower and following are usernames
def follow(following, follower):
    sql_command_1 = f"""
    INSERT INTO follows(player_id, follower_id)
    VALUES ( (
        SELECT player_id
        FROM player
        WHERE username = '{following}'),
        
        (
        SELECT player_id
        FROM player
        WHERE username = '{follower}') )
    
    """
    sql_command_2 = """"""
    print(execute_query(sql_command_1))


if __name__ == '__main__':
    follow('nec', 'integer')
