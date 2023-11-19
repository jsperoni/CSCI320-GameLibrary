SELECT
    (SELECT COUNT(DISTINCT collection_id) FROM collection) AS total_collections,
    (
        SELECT COUNT(*) FROM (
            SELECT player_id, collection_id FROM (
                SELECT c.player_id, c.collection_id, gg.genre_id, COUNT(gg.game_id) as genre_count,
                    (SELECT genre_id FROM (
                        SELECT gg.genre_id, COUNT(gg.game_id) as cnt
                        FROM plays p
                        JOIN game_genre gg ON p.game_id = gg.game_id
                        WHERE p.player_id = c.player_id
                        GROUP BY gg.genre_id
                        ORDER BY cnt DESC
                        LIMIT 1
                    ) as sub_max_genre) as favorite_genre_id
                FROM collection c
                JOIN game_collection gc ON c.collection_id = gc.collection_id
                JOIN game_genre gg ON gc.game_id = gg.game_id
                GROUP BY c.player_id, c.collection_id, gg.genre_id
            ) AS genre_counts
            WHERE genre_count = (
                SELECT MAX(genre_count) FROM (
                    SELECT COUNT(gg.game_id) as genre_count
                    FROM game_collection gc
                    JOIN game_genre gg ON gc.game_id = gg.game_id
                    WHERE gc.collection_id = genre_counts.collection_id
                    GROUP BY gg.genre_id
                ) AS max_genre_counts
            ) AND genre_id = favorite_genre_id
        ) AS matching_collections
    ) AS collections_with_favorite_genre
