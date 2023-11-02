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


def does_player_have_platform_by_name(player_id, platform_list):
    have_platform = False
    for i in range(0, len(platform_list)-1):
        name = platform_list[i].upper()
        param = "%" + name + "%"
        query = """
        SELECT o.player_id, p.platform_id, p.name FROM owns_platform o
        JOIN platform p ON p.platform_id = o.platform_id
        WHERE  UPPER(p.name) LIKE %s AND o.player_id = %s
        """
        have_platform = execute_query(query, params=(param, player_id)) != []
        if have_platform:
            return have_platform
    return have_platform


if __name__ == '__main__':
    print(does_player_have_platform(player_id=2424, platform_id=87))