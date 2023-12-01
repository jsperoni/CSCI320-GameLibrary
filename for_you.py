from db_config import execute_query


# unfinished
def for_you(player_id):
    query = f"""
SELECT title, game_id
FROM game
NATURAL JOIN (SELECT game_id
              FROM (SELECT DISTINCT game_id,
                                    SUM((EXTRACT(EPOCH FROM (end_time - start_time)))) / 1000 *
                                    count(DISTINCT player_id) AS score
                    FROM plays
                    WHERE player_id in (SELECT DISTINCT player_id
                                        FROM (SELECT player_id,
                                                     SUM((EXTRACT(EPOCH FROM (end_time - start_time))))   AS total_time,
                                                     genre_id,
                                                     ROW_NUMBER() OVER (PARTITION BY player_id, genre_id) AS row_num
                                              FROM plays p
                                                       NATURAL JOIN game_genre g
                                              WHERE EXTRACT(EPOCH FROM (end_time - start_time)) > 0
                                              GROUP BY player_id, genre_id
                                              ORDER BY player_id, total_time DESC) AS sub1
                                        WHERE row_num <= 3
                                          AND genre_id in (SELECT genre_id
                                                           FROM (SELECT genre_id,
                                                                        SUM(EXTRACT(EPOCH FROM (end_time - start_time))) as time
                                                                 FROM plays
                                                                          NATURAL JOIN game_genre
                                                                 WHERE player_id = {player_id}
                                                                 GROUP BY genre_id
                                                                 ORDER BY time DESC
                                                                 LIMIT 3) as gen)
                                        UNION
                                        DISTINCT
                                        SELECT DISTINCT player_id
                                        FROM (SELECT player_id,
                                                     SUM((EXTRACT(EPOCH FROM (end_time - start_time))))  AS total_time,
                                                     cont_id,
                                                     ROW_NUMBER() OVER (PARTITION BY player_id, cont_id) AS row_num
                                              FROM plays p
                                                       NATURAL LEFT JOIN publisher
                                                       NATURAL LEFT JOIN contributor
                                              WHERE EXTRACT(EPOCH FROM (end_time - start_time)) > 0
                                              GROUP BY player_id, cont_id
                                              ORDER BY player_id, total_time DESC) AS sub2
                                        WHERE row_num <= 3
                                          AND cont_id in (SELECT cont_id
                                                          FROM (SELECT cont_id,
                                                                       SUM(EXTRACT(EPOCH FROM (end_time - start_time))) AS time
                                                                FROM plays
                                                                         NATURAL JOIN publisher
                                                                WHERE player_id = {player_id}
                                                                GROUP BY cont_id
                                                                ORDER BY time DESC
                                                                LIMIT 3) as con1
                                                          UNION
                                                          DISTINCT
                                                          SELECT cont_id
                                                          FROM (SELECT cont_id,
                                                                       SUM(EXTRACT(EPOCH FROM (end_time - start_time))) AS time
                                                                FROM plays
                                                                         NATURAL JOIN developer
                                                                WHERE player_id = {player_id}
                                                                GROUP BY cont_id
                                                                ORDER BY time DESC
                                                                LIMIT 3) as con2))
                    GROUP BY game_id
                    ORDER BY score DESC) as g
              WHERE score > 0
              UNION
              DISTINCT
              (SELECT game_id
               FROM game_genre
               WHERE genre_id in (SELECT genre_id
                                  FROM (SELECT genre_id, SUM(EXTRACT(EPOCH FROM (end_time - start_time))) as time
                                        FROM plays
                                                 NATURAL JOIN game_genre
                                        WHERE player_id = {player_id}
                                        GROUP BY genre_id
                                        ORDER BY time DESC
                                        LIMIT 3) as a)
               ORDER BY RANDOM()
               LIMIT 3)
              UNION
              DISTINCT
              (SELECT game_id
               FROM developer
               WHERE cont_id in (SELECT cont_id
                                 FROM (SELECT cont_id, SUM(EXTRACT(EPOCH FROM (end_time - start_time))) as time
                                       FROM plays
                                                NATURAL JOIN developer
                                       WHERE player_id = {player_id}
                                       GROUP BY cont_id
                                       ORDER BY time DESC
                                       LIMIT 3) as b)
               ORDER BY RANDOM()
               LIMIT 3)
              UNION
              DISTINCT
              (SELECT game_id
               FROM publisher
               WHERE cont_id in (SELECT cont_id
                                 FROM (SELECT cont_id, SUM(EXTRACT(EPOCH FROM (end_time - start_time))) as time
                                       FROM plays
                                                NATURAL JOIN publisher
                                       WHERE player_id = {player_id}
                                       GROUP BY cont_id
                                       ORDER BY time DESC
                                       LIMIT 3) as c)
               ORDER BY RANDOM()
               LIMIT 3)) as games
    """
    return execute_query(query, params=(player_id,))


if __name__ == '__main__':
    print(for_you(1607))
