from dotenv import load_dotenv
from flask import Flask, Response, request, send_from_directory
from camera_pi2 import Camera
# from faceid import build_demography_models, build_facial_recognition_model

load_dotenv()

app = Flask(__name__)


# @app.route("/")
# def index():
#     """Video streaming home page."""
#     return render_template('faceid.html')

def gen(camera):
    """Video streaming generator function."""
    yield b'--frame\r\n'
    while True:
        frame = camera.get_frame()
        yield b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n--frame\r\n'


@app.route('/face/<mode>')
def face(mode=0):
    print(request)
    name = request.args.get('name')
    surname = request.args.get('surname')
    print(f"param1: {name}, param2: {surname}")
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera(mode)), mimetype='multipart/x-mixed-replace; boundary=frame')


# @app.route('/video_feed')
# def video_feed():
#     """Video streaming route. Put this in the src attribute of an img tag."""
#     return Response(gen(Camera()), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/video/<filename>")
def serve_video(filename):
    return send_from_directory('static/media', filename)
    # return render_template('video.html', filename=filename)


if __name__ == '__main__':
    # initialize models
    # build_demography_models(enable_face_analysis=False)
    # build_facial_recognition_model(model_name="VGG-Face")
    app.run(host='0.0.0.0', threaded=True)
