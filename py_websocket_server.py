import eventlet
import socketio
from py_config import ConfigFactory
from py_logging import LoggerFactory


class WebSocketServer():
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger

    def start(self):
        sio = socketio.Server(cors_allowed_origins='*')
        app = socketio.WSGIApp(sio)

        @sio.event
        def connect(sid, environ):
            print('connect ', sid)

        @sio.on('toServer')
        def my_message(sid, data):
            print('sid=', sid)
            ('toServer=%s' % data)

        @sio.event
        def disconnect(sid):
            print('disconnect ', sid)

        eventlet.wsgi.server(eventlet.listen(('', 8801)), app)


if __name__ == '__main__':
    config = ConfigFactory('py_lab.ini').getConfig()
    logger = LoggerFactory(config=config).getLogger()
    server = WebSocketServer(config=config, logger=logger)
    server.start()
