from db_config import execute_query

all_players = execute_query('SELECT * from "Player";')
print(all_players)
