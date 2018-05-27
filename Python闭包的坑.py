#!/usr/local/bin/python
# -*- coding: utf-8 -*-


def func():
    a = "hello"
    def change_in_main1():
        print("a = ", a)
        return
    def change_in_main2():
        a = "world"
        print("a = ", a)
        return
    def change_in_main3():
        print("a = ", a)
        a = "world"
        return
    change_in_main1()   # a =  hello
    change_in_main2()   # a =  world
    # change_in_main3() #  有错误!!! print(a) UnboundLocalError: local variable 'a' referenced before assignment


func()

# 总结:
# Python闭包只能跨域读值,不可以写值.
# 当内层函数仅写值的时候,会创建内层作用域内的新的本地变量.
# 当内层函数仅读值的时候,可以实现闭包, 跨域访问外层变量.
# 当内层函数欲先对外层变量读值,然后再写值的时候,会出现本地变量未定义的Error.
