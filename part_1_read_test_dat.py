import cc_dat_utils

#Part 1
input_dat_file = "data/pfgd_test.dat"
outFile = "data/pfgd_test.txt"

#Use cc_dat_utils.make_cc_level_pack_from_dat() to load the file specified by input_dat_file
data = cc_dat_utils.make_cc_level_pack_from_dat(input_dat_file)
#print the resulting data
print(data) #I feel like this line is redundant if we're writing directly to a text file anyways
dataString = data.__str__() #for writing compatability
#write to a file in the pipeline because copy pasting is annoying
with open(outFile, 'w') as writer: # based on "write_cc_level_pack_to_dat" fxn
    writer.write(dataString)