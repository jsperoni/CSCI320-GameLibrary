from db_config import execute_query

def does_player_have_platform(player_id, platform_id):
    query = """
    SELECT * FROM owns_platform 
    WHERE owns_platform.player_id = %s 
    AND owns_platform.platform_id = %s
    """
    # return structures look like
    # [(2424, 87)] if they have
    # [] if they don't
    return execute_query(query, params=(player_id,platform_id)) != []

if __name__ == '__main__':
    print(does_player_have_platform(player_id=2424, platform_id=87))