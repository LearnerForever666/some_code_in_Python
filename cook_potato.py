# 运用Python当中的类进行烤地瓜
"""
author:LearnerForever
Date:2021 Oct 4th
"""
class Potato(object):
    def __init__(self):
        self.time = 0
        self.flavour=['无']
        self.status = self.statusjug(self.time)

    def statusjug(self,time):
        if time < 3:
            return '生的'
        elif time < 6:
            return '半生不熟'
        elif time < 8:
            return '熟了'
        else:
            return '烤焦了'

    def __str__(self):
        return f'time:{self.time},status:{self.status},flavour:{self.flavour}'

    def cook(self,time):
        self.time+=time
        self.status=self.statusjug(self.time)

    def addflavour(self,flavour):
        if self.flavour[0]=='无':
            self.flavour.remove('无')
        self.flavour.append(flavour)



potato=Potato()
print(potato)
potato.cook(1)
potato.addflavour('番茄酱')
print(potato)
potato.cook(3)
potato.addflavour('孜然')
print(potato)
potato.cook(5)
potato.addflavour('辣椒油')
print(potato)