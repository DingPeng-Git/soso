# from flask import Flask

# app=Flask(__name__,template_folder='templates',static_url_path='/static/')

# app.debug=True
# app.secret_key='sjehfjeefrjewth43u'  #设置session加密
# app.config['JSON_AS_ASCII']=False  #指定json编码格式 如果为False 就不使用ascii编码，
# app.config['JSONIFY_MIMETYPE'] ="application/json;charset=utf-8" #指定浏览器渲染的文件类型，和解码格式；


# from .views.user import index,login,vs_detail
# # from .views import index

# #把文件中蓝图对象注册到app里
# # app.register_blueprint(login.login,url_prefix='/login') #访问login蓝图必须以url_prefix开头
# app.register_blueprint(index.index_blue,url_prefix='/user')
# # app.register_blueprint(index.index,url_,url_prefix='/')

# app.register_blueprint(login.login)
# app.register_blueprint(vs_detail.vs_detail)
# # app.register_blueprint(vs_detail.vs_detail)

# if __name__ == '__main__':
#     app.run()
