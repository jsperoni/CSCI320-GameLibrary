import random


def login():
    while True:
        username = input("Enter username: ")
        temp_un_list = ["123"]
        temp_pw_list = ["123"]
        if username in temp_un_list:
            password = input("Enter password: ")
            if password in temp_pw_list:
                print("Logged in!")
                user_id = 10  # query the id from sql
                return True, user_id
        else:
            temp = input("Account does not exist. Create new account? \n"
                         "(Y)es/(N)o\n")
            if temp.upper() == "N":
                continue
            elif temp.upper() == "Y":
                temp_un_list.append(username)
                password = input("Enter password: ")
                temp_pw_list.append(password)
                user_id = 10  # query the id from sql
                return True, user_id
            else:
                print("Unknown input... Start again")
                continue


def collection_processing(user_id):
    page_length = 10
    current_page = 1
    temp_collections_list = []
    while True:
        # sql query to get list of all collections should be inside while loop
        collection_option = input("(C)reate | (V)iew | (N)ext page | (P)revious page | (B)ack \n")
        if collection_option.upper() == "C":
            collection_name = input("Enter collection name to create (leave empty to go back): ")
            if collection_name == "":
                return
            else:
                create_collection(collection_name)
        elif collection_option.upper() == "V":
            collection_name = input("Enter collection name to look into (leave empty to go back): ")
            if collection_name == "":
                return
            elif collection_name.upper() in temp_collections_list:
                view_collection(collection_name)
            else:
                print("Collection not found")
                continue
        elif collection_option.upper() == "B":
            break
        elif collection_option.upper() == "N":
            # if current_page != ((len(list_of_all_games)/10)+1)
            current_page += 1
        elif collection_option.upper() == "P":
            if current_page != 0:
                current_page -= 1
        else:
            print("Unknown command... Try again")
    return


def create_collection(collection_name):
    # SQL statement to create collection with "collection_name" as name
    return


def view_collection(collection_name):
    while True:
        view_option = input("(D)elete | (E)dit | (V)iew collection | (B)ack \n")
        if view_option.upper() == "D":
            delete_collection(collection_name)
        elif view_option.upper() == "E":
            rename_collection(collection_name)
            break
        elif view_option.upper() == "V":
            view_collection_games(collection_name)
        elif view_option.upper() == "B":
            break
        else:
            print("Unknown command... Try again")
    return


def view_collection_games(collection_name):
    # sql statement to get all the games in the collection
    # add pages later
    temp_game_list = ["1", "2", "Hello"]
    while True:
        view_option = input("(A)dd | (D)elete | (P)lay | (R)andom play | (B)ack \n")
        if view_option.upper() == "A":
            game_name = input("Enter name of the game you wish to add to collection (leave blank to go back): ")
            if game_name == "":
                continue
            elif game_name.upper() in temp_game_list:
                add_to_collection(collection_name, game_name)
            else:
                print("No such game exists")
                continue
        elif view_option.upper() == "D":
            game_name = input("Enter name of the game you wish to delete from collection (leave blank to go back): ")
            if game_name == "":
                continue
            elif game_name.upper() in temp_game_list:
                delete_from_collection(collection_name, game_name)
            else:
                print("No such game in collection")
                continue
        elif view_option.upper() == "P":
            if len(temp_game_list) == 0:
                print("Collection is empty. Try again")
            else:
                game_name = input("Enter name of the game you wish to play (leave blank to go back): ")
                if game_name == "":
                    continue
                elif game_name in temp_game_list:
                    # check if the game is in this collection...
                    play_game(game_name)
                else:
                    print("No such game in collection...")
        elif view_option.upper() == "R":
            if len(temp_game_list) == 0:
                print("Collection is empty. Try again")
            else:
                temp_int = random.randint(0, len(temp_game_list)-1)
                # from 0 to end of list containing all games in the collection
                print("Random game chosen is '" + temp_game_list[temp_int] + "'")
                play_game(temp_game_list[temp_int])


def add_to_collection(collection_name, game_name):
    # sql statement to add game to collection
    print("stub game added")
    return


def delete_from_collection(collection_name, game_name):
    # sql statement to remove game from collection
    print("stub game removed")
    return


def rename_collection(name):
    newname = input("Enter new name for collection: '" + name + "' : ")
    # sql statement to update collection name
    return


def delete_collection(name):
    # sql statement to delete collection
    # potentially add error processing in case collection name does not exist or mistyped?
    return


def videogames_processing(user_id):
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
                play_game(game_name)
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


def play_game(name):
    while True:
        print("Starting the game '" + name + "'")
        temp = input("(E)xit to leave the game.. \n")
        if temp.upper() == "E":
            break
    return


def user_processing(user_id):
    while True:
        user_option = input("(S)earch by email | (F)ollow list | (B)ack \n")
        if user_option.upper() == "B":
            break
        elif user_option.upper() == "F":
            follow_list(user_id)
        elif user_option.upper() == "S":
            email = input("Enter email to search for (leave blank to go back): ")
            search_users(email)
    return


def follow_list(user_id):
    while True:
        temp_username_list = []
        # sql statement to show all the users followed
        opt = input("(B)ack | (U)nfollow")
        if opt.upper() == "B":
            break
        elif opt.upper() == "U":
            username = input("Enter the user to unfollow (leave blank to go back): ")
            if username == "":
                continue
            elif username.upper in temp_username_list:
                unfollow_user(username)
            else:
                print("User not found")
                continue
    return


def unfollow_user(username):
    # sql statement to unfollow username
    return


def search_users(email):
    while True:
        # sql command to search for user by email
        username = "temp"
        # sql command to check if the user is already followed
        opt = input("(F)ollow | (U)nfollow | (B)ack \n")
        if opt.upper() == "B":
            break
        elif opt.upper() == "F":
            follow_user(username)
        elif opt.upper() == "U":
            unfollow_user(username)
        else:
            print("Unknown command. Try again")
            continue
    return


def follow_user(username):
    # sql statement to follow username
    return


def start_ui():
    # add user_id as the second value for the return of login...?
    logged_in, user_id = login()
    while logged_in:
        print("Main menu")
        menu_option = input("(C)ollections | (V)ideogames | (U)ser | (Q)uit \n")
        if menu_option.upper() == "C":
            collection_processing(user_id)
        elif menu_option.upper() == "V":
            videogames_processing(user_id)
        elif menu_option.upper() == "U":
            user_processing(user_id)
        elif menu_option.upper() == "Q":
            print("Logging out!")
            break
        else:
            print("Unknown command.. Try again")


if __name__ == '__main__':
    while True:
        start_ui()
