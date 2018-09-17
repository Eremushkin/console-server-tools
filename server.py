class ServerConnection(object):
    def __init__(self, alias=None, host='localhost'):
        self.host = host
        self.alias = alias


def get_connection(host, password):
    return ServerConnection(host)


def ping(server_connection):
    return True
