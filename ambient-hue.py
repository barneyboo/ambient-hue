"""
ambient hue
(c) luke hutton 2017
"""
import objc
objc.loadBundle('CoreWLAN',
       bundle_path='/System/Library/Frameworks/CoreWLAN.framework',
       module_globals=globals())

rooms = {}

if __name__ == "__main__":
    for iname in CWInterface.interfaceNames():
        interface = CWInterface.interfaceWithName_(iname)
        rssi = interface.rssi()
        break

    print "ambient hue"
    print "-----------"
    print
    print "Move to the first room you want to be able to control, then hit ENTER to start calibration. This only takes a few seconds per room."
