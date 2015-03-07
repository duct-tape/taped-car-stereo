import os
from random import randint

from carpu.log import logger
from carpu.events import GetNextSongEvent
from carpu.events import PlayNextSongEvent


class Playlist(object):
    """
    Playlist implementation
    """

    def __init__(self, server, directory=None):
        """
        Init player server
        """
        self.server = server
        assert directory is not None, "Please specify working directory"
        self.library = directory
        self.index = -1
        self.random_excempt = []

        self.init_playlist()
        self.server.subscribe(self)

    def init_playlist(self):
        """
        Initialize playlist
        """
        self.playlist = []
        for root, dirs, files in os.walk(self.library):
            self.playlist = [os.path.join(self.library, f) for f in files]

    def get_next(self, random=True):
        """
        Get next file in playlist
        """
        if random:
            index = randint(0, len(self.playlist))
        else:
            index = self.index + 1

        if index == len(self.playlist):
            index = -1

        return self.playlist[index]

    def handle_event(self, event):
        """
        Handle event from server
        """
        if isinstance(event, GetNextSongEvent):
            next = self.get_next()
            logger.debug('Next: {}'.format(next))
            self.server.fire(PlayNextSongEvent(next))
