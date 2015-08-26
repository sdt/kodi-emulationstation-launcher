import os
import xbmcaddon

__addon__ = xbmcaddon.Addon()
program = __addon__.getSetting('emulationstation_path')
os.execlp(program, program)
