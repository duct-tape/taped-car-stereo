import pifacecad

from carpu.events import GetNextSongEvent
from carpu.events import VolumeUPEvent
from carpu.events import VolumeDOWNEvent

class Face(object):
    def __init__(self, server):
        self.events = server
        self.cad = pifacecad.PiFaceCAD() 
        
        self.cad.lcd.set_cursor(3, 0)
        self.cad.lcd.write("started")
        
        self.cad.lcd.blink_off()
        self.cad.lcd.backlight_on()

        self.switchlistener = pifacecad.SwitchEventListener(chip=self.cad) 
        for x in range(8):
            self.switchlistener.register(x, pifacecad.IODIR_ON, self.test)
        self.switchlistener.activate()


    def stop(self):
        self.switchlistener.deactivate()

    def test(self, event):

        if event.pin_num == 0:
            self.events.fire(GetNextSongEvent(None))
        elif event.pin_num == 1:
            print("Pause")

        elif event.pin_num == 6:
            self.events.fire(VolumeDOWNEvent(None))
        elif event.pin_num == 7:
            self.events.fire(VolumeUPEvent(None))

        print(repr(event.pin_num))
