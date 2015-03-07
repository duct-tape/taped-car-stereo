class BaseEvent(object):
    """
    Generic event class
    """
    def __init__(self, value):
        self.value = value

    def __unicode__(self):
        return "<{}: '{}'>".format(self.__class__, self.value)


class PlayNextSongEvent(BaseEvent):
    """
    Play Next Song
    """
    pass


class GetNextSongEvent(BaseEvent):
    """
    Get next song to play
    """
    pass


class UpdateMetadataEvent(BaseEvent):
    """
    Update metadata event
    """
    pass
