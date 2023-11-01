import random
from time import time
from datetime import datetime

from add_game_to_collection import add_game_to_collection
from create_access_date import create_access_date
from create_collection import create_collection
from create_player import create_player
from delete_collection import delete_collection
from delete_game_from_collection import delete_game_from_collection
from find_all_followers import find_following
from follow_player import create_follow, delete_follow
from search_collections import search_collection
from search_game_collections import search_game_collections
from search_games import search_game_by_id
from search_player import does_username_exist, does_password_match, search_player
from update_collection_name import update_collection_name
from create_play_session import create_play_session

# global variable so we dont have to pass it around always
player_id = ""

def login():
    global player_id

    while True:
        username = input("Enter username: ")
        local_player_id = does_username_exist(username)

        if local_player_id:
            password = input("Enter password: ")
            if does_password_match(username, password):
                print(f"Logged in with id {local_player_id}!")
                create_access_date(local_player_id)
                player_id = local_player_id

                return True
            else:
                print("Invalid password")
        else:
            temp = input("Account does not exist. Create new account? \n"
                         "(Y)es/(N)o\n")
            if temp.upper() == "N":
                continue
            elif temp.upper() == "Y":
                password = input("Enter password: ")

                local_player_id = create_player(
                    username=username,
                    password=password,
                    email=f"{username}@gmail.com",
                    first_name=f"{username} first name",
                    last_name=f"{username} last name"
                )
                create_access_date(local_player_id)
                player_id = local_player_id

                return True
            else:
                print("Unknown input... Start again")
                continue


def collection_processing():
    collections_list = search_collection(player_id)

    print("Collections:")

    if not collections_list:
        print("No collections")
    else:
        for collection in collections_list:
            print(f"id={collection[0]} name={collection[1]}, games={collection[2]}, total_play_time (H:M)={round(collection[3])}")

    while True:
        # sql query to get list of all collections should be inside while loop
        collection_option = input("(C)reate | (V)iew | (B)ack \n")
        if collection_option.upper() == "C":
            collection_name = input("Enter collection name to create (leave empty to go back): ")
            if collection_name == "":
                return
            else:
                create_collection(player_id=player_id, collection_name=collection_name)
                print("Collection created")
        elif collection_option.upper() == "V":
            collection_id = input("Enter collection id to look into (leave empty to go back): ")

            if collection_id == "":
                return

            matching_row = list(filter(lambda col: col[0] == int(collection_id), collections_list))

            if matching_row:
                view_collection(collection_name=matching_row[0][1], collection_id=collection_id)
            else:
                print("Collection not found")
                continue
        elif collection_option.upper() == "B":
            break
        else:
            print("Unknown command... Try again")
    return


def view_collection(collection_name, collection_id):
    print(f"Viewing {collection_name}")

    while True:
        view_option = input("(D)elete | (E)dit | (V)iew collection games | (B)ack \n")
        if view_option.upper() == "D":
            delete_collection(collection_id)
            print("Collection deleted")
        elif view_option.upper() == "E":
            rename_collection(collection_id=collection_id, collection_name=collection_name)
            break
        elif view_option.upper() == "V":
            view_collection_games(collection_id=collection_id, collection_name=collection_name)
        elif view_option.upper() == "B":
            break
        else:
            print("Unknown command... Try again")
    return


def view_collection_games(collection_id, collection_name):
    games_in_collection = search_game_collections(collection_id)

    print(f"Game in collection {collection_name}:")

    if not games_in_collection:
        print("No games")
    else:
        for game in games_in_collection:
            print(f"id={game[0]} name={game[1]}, esrb={game[2]}")

    while True:
        view_option = input("(A)dd | (D)elete | (P)lay | (R)andom play | (B)ack \n")
        if view_option.upper() == "A":
            game_id = input("Enter id of the game you wish to add to collection (leave blank to go back): ")

            if game_id == "":
                continue

            game = search_game_by_id(game_id)

            if not game:
                print("No game found")
                continue

            add_game_to_collection(collection_id=collection_id, video_game_id=game[0][0])
            print(f"Game {game[0][1]} added")
        elif view_option.upper() == "D":
            game_id = input("Enter name of the game you wish to delete from collection (leave blank to go back): ")

            if game_id == "":
                continue

            delete_game_from_collection(collection_id=collection_id, game_id=int(game_id))
            print("Game deleted")

        elif view_option.upper() == "P":
            if len(games_in_collection) == 0:
                print("Collection is empty. Try again")
            else:
                game_id = input("Enter id of the game you wish to play (leave blank to go back): ")
                if game_id == "":
                    continue

                matching_row = list(filter(lambda col: col[0] == int(game_id), games_in_collection))

                if matching_row:
                    # check if the game is in this collection...
                    play_game(game_id=matching_row[0][0], name=matching_row[0][1])
                else:
                    print("No such game in collection...")
        elif view_option.upper() == "R":
            if len(games_in_collection) == 0:
                print("Collection is empty. Try again")
            else:
                temp_int = random.randint(0, len(games_in_collection)-1)
                chosen = games_in_collection[temp_int]
                # from 0 to end of list containing all games in the collection
                print("Random game chosen is '" + chosen[1] + "'")
                play_game(game_id=chosen[0], name=chosen[1])


def rename_collection(collection_id, collection_name):
    new_name = input("Enter new name for collection: '" + collection_name + "' : ")

    update_collection_name(collection_id=collection_id, name=new_name)

    print(f"Collection {collection_name} renamed to {new_name}")

    return


def videogames_processing():
    while True:
        vg_option = input("(S)tore | (L)ibrary | (B)ack \n")
        if vg_option.upper() == "B":
            return
        elif vg_option.upper() == "S":
            store_processing()
        elif vg_option.upper() == "L":
            library_processing()
        else:
            print("Unknown command... Try again")


def store_processing():
    search_result = []  # list of all games initially, then changes when user performs search...
    while True:
        # not sure about the structure; need further discussion
        store_option = input("(S)earch | (B)uy | (R)ate | (E)xit \n")
        if store_option.upper() == "E":
            break
        elif store_option.upper() == "S":
            search_result = search_games()
        elif store_option.upper() == "B":
            game_name = input("Enter the name of the game to buy (leave blank to go back): ")
            if game_name == "":
                continue
            elif game_name.upper() in search_result:  # would need to change 'search_result' to list containing games
                buy_game(game_name)
            else:
                print(game_name + " does not exist. Try again")

        elif store_option.upper() == "R":
            game_to_rate = input("Enter the name of the game you wish to rate (leave blank to go back): ")
            if game_to_rate == "":
                continue
            elif game_to_rate.upper in search_result:
                rate_game(game_to_rate)
            else:
                print("Game not found")
        else:
            print("Unknown command... Try again")
    return


def buy_game(game_name):
    confirmation = input("(A)ccept | (R)eject")
    if confirmation.upper() == "A":
        # sql statement to buy game
        print("Game '" + game_name + "' was successfully bought!")
    elif confirmation.upper() == "R":
        return
    else:
        print("Unexpected input. Returning back to store")
        return


def search_games():
    temp_output_list = []
    print("You can search by:")
    search_options = input("(N)ame | (P)latform | (R)elease date | (D)evelopers | (G)enre | (C)ost \n")
    #
    return temp_output_list


def rate_game(game_name):
    rating = int(input("Enter the rating for '" + game_name + "' (from 1 to 5"))
    if rating > 5 or rating < 1:
        print("Invalid argument")
    else:
        # sql statement to rate the game
        return


def library_processing():
    search_result = []  # list of all games owned, then changes when user performs search...
    while True:
        # not sure about the structure; need further discussion
        library_option = input("(S)earch | (P)lay | (R)ate | (E)xit \n")
        if library_option.upper() == "E":
            break
        elif library_option.upper() == "S":
            search_result = search_games()
        elif library_option.upper() == "P":
            game_name = input("Enter name of the game you wish to play (leave blank to go back): ")
            if game_name == "":
                continue
            elif game_name in search_result:  # need to change to list of games in library
                # check if the game is in this collection...
                play_game(name=game_name)
            else:
                print("No such game in library...")
        elif library_option.upper() == "R":
            game_to_rate = input("Enter the name of the game you wish to rate (leave blank to go back): ")
            if game_to_rate == "":
                continue
            elif game_to_rate.upper in search_result:
                rate_game(game_to_rate)
            else:
                print("Game not found")
        else:
            print("Unknown command... Try again")
    return


def play_game(game_id, name):
    start_time = time()
    start_time_formatted = datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')

    while True:
        print("Starting the game '" + name + "'")
        temp = input("(E)xit to leave the game.. \n")
        if temp.upper() == "E":
            break

    end_time = time()
    end_time_formatted = datetime.fromtimestamp(end_time).strftime('%Y-%m-%d %H:%M:%S')

    create_play_session(player_id=player_id, game_id=game_id, start_time=start_time_formatted,
                        end_time=end_time_formatted)

    print(f"Played the game for {round(end_time - start_time, 2)} seconds")

    return


def user_processing():
    while True:
        user_option = input("(S)earch by email | (F)ollowing list | (B)ack \n")
        if user_option.upper() == "B":
            break
        elif user_option.upper() == "F":
            follow_list()
        elif user_option.upper() == "S":
            email = input("Enter email to search for (leave blank to go back): ")
            search_users(email)
    return


def follow_list():
    following = find_following(player_id)

    if not following:
        print("You have no followers")
        return

    for player in following:
        print(f"id={player[0]}, username={player[1]}")

    while True:
        opt = input("(B)ack | (U)nfollow \n")
        if opt.upper() == "B":
            break
        elif opt.upper() == "U":
            user_id = input("Enter the user id to unfollow (leave blank to go back): ")

            if user_id == "":
                continue

            matching_row = list(filter(lambda col: col[0] == int(user_id), following))

            if matching_row:
                delete_follow(unfollowing_id=matching_row[0][0], unfollower_id=player_id)
                print(f"{matching_row[0][1]} unfollowed")
            else:
                print("User not found")
                continue
    return


def search_users(email):
    result = search_player(column_name='email', value=email)

    if not result:
        print(f"No user with email {email} found")
        return

    # print username
    username_of_search = result[0][1]
    id_of_search = result[0][0]
    print(f"User found: {username_of_search}")

    while True:
        # sql command to check if the user is already followed
        opt = input("(F)ollow | (U)nfollow | (B)ack \n")
        if opt.upper() == "B":
            break
        elif opt.upper() == "F":
            create_follow(following_id=id_of_search, follower_id=player_id)
            print(f"Followed {username_of_search}")
        elif opt.upper() == "U":
            delete_follow(unfollowing_id=id_of_search, unfollower_id=player_id)
            print(f"Unfollowed {username_of_search}")
        else:
            print("Unknown command. Try again")
            continue
    return


def start_ui():
    # add player_id as the second value for the return of login...?
    logged_in = login()
    while logged_in:
        print("Main menu")
        menu_option = input("(C)ollections | (V)ideogames | (U)ser | (Q)uit \n")
        if menu_option.upper() == "C":
            collection_processing()
        elif menu_option.upper() == "V":
            videogames_processing()
        elif menu_option.upper() == "U":
            user_processing()
        elif menu_option.upper() == "Q":
            print("Logging out!")
            break
        else:
            print("Unknown command.. Try again")


if __name__ == '__main__':
    while True:
        start_ui()
