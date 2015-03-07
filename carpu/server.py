from carpu.log import logger


class Server(object):
    """
    Generic event handling server
    """
    def __init__(self):
        """
        Init server
        """
        self.listeners = list()

    def subscribe(self, listener):
        """
        Subscribe for certain events
        """
        if listener in self.listeners:
            raise AttributeError("Listener {} already registered.".format(
                listener))

        self.listeners.append(listener)

    def fire(self, event):
        """
        Fire event
        """
        logger.debug("Event: {}".format(event))
        for listener in self.listeners:
            listener.handle_event(event)
