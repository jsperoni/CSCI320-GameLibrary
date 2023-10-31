from db_config import execute_query

def create_access_date(player_id):
    query = "INSERT INTO login_date VALUES (%s, NOW())"
    execute_query(query, params=(player_id,), fetch_results=False)

if __name__ == '__main__':
    create_access_date(player_id=2596)