# aps-kiosk-faceid 😉

Raspberry pi4 os Debian GNU/Linux 12 (bookworm)

Using picamera2 in virtual environments
```
python3 -m venv --system-site-packages .venv

pip install flask
pip install python-dotenv
pip install opencv-python
pip install deepface
pip install tf-keras
pip install gunicorn

pm2 --name=faceid start "gunicorn app:app -b localhost:5000 --workers 1 --threads 4"

```
Thank you https://github.com/serengil 🤗
