import asyncore

from carpu.log import logger
from carpu.playlist import Playlist
from carpu.events import PlayNextSongEvent
from carpu.player import Player
from carpu.server import Server


if __name__ == '__main__':
    server = Server()

    playlist = Playlist(server, '/home/nick.garanko/Music/')

    player = Player(server, ['-really-quiet', '-msglevel', 'global=6'])

    server.fire(PlayNextSongEvent(None))

    logger.debug('Starting the loop.')
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        print('Bye.')
