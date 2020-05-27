import sys
from utils.pretty_print import prettyPrint

def closeBrowserAndExit(self):
    prettyPrint('stack', 'Exiting Zagreus, Goodbye master!')
    self.browser.close()
    sys.exit()