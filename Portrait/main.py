import sys

try:
    from IPython.terminal.embed import InteractiveShellEmbed
    from IPython.terminal.prompts import Prompts, Token
except ImportError:
    sys.exit('Cannot import from ipython: Do `pip3 install ipython` to install')

import cozmo
from portrait import Portrait

usage = ('This is an IPython interactive shell for Cozmo.\n'
         'All commands are executed within cozmo\'s running program loop.\n'
         'Use the [tab] key to auto-complete commands, and see all available methods.\n'
         'All IPython commands work as usual. See below for some useful syntax:\n'
         '  ?         -> Introduction and overview of IPython\'s features.\n'
         '  object?   -> Details about \'object\'.\n'
         '  object??  -> More detailed, verbose information about \'object\'.')

# Creating IPython's history database on the main thread
ipyshell = InteractiveShellEmbed(banner1='\nWelcome to the Cozmo Shell',
                                 exit_msg='Goodbye\n')

p: Portrait = None

def test():
    p.ready()

def cozmo_program(robot: cozmo.robot.Robot):
    global p
    p = Portrait(robot)
    '''Invoke the ipython shell while connected to cozmo'''
    default_log_level = cozmo.logger.level
    cozmo.logger.setLevel('WARN')
    ipyshell(usage)
    cozmo.logger.setLevel(default_log_level)


cozmo.run_program(cozmo_program, use_3d_viewer=True, use_viewer=True)