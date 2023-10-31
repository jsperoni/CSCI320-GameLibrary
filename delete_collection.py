from db_config import execute_query

def delete_collection(collection_id):
    query = "DELETE FROM collection WHERE collection_id = %s"

    execute_query(query, params=(collection_id,), fetch_results=False)

if __name__ == '__main__':
    delete_collection(collection_id=286)