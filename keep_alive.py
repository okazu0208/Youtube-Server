from flask import Flask
from threading import Thread
from pytube import YouTube
from io import BytesIO
import base64

app = Flask('')

@app.route('/')
def home():
    yt = YouTube('https://www.youtube.com/watch?v=aXE4aMjbfww')
    stream = yt.streams.first()
    buffer=BytesIO()
    stream.stream_to_buffer(buffer)
    buffer.seek(0)
    base64.b64encode(buffer.read()).decode()
    return "I'm alive"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
