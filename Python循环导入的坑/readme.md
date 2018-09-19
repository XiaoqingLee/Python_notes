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
