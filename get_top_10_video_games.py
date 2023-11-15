from db_config import execute_query

def get_top_10_video_games_highest_rating(player_id):
    query = """
    SELECT g.title, r.rating
    FROM game g
        JOIN rates r on g.game_id = r.game_id
    WHERE r.player_id = %s
    ORDER BY r.rating DESC
    LIMIT 10
    """
    return execute_query(query, params=(player_id,))

def get_top_10_video_games_most_played(player_id):
    query = """
    SELECT g.title,
       SUM(EXTRACT(EPOCH FROM (p.end_time - p.start_time))) as total_play_seconds
    FROM plays p
    JOIN game g ON p.game_id = g.game_id
    WHERE p.player_id = %s
    GROUP BY g.game_id, g.title
    ORDER BY total_play_seconds DESC
    LIMIT 10;
    """
    return execute_query(query, params=(player_id,))

def get_top_10_video_games_most_played_and_rating(player_id):
    query = """
    SELECT g.title,
       r.rating,
       COALESCE(SUM(EXTRACT(EPOCH FROM (p.end_time - p.start_time))), 0) as total_play_seconds
    FROM game g
    LEFT JOIN rates r ON g.game_id = r.game_id AND r.player_id = %s
    FULL OUTER JOIN plays p ON g.game_id = p.game_id AND p.player_id = %s
    WHERE r.player_id = %s OR p.player_id = %s
    GROUP BY g.title, r.rating
    ORDER BY total_play_seconds DESC, r.rating DESC NULLS LAST
    LIMIT 10;
    """
    return execute_query(query, params=(player_id,))

