from db_config import execute_query
import bcrypt
import binascii

def search_player(column_name, value):
    query = f"SELECT * FROM player WHERE {column_name} = %s;"
    return execute_query(query, params=(value,))

def does_username_exist(username):
    res = search_player(column_name='username', value=username)

    if not res:
        return False

    # get player id
    return res[0][0]

def does_password_match(username, password):
    user_details = search_player(column_name='username', value=username)

    if not user_details:
        return False

    stored_hashed_password = user_details[0][6]
    hashed_password_bytes = binascii.unhexlify(stored_hashed_password[2:])

    # return true if its exists
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password_bytes)

if __name__ == '__main__':
    print(search_player(column_name = "email", value = "email123@gmail.com"))