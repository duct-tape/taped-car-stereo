import pifacecad
import asyncore
from mplayer.async import AsyncPlayer


def handle_data(data):
    if not data.startswith('EOF code'):
        print('log: %s' % (data, ))
    else:
        player.quit()


def init_player():
    # Don't autospawn because we want to setup the args later
    player = AsyncPlayer(autospawn=False)

    # Setup additional args
    player.args = ['-really-quiet', '-msglevel', 'global=6']

    # hook a subscriber to MPlayer's stdout
    player.stdout.hook(handle_data)

    # Manually spawn the MPlayer process
    player.spawn()

    # play a file
    player.loadfile('/home/pi/y.mp3')

    metadata = player.metadata or {}
    cad = init_cad()
    cad.lcd.write('P: {name}'.format(name=metadata.get('Title', '')))

    listener = pifacecad.SwitchEventListener(chip=cad)

    def play_next(event):
        print(str(event.pin_num))
        player.loadfile('/home/pi/c.mp3')

    # for i in range(8):
    listener.register(0, pifacecad.IODIR_FALLING_EDGE, play_next)

    listener.activate()

    # run the asyncore event loop
    asyncore.loop()


def init_cad():
    cad = pifacecad.PiFaceCAD()
    return cad


if __name__ == '__main__':
    init_player()
