# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/15 16:05


class A(object):
    def __init__(self, a):
        self.a = a

A.__dict__
a = A(1)
a.__dict__