import cc_dat_utils
import json

#Part 3
#Load your custom JSON file
inputFile = "data/levels.json"
outputFile = "data/levels.dat"

levelPack = cc_dat_utils.cc_classes.CCLevelPack()

"""
from cc_classes.py: create
CCLevelPack and add those levels:
    CCLevel with:
        CCMapTitleField, CCEncodedPasswordField, CCMapHintField,
        CCMonsterMovementField & CCCoordinate
"""

with open(inputFile, "r") as reader:
    jsonData = json.load(reader)
    levels = jsonData["levels"]
    for lev in levels:
        ccLevel = cc_dat_utils.cc_classes.CCLevel()
        ccLevel.level_number = lev["number"]
        ccLevel.time = lev["time"]
        ccLevel.num_chips = lev["chips"]
        ccLevel.upper_layer = lev["upper layer"]

        fields = lev["fields"]
        for key in fields:  #loop through field dictionary via keys
            value = fields[key]

            if (key == "3"):
                ccField = cc_dat_utils.cc_classes.CCMapTitleField(value)
            elif (key == "6"):
                ccField = cc_dat_utils.cc_classes.CCEncodedPasswordField(value)
            elif (key == "7"):
                ccField = cc_dat_utils.cc_classes.CCMapHintField(value)
            elif (key == "10"):
                ccCoordList = []
                for i in range(0, len(value), 2):
                    x = value[i]
                    y = value[i+1]
                    coord = cc_dat_utils.cc_classes.CCCoordinate(x, y)
                    ccCoordList.append(coord)
                ccField = cc_dat_utils.cc_classes.CCMonsterMovementField(ccCoordList)
                #couldve updated the upper layer with the type of monster instead of preloaded

            ccLevel.add_field(ccField)

        #Convert JSON data to CCLevelPack
        levelPack.add_level(ccLevel)

#Save data to DAT file from cc_dat_utils.py: write_cc_level_pack_to_dat
cc_dat_utils.write_cc_level_pack_to_dat(levelPack, outputFile)
