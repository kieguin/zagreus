from utils.colours import bcolors as colors

def prettyPrint(type, message):

    if (type == 'info'):
        print(colors.HEADER + '[ > ] ' + message + colors.ENDC)

    elif (type == 'success'):
        print(colors.OKGREEN + '[ ✓ ] ' + message + colors.ENDC)

    elif (type == 'error'):
        print(colors.FAIL + '[ ✘ ] ' + message + colors.ENDC)

    elif (type == 'warning'):
        print(colors.WARNING + '[ ⚠ ] ' + message + colors.ENDC)