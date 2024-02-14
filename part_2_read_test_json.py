import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    ### Begin Add Code Here ###
    gameList = json_data["games"]
    for game in gameList:
        title = game["title"]
        year = game["Year"]
        platform = game["platform"]

        gamePlatform = test_data.Platform(platform["name"], platform["launch year"])
        newGame = test_data.Game(title, gamePlatform, year)
        game_library.add_game(newGame)
    ### End Add Code Here ###

    return game_library


#Part 2
input_json_file = "data/test_data.json"

### Begin Add Code Here ###
#Open the file specified by input_json_file
with open(input_json_file, "r") as reader:
    json_data = json.load(reader)   #Use the json module to load the data from the file
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
game_library = make_game_library_from_json(json_data)
#Print out the resulting GameLibrary data using print()
print(game_library)
### End Add Code Here ###
