from db_config import execute_query

def search_player(column_name, value):
    query = f"SELECT * FROM player WHERE {column_name} = %s;"
    return execute_query(query, params=(value,))

if __name__ == '__main__':
    print(search_player(column_name = "email", value = "email123@gmail.com"))