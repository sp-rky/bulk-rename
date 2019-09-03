import os

# variables used later in the script
nameSuffix = 0
fileDict = {}

# function to get all files from all subdirectories
def getAllFiles(location):
    files = {}
    # go through every folder in the specified directory
    # r = location, d = directory, f = file
    for r, d, f in os.walk(location):
        for file in f:
            # add the entry to the fileDict dictionary
            files[os.path.join(r, file)] = r
    return files

# get required input from the user
fileDirectory = input('Where are the files? ')

# do we need to go through all the subdirectories?
doSubDir = input('Would you like to rename all subdirectories?(y/n) ')

# if yes then use the getAllFiles() function
if doSubDir.lower()[0] == 'y':
    fileDict = getAllFiles(fileDirectory)

# otherwise just use the listdir() function
else:
    for file in os.listdir(fileDirectory):
        if os.path.splitext(file)[1] != '':
            # add the entry to the fileDict dictionary
            # stored like this: {file location: containing folder of file}
            fileDict[fileDirectory + '\\' + file] = fileDirectory

# get the naming prefix from the user
namePrefix = input('What would you like the naming prefix to be? ')

# loop through every file to be renamed
for file in fileDict:
    # get the file extension to be used in the next line
    fileExtension = os.path.splitext(file)[1]
    # set the name
    name = fileDict[file] + '\\' + namePrefix + str(nameSuffix) + fileExtension
    # rename the file
    os.rename(file, name)
    print(f'Renamed \"{file}\" to \"{name}\"')
    # increment nameSuffix by 1 so all names are unique
    nameSuffix += 1

# alert the user that the program is finished
print(f'Renamed {nameSuffix} file(s).')
input('Press the enter key to exit...')
