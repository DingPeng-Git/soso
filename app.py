#程序主入口
from flask import Flask

app=Flask(__name__)

app.debug=True
app.secret_key='sjehfjeefrjewth43u'  #设置session加密
app.config['JSON_AS_ASCII']=False  #指定json编码格式 如果为False 就不使用ascii编码，
app.config['JSONIFY_MIMETYPE'] ="application/json;charset=utf-8" #指定浏览器渲染的文件类型，和解码格式；


from user import index
from user import login
from user import vs_detail

#把文件中蓝图对象注册到app里
app.register_blueprint(index.index_blue)
app.register_blueprint(login.login_blue)
app.register_blueprint(vs_detail.vs_detail_blue)

if __name__ == '__main__':
    print(app.url_map)
    app.run(host = '0.0.0.0',port = '2334')