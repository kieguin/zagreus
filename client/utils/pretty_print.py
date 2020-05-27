from utils.colours import bcolors as colors

def prettyPrint(color, message):
    if(color == 'info'):
        print(colors.HEADER + '[ > ] ' + message + colors.ENDC)
    elif(color == 'error'):
        print(colors.FAIL + '[ ✘ ] ' + message + colors.ENDC)
    elif(color == 'success'):
        print(colors.OKGREEN + '[ ✓ ] ' + message + colors.ENDC)
    elif(color == 'stack'):
        print(colors.WARNING + '[ - ] ' + message + colors.ENDC)