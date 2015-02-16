import sys
import nuke

print 'Loading Lab Tools...'
menubar = nuke.menu("Nuke")

def getRead():
	try:
		firstFrame = int(nuke.knob('root.first_frame'))
		lastFrame =  int(nuke.knob('root.last_frame'))
		myValue = nuke.selectedNode().knob('file').getValue()
		myRead = nuke.createNode('Read')
		myRead.knob('file').setValue(myValue)
		myRead.knob('first').setValue(firstFrame)
		myRead.knob('last').setValue(lastFrame)
	except:
		print 'select the write node'
 
# Custom Lab Tools
toolbar = nuke.toolbar("Nodes")
m = toolbar.addMenu("crussell", icon="ICON NAME HERE.png")
#m=menubar.addMenu("readWrite")
m.addCommand("readWrite", 'getRead()', "ctrl+r", icon="IconName",index=1)
m.addCommand("FML", "nuke.createNode(\"FML\")", icon="IMAGE NAME HERE.png")