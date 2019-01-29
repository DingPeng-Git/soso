#主界面
from flask import Blueprint,render_template,session

index_blue = Blueprint('index',__name__,template_folder='user_templates')

@index_blue.route('/user/index/')
def index():
    info = '这是传送的数据'
    name = session.get('user')
    t=''
    if name:
        t=name
    list1 = {'info':info,'name':t}
    return render_template('index.html',list1=list1)

@index_blue.route('/index1')
def index1():
    return 'hello'