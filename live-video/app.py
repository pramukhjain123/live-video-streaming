from flask import Flask, render_template, Response
import requests

app = Flask(__name__)

ESP32_CAM_URL = "ip goes here"

@app.route('/')
def index():
    return render_template('index.html')

def generate():
    while True:
        img_resp = requests.get(f"{ESP32_CAM_URL}/capture")
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + img_resp.content + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
#created by pramukh rajendra jain
