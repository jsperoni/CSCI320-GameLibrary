SELECT g.genre_id, a.name FROM plays p
    JOIN game_genre g ON p.game_id = g.game_id
    JOIN genre a ON g.genre_id = a.genre_id
    WHERE (start_time BETWEEN '2023-10-01' AND '2023-11-01')
    OR (end_time BETWEEN '2023-10-01' AND '2023-11-01')
    ORDER BY g.genre_id ASC