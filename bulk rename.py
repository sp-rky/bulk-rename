import os

# variables used later in the script
nameSuffix = 0
fileDict = {}

# function to get all files from all subdirectories
def getAllFiles(location, doFolders):
    files = {}
    # go through every subdirectory in the specified directory
    # r = location, d = directory, f = file
    for r, d, f in os.walk(location):
        for file in f:
            # add the entry to the fileDict dictionary
            files[os.path.join(r, file)] = r
        if doFolders:
            for folder in d:
                files[os.path.join(r, folder)] = r
    return files

# get required input from the user
fileDirectory = input('Where are the files? ')

# rename folders as well as files?
doRenameFolders = input('Would you like to rename all files?(y/n) ')

# do we need to go through all the subdirectories?
doSubDir = input('Would you like to rename all subdirectories?(y/n) ')

# if yes then use the getAllFiles() function
if doSubDir.lower()[0] == 'y':
    if doRenameFolders.lower()[0] == 'n':
        fileDict = getAllFiles(fileDirectory, False)
    else:
        fileDict = getAllFiles(fileDirectory, True)

# otherwise just use the listdir() function
else:
    for file in os.listdir(fileDirectory):
        # check to see if the file is a folder
        if os.path.splitext(file)[1] != '' and doRenameFolders.lower()[0] == 'n':
            # add the entry to the fileDict dictionary
            # stored like this: {file location: containing folder of file}
            fileDict[fileDirectory + '\\' + file] = fileDirectory
        else:
            # see above comment
            fileDict[fileDirectory + '\\' + file] = fileDirectory

# get the naming prefix from the user
namePrefix = input('What would you like the naming prefix to be? ')

print()

# loop through every file to be renamed
for file in fileDict:
    # get the file extension to be used in the next line
    fileExtension = os.path.splitext(file)[1]
    # set the name
    name = fileDict[file] + '\\' + namePrefix + str(nameSuffix) + fileExtension
    # rename the file if it is just a file
    if fileExtension != '':
        os.rename(file, name)
        # increment nameSuffix by 1 so all names are unique
        nameSuffix += 1
        print(f'Renamed \"{file}\" to \"{name}\"')

for file in fileDict:
    # get the file extension to be used in the next line
    fileExtension = os.path.splitext(file)[1]
    # set the name
    name = fileDict[file] + '\\' + namePrefix + str(nameSuffix) + fileExtension
    # rename the file if it is a folder
    if fileExtension == '':
        os.rename(file, name)
        # increment nameSuffix by 1 so all names are unique
        nameSuffix += 1
        print(f'Renamed \"{file}\" to \"{name}\"')

# alert the user that the program is finished
print(f'\nRenamed {nameSuffix} file(s).')
input('Press the enter key to exit...')
