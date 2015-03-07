from mplayer.async import AsyncPlayer

from carpu.log import logger
from carpu.events import PlayNextSongEvent
from carpu.events import GetNextSongEvent
from carpu.events import UpdateMetadataEvent


class Player(AsyncPlayer):
    """
    A bit extended AsyncPlayer
    """

    def __init__(self, server, *args, **kwargs):
        """
        Create AsyncPlayer and set initial args
        """
        self.events = server

        super(Player, self).__init__(*args, **kwargs)

        self.events.subscribe(self)

        self._stdout.connect(self.stdout_handler)
        self._stderr.connect(self.stderr_handler)

    def stdout_handler(self, data):
        """
        Handle mplayer stdout
        """
        logger.debug("Stdout: {}".format(data))
        if data.startswith("EOF code"):
            self.events.fire(GetNextSongEvent(None))

    def stderr_handler(self, data):
        """
        Handle mplayer stderr
        """
        logger.error("Stderr: {}".format(data))

    def handle_event(self, event):
        """
        Handle server event
        """
        if isinstance(event, PlayNextSongEvent):
            if event.value is None:
                self.events.fire(GetNextSongEvent(None))
            else:
                logger.debug("Loading: {}".format(event.value))
                self.loadfile(event.value)
                self.events.fire(UpdateMetadataEvent(self.metadata or {}))
