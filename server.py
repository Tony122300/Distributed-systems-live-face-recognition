import eventlet
from app import app
import socketio

sio = socketio.Server(async_mode='threading')
appServer = socketio.WSGIApp(sio, app)
thread_pool = eventlet.GreenPool(6)

@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.event
def my_message(sid, data):
    print('message ', data)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), appServer, custom_pool=thread_pool)