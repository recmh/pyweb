# -*- coding: UTF-8 -*-
'''
Created on 2015年11月21日

@author: Administrator
'''

from fafer.models import User

User.objects.filter(name='fafer').delete()