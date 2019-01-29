#登录界面
from flask import Flask, render_template, request, redirect,Blueprint,session
from wtforms import Form
from wtforms.fields import core
from wtforms.fields import html5
from wtforms.fields import simple
from wtforms import validators
from wtforms import widgets


class LoginForm(Form):

    #不同的字段 内部包含正则表达式 html5.EmailField | html5.DateTimeField...
    name=simple.StringField(
        label='用户名',
        validators=[                                #验证规则和错误提示信息
            validators.DataRequired(message='用户名不能为空.'),
            validators.Length(min=6, max=18, message='用户名长度必须大于%(min)d且小于%(max)d')
        ],
        widget=widgets.TextInput(),                 #前端页面显示的插件.TextArea
        render_kw={'class': 'form-control'}      #设置form标签的class信息

        )

    # 不同的字段 内部包含正则表达式  html5.EmailField | html5.DateTimeField...
    pwd = simple.PasswordField(
        label='密码',
        validators=[
            validators.DataRequired(message='密码不能为空.'),
            validators.Length(min=8, message='用户名长度必须大于%(min)d'),
            #自定义验证规则
            validators.Regexp(regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}",
                              message='密码至少8个字符，至少1个大写字母，1个小写字母，1个数字和1个特殊字符')

        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control'}
    )

login_blue = Blueprint('login',__name__,template_folder='user_templates')
@login_blue.route('/user/login/')
def login():
    print('hahah',request.method)
    if request.method == 'GET':
        form = LoginForm()     #实例化 form验证类
        return render_template('login.html', form=form)
    else:
        form = LoginForm(formdata=request.form)
        if form.validate(): #判断是否验证成功？
            print('用户提交数据通过格式验证，提交的值为：', form.data)
            session['user'] = form.data['name']
            return redirect('index')
        else:
            print(form.errors)
        return render_template('login.html', form=form)
    # return 'hello'