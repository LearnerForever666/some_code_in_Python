# This system is designed to manage some information of students
"""
author:LearnerForever
Date:2021 Sep 29th
"""


def menu1():
    """用于打印初始页面的菜单"""
    print('*' * 30)
    print('1.增加学生信息', '2.删除学生信息')
    print('3.修改学生信息', '4.查询单个学生信息')
    print('5.查询所有学生信息', '0.退出')
    print('*' * 30)


def menu2():
    """用于打印修改学生信息菜单"""
    print('*' * 30)
    print('1.姓名', '2.班级')
    print('3.性别', '4.住址')
    print('5.电话', '0.退出')
    print('*' * 30)


def infoadd(inform):
    """用于增加学生信息"""
    global num
    inform.append({'姓名': input('请输入学生姓名:>'),
                   '班级': input('请输入学生班级:>'),
                   '性别': input('请输入学生性别:>'),
                   '住址': input('请输入学生住址:>'),
                   '电话': input('请输入学生电话:>')})
    num += 1


def infodel(inform):
    """用于删除学生信息"""
    global num
    namefind = input('请输入待查找学生姓名:>')
    for i in inform:
        if i['姓名'] == namefind:
            del i
            num -= 1
            break
    else:
        print('未找到')


def infomod(infor):
    """用于修改学生信息"""
    name = input('请输入要修改学生姓名:>')
    choic = 1
    for i in infor:
        if i['姓名'] == name:
            while choic:
                menu2()
                choic = int(input('请输入要修改的信息:>'))
                if choic == 1:
                    i['姓名'] = input('请输入新的姓名:>')
                elif choic == 2:
                    i['班级'] = input('请输入新的班级:>')
                elif choic == 3:
                    i['性别'] = input('请输入新的性别:>')
                elif choic == 4:
                    i['住址'] = input('请输入新的住址:>')
                elif choic == 5:
                    i['电话'] = input('请输入新的电话:>')
            break
    else:
        print('未找到')


def sinprint(inform):
    name = input('请输入待查找学生的姓名:>')
    for i in inform:
        if i['姓名'] == name:
            print('学生姓名:', i['姓名'])
            print('学生班级:', i['班级'])
            print('学生性别:', i['性别'])
            print('学生住址:', i['住址'])
            print('学生电话:', i['电话'])
            print('*' * 30)
            break
    else:
        print('未找到')


def whoprint(inform):
    for i in inform:
        print('学生姓名:', i['姓名'])
        print('学生班级:', i['班级'])
        print('学生性别:', i['性别'])
        print('学生住址:', i['住址'])
        print('学生电话:', i['电话'])
        print('*' * 30)


inforarray = []
choic = 1
num = 0
while choic:
    menu1()
    choic = int(input('请输入:>'))
    if choic == 1:
        infoadd(inforarray)
    elif choic == 2:
        infodel(inforarray)
    elif choic == 3:
        infomod(inforarray)
    elif choic == 4:
        sinprint(inforarray)
    elif choic == 5:
        whoprint(inforarray)
    elif choic == 0:
        pass
    else:
        print('输入错误')
