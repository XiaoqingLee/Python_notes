version 0:

```bash
(venv) 
# ~/PycharmProjects/Python_notes [master ✗ (980a389)] ➤ cd Python循环导入的坑 
(venv) 
# ~/PycharmProjects/Python_notes/Python循环导入的坑 [master ✗ (980a389)] ➤ ls
first.py  second.py  start.py
(venv) 
# ~/PycharmProjects/Python_notes/Python循环导入的坑 [master ✗ (980a389)] ➤ python3 first.py 
I'm into first module
I'm into second module
I'm into first module
Traceback (most recent call last):
  File "first.py", line 7, in <module>
    from second import second_function
  File "/home/lee/PycharmProjects/Python_notes/Python循环导入的坑/second.py", line 7, in <module>
    from first import first_function
  File "/home/lee/PycharmProjects/Python_notes/Python循环导入的坑/first.py", line 7, in <module>
    from second import second_function
ImportError: cannot import name 'second_function'
(venv) 
# ~/PycharmProjects/Python_notes/Python循环导入的坑 [master ✗ (980a389)] ➤ python start.py 
I'm into start module
I'm into first module
I'm into second module
Traceback (most recent call last):
  File "start.py", line 7, in <module>
    import first
  File "/home/lee/PycharmProjects/Python_notes/Python循环导入的坑/first.py", line 7, in <module>
    from second import second_function
  File "/home/lee/PycharmProjects/Python_notes/Python循环导入的坑/second.py", line 7, in <module>
    from first import first_function
ImportError: cannot import name 'first_function'
```

version 1:

```bash
(venv) 
# ~/PycharmProjects/Python_notes/Python循环导入的坑 [master ✗ (2ee32fd)] ➤ python3 start.py 
I'm into start module
I'm into first module
I'm into second module
I'm going out of second module
I'm going out of first module
I'm going out of start module
(venv) 
# ~/PycharmProjects/Python_notes/Python循环导入的坑 [master ✗ (2ee32fd)] ➤ python3 first.py 
I'm into first module
I'm into second module
I'm into first module
Traceback (most recent call last):
  File "first.py", line 12, in <module>
    from second import second_function
  File "/home/lee/PycharmProjects/Python_notes/Python循环导入的坑/second.py", line 7, in <module>
    from first import first_function
  File "/home/lee/PycharmProjects/Python_notes/Python循环导入的坑/first.py", line 12, in <module>
    from second import second_function
ImportError: cannot import name 'second_function'
 
```

version 2:

```bash
(venv) 
# ~/PycharmProjects/Python_notes/Python循环导入的坑 [master ✗ (d2c9175)] ➤ python3 first.py 
I'm into first module
I'm into second module
I'm into first module
I'm going out of first module
I'm going out of second module
I'm going out of first module
(venv) 
# ~/PycharmProjects/Python_notes/Python循环导入的坑 [master ✗ (d2c9175)] ➤ python3 second.py 
I'm into second module
I'm into first module
I'm into second module
I'm going out of second module
I'm going out of first module
I'm going out of second module
(venv) 
# ~/PycharmProjects/Python_notes/Python循环导入的坑 [master ✗ (d2c9175)] ➤ python3 start.py 
I'm into start module
I'm into first module
I'm into second module
I'm going out of second module
I'm going out of first module
I'm going out of start module

```

参考：https://blog.miguelgrinberg.com/post/flask-webcast-3-circular-dependencies

说明：

    1.下面三个语句的都会从头到尾执行moduleA的语句：
        form Outermodule import moduleA
        from moduleA import a_function
        import moduleA

    2.$ python3 foo.py 命令执行的时候 foo.py的名字是__main__。 （foo.py 是1号参数，python3 是 0号参数）

    3.解释器访问模块A，在A脚本的一半的位置出现from B import Bfunction，控制结构要转给B，从头执行B的代码， 如果B脚本半腰处有form A import Afunction，这个时候分两种情况
    （1）如果A.py 不是__main__ : python解释器记得之前访问过A，所以它从之前执行过的A的上半部分脚本寻找 Afunction的定义，能找到就找到， 找不到就如实报错：cannot find functionA。
    （2）如果A.py 是 __main__ : 此时python解释器不认为A是之前访问过的A，只记得访问过__main__, 所以它会去从头执行__main__文件的一份拷贝。
