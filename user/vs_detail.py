from flask import Blueprint,render_template,Response,send_from_directory
from time import time


vs_detail_blue = Blueprint('vs_detail1',__name__,template_folder='user_templates')

@vs_detail_blue.route('/user/vs_detail/')
def vs_detail1():
    return render_template('video_detail.html')

@vs_detail_blue.route('/user/video_test/',endpoint='video_test')
def test():
  # flask.send_file()
  return send_from_directory('user/user_static/', '123.avi', as_attachment=True)


def gen(camera):
  while True:
    frame = camera.get_frame()
    print('laji',frame)
    yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
  
@vs_detail_blue.route('/user/video_feed/',endpoint='video_feed')
def video_feed():
    print('视屏过来了')
    return Response(gen(Camera()),mimetype='multipart/x-mixed-replace; boundary=frame')

class Camera(object):
  def __init__(self):
    self.frames = [open('./user/user_static/' + f + '.jpg', 'rb').read() for f in ['1', '2', '3']]
  
  def get_frame(self):
    return self.frames[int(time()) % 3]