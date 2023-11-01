from psycopg2 import connect
from sshtunnel import SSHTunnelForwarder
from rit_credentials import username, password

# SSH Configuration
ssh_host = 'starbug.cs.rit.edu'
ssh_port = 22
ssh_user = username
ssh_password = password

# PostgreSQL Configuration
pg_host = '127.0.0.1'
pg_port = 5432
pg_database = 'p320_31'
pg_user = username
pg_password = password


def execute_query(query, params=None, fetch_results=True):
    try:
        with SSHTunnelForwarder(
                (ssh_host, ssh_port),
                ssh_username=ssh_user,
                ssh_password=ssh_password,
                remote_bind_address=(pg_host, pg_port)
        ) as tunnel:
            with connect(
                    dbname=pg_database,
                    user=pg_user,
                    password=pg_password,
                    host=tunnel.local_bind_host,
                    port=tunnel.local_bind_port
            ) as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, params)

                    # Commit changes for non-select statements
                    conn.commit()

                    if fetch_results:
                        result = cursor.fetchall()
                        return result

    except Exception as e:
        print(f"An error occurred: {e}")
        return None