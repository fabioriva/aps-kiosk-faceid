import os
import re
from flask import Flask, Response, render_template, send_from_directory
from camera_pi2 import Camera

app = Flask(__name__)


@app.route("/")
def index():
    """Video streaming home page."""
    return render_template('faceid.html')
    # return render_template('video.html', filename='test.mp4')


def gen(camera):
    """Video streaming generator function."""
    yield b'--frame\r\n'
    while True:
        frame = camera.get_frame()
        yield b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n--frame\r\n'


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/video/<filename>")
def serve_video(filename):
    return send_from_directory('static/media', filename)
    # return render_template('video.html', filename=filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
