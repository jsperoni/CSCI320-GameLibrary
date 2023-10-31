from db_config import execute_query

def search_game_by_id(game_id):
    sql = "SELECT * FROM game WHERE game_id = %s"

    return execute_query(sql, (game_id,))

# assumes sort is passed in sql formal
def search_game_name(name, sort="g.title ASC"):
    param = "%" + name + "%"
    query = """
    SELECT
        g.title,
        p.name,
        c.name,
        r.price,
        ge.name
    FROM
        game g
    JOIN
        developer d ON g.game_id = d.game_id
    JOIN
        contributor c ON c.cont_id = d.cont_id
    JOIN
        runs_on r ON g.game_id = r.game_id
    JOIN
        platform p ON r.platform_id = p.platform_id
    JOIN
        game_genre gg ON g.game_id = gg.game_id
    JOIN
        genre ge ON gg.genre_id = ge.genre_id
    WHERE
        g.title LIKE %s
    ORDER BY
        """ + sort
    return execute_query(query, (param,))

# assumes sort is passed in sql format
def search_game_platform(platform, sort="g.title ASC"):
    param = "%" + platform + "%"
    query = """
    SELECT
        g.title,
        p.name,
        c.name,
        r.price,
        ge.name
    FROM
        game g
    JOIN
        developer d ON g.game_id = d.game_id
    JOIN
        contributor c ON c.cont_id = d.cont_id
    JOIN
        runs_on r ON g.game_id = r.game_id
    JOIN
        platform p ON r.platform_id = p.platform_id
    JOIN
        game_genre gg ON g.game_id = gg.game_id
    JOIN
        genre ge ON gg.genre_id = ge.genre_id
    WHERE
        p.name LIKE %s
    ORDER BY
        """ + sort
    return execute_query(query, (param,))

# assumes date is passed in correct format (not sure if the %% works for datetimes)
# assumes sort is passed in sql format
def search_game_date(date, sort="g.title ASC"):
    param = "%" + date + "%"
    query = """
    SELECT
        g.title,
        p.name,
        c.name,
        r.price,
        ge.name
    FROM
        game g
    JOIN
        developer d ON g.game_id = d.game_id
    JOIN
        contributor c ON c.cont_id = d.cont_id
    JOIN
        runs_on r ON g.game_id = r.game_id
    JOIN
        platform p ON r.platform_id = p.platform_id
    JOIN
        game_genre gg ON g.game_id = gg.game_id
    JOIN
        genre ge ON gg.genre_id = ge.genre_id
    WHERE
        r.release_date = %s
    ORDER BY
        """ + sort
    return execute_query(query, (param,))

def search_game_devs(developer, sort="g.title ASC"):
    param = "%" + developer + "%"
    query = """
    SELECT
        g.title,
        p.name,
        c.name,
        r.price,
        ge.name
    FROM
        game g
    JOIN
        developer d ON g.game_id = d.game_id
    JOIN
        contributor c ON c.cont_id = d.cont_id
    JOIN
        runs_on r ON g.game_id = r.game_id
    JOIN
        platform p ON r.platform_id = p.platform_id
    JOIN
        game_genre gg ON g.game_id = gg.game_id
    JOIN
        genre ge ON gg.genre_id = ge.genre_id
    WHERE
        c.name LIKE %s
    ORDER BY
        """ + sort
    return execute_query(query, (param,))

def search_game_price(price, sort="g.title ASC"):
    query = """
    SELECT
        g.title,
        p.name,
        c.name,
        r.price,
        ge.name
    FROM
        game g
    JOIN
        developer d ON g.game_id = d.game_id
    JOIN
        contributor c ON c.cont_id = d.cont_id
    JOIN
        runs_on r ON g.game_id = r.game_id
    JOIN
        platform p ON r.platform_id = p.platform_id
    JOIN
        game_genre gg ON g.game_id = gg.game_id
    JOIN
        genre ge ON gg.genre_id = ge.genre_id
    WHERE
        r.price = %s
    ORDER BY
        """ + sort
    return execute_query(query, (price,))

def search_game_genre(genre, sort="g.title ASC"):
    param = "%" + genre + "%"
    query = """
    SELECT
        g.title,
        p.name,
        c.name,
        r.price,
        ge.name
    FROM
        game g
    JOIN
        developer d ON g.game_id = d.game_id
    JOIN
        contributor c ON c.cont_id = d.cont_id
    JOIN
        runs_on r ON g.game_id = r.game_id
    JOIN
        platform p ON r.platform_id = p.platform_id
    JOIN
        game_genre gg ON g.game_id = gg.game_id
    JOIN
        genre ge ON gg.genre_id = ge.genre_id
    WHERE
        ge.name LIKE %s
    ORDER BY
        """ + sort
    return execute_query(query, (param,))

if __name__ == '__main__':
    print(search_game_name("Galactic")) #works, however output is not as expected
    # print(search_game_platform("PlayStation")) works ^
    # print(search_game_date("2023-08-31")) ^
    # print(search_game_devs("am")) ^
    # print(search_game_price(21.62)) ^ 
    # print(search_game_genre("Tower Defense")) # ^