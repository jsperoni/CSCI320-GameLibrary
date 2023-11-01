from db_config import execute_query


# follower and following are usernames
def create_follow(following_id, follower_id):
    sql_command = "INSERT INTO follows VALUES (%s, %s)"
    execute_query(sql_command, params=(following_id, follower_id), fetch_results=False)

def delete_follow(unfollowing_id, unfollower_id):
    sql_command = "DELETE FROM follows WHERE player_id=%s and follower_id = %s"
    execute_query(sql_command, params=(unfollowing_id, unfollower_id), fetch_results=False)

if __name__ == '__main__':
    delete_follow('nec', 'integer')
