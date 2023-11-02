from db_config import execute_query


def post_processing(query, param):
    results = execute_query(query, (param,))
    final = []
    key = None
    counter = -1
    for entry in results:
        if key != None and key == entry[0]:
            for j in range(len(entry)-1):
                if entry[j] not in final[counter][j]:
                    final[counter][j].append(entry[j])
        else:
            final.append([])
            counter = counter + 1
            for piece in entry:
                final[counter].append([piece])
        key = entry[0]
    return final

# assumes sort is passed in sql formal
def search_game_name(name, sort="g.title ASC, r.release_date DESC"):
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
        UPPER(g.title) LIKE %s
    ORDER BY
        """ + sort
    return post_processing(query, param)

def search_game_id(id, sort="g.title ASC, r.release_date DESC"):
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
        g.game_id = %s
    ORDER BY
        """ + sort
    return post_processing(query, id)

# assumes sort is passed in sql format
def search_game_platform(platform, sort="g.title ASC, r.release_date DESC"):
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
        UPPER(p.name) LIKE %s
    ORDER BY
        """ + sort
    return post_processing(query, param)

# assumes date is passed in correct format (not sure if the %% works for datetimes)
# assumes sort is passed in sql format
def search_game_date(date, sort="g.title ASC, r.release_date DESC"):
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
    return post_processing(query, param)

def search_game_devs(developer, sort="g.title ASC, r.release_date DESC"):
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
        UPPER(c.name) LIKE %s
    ORDER BY
        """ + sort
    return post_processing(query, param)

def search_game_price(price, sort="g.title ASC, r.release_date DESC"):
    query = """
    SELECT
        g.game_id,
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
    return post_processing(query, price)

def search_game_genre(genre, sort="g.title ASC, r.release_date DESC"):
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
        UPPER(ge.name) LIKE %s
    ORDER BY
        """ + sort
    return post_processing(query, param)

if __name__ == '__main__':
    # print(search_game_id(16))
    print(search_game_name("GALACTIC"))
    # print(search_game_platform("PlayStation"))
    # print(search_game_date("2023-08-31"))
    # print(search_game_devs("am"))
    # print(search_game_price(21.62))
    # print(search_game_genre("Tower Defense"))