# This system can add the information of the students to the memory
"""
author:LearnerForever
Date:2021 Sep 30th
"""
import os


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


def infoadd(infor):
    infor.append({'学生姓名:': input('请输入学生姓名:>'),
                  '学生性别:': input('请输入学生性别:>'),
                  '学生班级:': input('请输入学生班级:>'),
                  '学生住址:': input('请输入学生住址:>'),
                  '学生号码:': input('请输入学生号码:>')})
    print('添加完成!!!')


def wholfind(infor):
    for diction in infor:
        print('*' * 30)
        for k, v in diction.items():
            print(k, v)
    print('打印完成!!!')


def infodel(infor):
    name = input('请输入要删除学生姓名:>')
    for d in infor:
        if d['学生姓名:'] == name:
            del infor[infor.index(d)]
            print('删除成功!!!')
            break
    else:
        print('未找到学生信息!!!')


def infochg(infor):
    name = input('请输入要修改学生的姓名:>')
    for d in infor:
        if d['学生姓名:'] == name:
            choic = 1
            while choic:
                menu2()
                choic = int(input('请输入修改内容:>'))
                if choic == 1:
                    d['学生姓名:'] = input('请输入修改后的学生姓名:>')
                elif choic == 2:
                    d['学生班级:'] = input('请输入修改后的学生班级:>')
                elif choic == 3:
                    d['学生性别:'] = input('请输入修改后的学生性别:>')
                elif choic == 4:
                    d['学生住址:'] = input('请输入修改后的学生住址:>')
                elif choic == 5:
                    d['学生电话:'] = input('请输入修改后的学生号码:>')
                elif choic == 0:
                    pass
                else:
                    print('输入错误，请重新输入!!!')
            print('修改完成!!!')
            break
    else:
        print('未找到学生信息!!!')


def singfind(infor):
    name = input('请输入要查询学生姓名:>')
    for d in infor:
        if d['学生姓名:'] == name:
            for k, v in d.items():
                print(k, v)
            print('打印完毕!!!')
            break
    else:
        print('未找到学生信息!!!')


print('欢迎使用学生信息管理系统')
choic = 1
inforarray=[]
d=[]
fr=open('inform.txt','r',encoding='utf-8')
num=int(fr.readline())
for i in range(0,num):
    for j in range(0,5):
        k=fr.readline()
        v=fr.readline()
        k=k.strip()
        v=v.strip()
        d.append((k,v))
    inforarray.append(dict(d))
while choic:
    menu1()
    choic = int(input('请选择功能:>'))
    if choic == 1:
        infoadd(inforarray)
    elif choic == 2:
        infodel(inforarray)
    elif choic == 3:
        infochg(inforarray)
    elif choic == 4:
        singfind(inforarray)
    elif choic == 5:
        wholfind(inforarray)
    elif choic == 0:
        pass
    else:
        print('输入错误，请重试!!!')
f = open('inform.txt', 'w', encoding='utf-8')
f.write(str(len(inforarray)))
f.write('\n')
for n in range(0, len(inforarray), 1):
    for k, v in inforarray[n].items():
        f.write(k)
        f.write('\n')
        f.write(v)
        f.write('\n')
