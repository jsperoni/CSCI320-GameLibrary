import bcrypt
from db_config import execute_query

def create_player(username, password, email, first_name, last_name):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    sql_command = """
    INSERT INTO player(username, password, email, first_name, last_name, creation_date)
    VALUES (%s, %s, %s, %s, %s, NOW());
    """
    execute_query(sql_command, params=(username, hashed_password, email, first_name, last_name), fetch_results=False)

if __name__ == '__main__':
    create_player(username = 'user12345',
    password = 'pass1234',
    email = 'email12345@gmail.com',
    first_name = 'firstname',
    last_name = 'secondname')