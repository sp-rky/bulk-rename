try:
    import os

    # variables used later in the script
    nameSuffix = 0
    # structure: {file location: containing folder of file}
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

    def getSurfaceFiles(location, doFolders):
        files = {}
        for file in os.listdir(fileDirectory):
            # check to see if the file is a folder
            if os.path.splitext(file)[1] != '' and not doFolders:
                # add the entry to the fileDict dictionary
                files[location + '\\' + file] = fileDirectory
            if doFolders:
                # see above comment
                files[location + '\\' + file] = fileDirectory
        return files

    # get required input from the user
    fileDirectory = input('Where are the files? ')

    # rename folders as well as files?
    doRenameFolders = True if input('Would you like to rename all files? (y/n) ').lower()[0] == 'y' else False

    # do we need to go through all the subdirectories?
    doSubDir = True if input('Would you like to rename all subdirectories? (y/n) ').lower()[0] == 'y' else False

    # if yes then use the getAllFiles() function
    if doSubDir:
        fileDict = getAllFiles(fileDirectory, doRenameFolders)

    # otherwise just use the getSurfaceFiles() function
    else:
        fileDict = getSurfaceFiles(fileDirectory, doRenameFolders)

    # get the naming prefix from the user
    namePrefix = input('What would you like the naming prefix to be? ')
    print()

    # sort folders by how deep they are in the file system in order to prevent renaming of holding folders
    # fuck yes this is janky as shit but its fastish and it works
    sortedFiles = {}
    originalSize = len(fileDict)
    while(len(sortedFiles) != originalSize):
        maxKey = ''
        for file in fileDict:
            # if the file is the deepest in the file system
            if len(maxKey.split('\\')) < len(file.split('\\')):
                maxKey, maxVal = file, fileDict[file]
        sortedFiles[maxKey] = maxVal
        fileDict.pop(maxKey)

    # loop through every file to be renamed
    for file in sortedFiles:
        # get the file extension to be used in the next line
        fileExtension = os.path.splitext(file)[1]
        # set the name
        name = sortedFiles[file] + '\\' + namePrefix + str(nameSuffix) + fileExtension
        # rename the file/folder
        os.rename(file, name)
        # increment nameSuffix by 1 so all names are unique
        nameSuffix += 1
        print(f'Renamed \"{file}\" to \"{name}\"')

    # alert the user that the program is finished
    print(f'\nRenamed {nameSuffix} file(s).')
    print('Press the any key to exit...', end='', flush=True)
    os.system('PAUSE >nul')
except Exception as e:
    print('Error:')
    print(e)
    input('Press enter to exit...')
