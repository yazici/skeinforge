"""
This page is in the table of contents.
Winding is a script to set the winding profile for the skeinforge chain.

The displayed craft sequence is the sequence in which the tools craft the model and export the output.

On the winding dialog, clicking the 'Add Profile' button will duplicate the selected profile and give it the name in the input field.  For example, if laser is selected and the name laser_10mm is in the input field, clicking the 'Add Profile' button will duplicate laser and save it as laser_10mm.  The 'Delete Profile' button deletes the selected profile.

The profile selection is the setting.  If you hit 'Save and Close' the selection will be saved, if you hit 'Cancel' the selection will not be saved.  However; adding and deleting a profile is a permanent action, for example 'Cancel' will not bring back any deleted profiles.

To change the winding profile, in a shell in the profile_plugins folder type:
> python winding.py

An example of using winding from the python interpreter follows below.


> python
Python 2.5.1 (r251:54863, Sep 22 2007, 01:43:31)
[GCC 4.2.1 (SUSE Linux)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import winding
>>> winding.main()
This brings up the winding setting dialog.

"""


from __future__ import absolute_import
import __init__
from skeinforge_tools.skeinforge_utilities import settings
import sys


__author__ = "Enrique Perez (perez_enrique@yahoo.com)"
__date__ = "$Date: 2008/21/04 $"
__license__ = "GPL 3.0"


def getCraftSequence():
	"Get the winding craft sequence."
	return 'cleave,preface,coil,flow,feed,home,lash,fillet,dimension,unpause,export'.split( ',' )

def getNewRepository():
	"Get the repository constructor."
	return WindingRepository()


class WindingRepository:
	"A class to handle the winding settings."
	def __init__( self ):
		"Set the default settings, execute title & settings fileName."
		settings.addListsSetCraftProfileArchive( getCraftSequence(), 'free_wire', self, 'skeinforge_tools.profile_plugins.winding.html' )


def main():
	"Display the export dialog."
	if len( sys.argv ) > 1:
		writeOutput( ' '.join( sys.argv[ 1 : ] ) )
	else:
		settings.startMainLoopFromConstructor( getNewRepository() )

if __name__ == "__main__":
	main()
