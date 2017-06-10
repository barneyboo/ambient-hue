"""
ambient hue
(c) luke hutton 2017
"""

import numpy
import objc
import phue
import time


objc.loadBundle('CoreWLAN',
       bundle_path='/System/Library/Frameworks/CoreWLAN.framework',
       module_globals=globals())

rooms = {}

if __name__ == "__main__":
    b = phue.Bridge(BRIDGE_IP)
    b.get_api()
    lights = b.get_light_objects('id')

    interface = None
    for iname in CWInterface.interfaceNames():
        interface = CWInterface.interfaceWithName_(iname)
        rssi = interface.rssi()
        break

    print "ambient hue"
    print "-----------"
    print
    rooms = []
    name = raw_input('Type a name for the first room you want to be able to control, then hit ENTER to start calibration. This only takes a few seconds per room.')  # noqa
    measures = []
    while(True):
        measures.append(interface.rssi())
        time.sleep(0.5)
        if(len(measures) > 10):
            break
    new_room = {'rssi':measures,'name':name}
    rooms.append(new_room)

    while(True):
        name = raw_input("Type a name for the next room you want to be able to control, then hit ENTER. Enter a blank name if you're done.")
        if len(name) == 0:
            break
        measures = []
        while(True):
            measures.append(interface.rssi())
            time.sleep(0.5)
            if(len(measures) > 10):
                break
        new_room = {'rssi':measures,'name':name}
        rooms.append(new_room)

    print "Thanks! Here are the rooms you've captured:"
    for room in rooms:
        print "%s (%s dBm)" % (room['name'], numpy.mean(room['rssi']))
