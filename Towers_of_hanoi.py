# This Function use the recursion to solve the hanoi problem
'''
author:LearnerForever
Date:2021 Sep 28th
'''
trans = [0, 'a', 'b', 'c']


def hanoi(f, l, floors):
    if floors == 1:
        print('1 : %s -> %s' % (trans[f], trans[l]))
    else:
        hanoi(f, (6 - f - l), floors - 1)
        print('%d : %s -> %s' % (floors, trans[f], trans[l]))
        hanoi((6 - f - l), l, floors - 1)


print('欢迎使用汉诺塔答案生成器')
floor = int(input('请输入汉诺塔初始层数:>'))
a = input('请输入起始柱:>')
b = input('请输入目标柱:>')
hanoi(trans.index(a), trans.index(b), floor)
