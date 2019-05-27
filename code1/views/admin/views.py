from flask import render_template, redirect
from sqlalchemy.orm import sessionmaker
from models.models import engine, User
# 引入蓝图
from . import admin_blu

print(1111111111111111111)


# 使用蓝图添加路由
@admin_blu.route('/')
def index1():
    # 访问 / 就重定向到index.html
    return redirect('index.html')


@admin_blu.route('/index.html')
def index2():
    # 创建session对象
    # DBSession = sessionmaker(bind=engine)  # 创建与数据库的会话，返回的是一个类
    # session = DBSession()  # 生成会话对象
    # 查询user表中所有的用户数据
    # all_user_info = session.query(User).all()
    # print(all_user_info)
    # 关闭session
    # session.close()
    return render_template('admin/index.html')


@admin_blu.route('/tables.html')
def tables():
    """显示用户信息的页面"""
    # 创建session对象
    DBSession = sessionmaker(bind=engine)  # 创建与数据库的会话，返回的是一个类
    session = DBSession()  # 生成会话对象
    # 查询user表中所有的用户数据
    all_user_info = session.query(User).all()
    # print(all_user_info)
    # 关闭session
    session.close()
    return render_template('admin/tables.html', user_infos=all_user_info)


@admin_blu.route('/testfilter.html')
def testfilter():
    """显示用户信息的页面"""
    var1 = '<em>hello</em>'
    var2 = 'hEllo world hehe'
    return render_template('admin/testfilter.html', var1=var1, var2=var2)


class Student():
    def __init__(self, name):
        self.name = name


@admin_blu.route('/control.html')
def testcontrol():
    """显示用户信息的页面"""
    # stu = Student('小明')
    stu = None
    stu1 = Student('小红')
    stu2 = Student('小明')
    stu3 = Student('小绿')
    stu4 = Student(None)
    stus = [stu1, stu2, stu3, stu4]

    return render_template('admin/control.html', stu=stu, stus=stus)
