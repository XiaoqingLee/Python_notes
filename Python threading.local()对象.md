
```python
# ~ ➤ python3
Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170118] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import threading
>>> class A:
...     pass
... 
>>> a = A()
>>> a
<__main__.A object at 0x7f05185f79b0>
>>> a.foo = 1
>>> a.foo
1
>>> class AnotherThread(threading.Thread):
...     def run(self):
...         a.foo = 2
...         print(a.foo)
... 
>>> AnotherThread().start()
2
>>> a.foo
2
>>> a = threading.local()
>>> a.foo = 1
>>> class AnotherThread(threading.Thread):
...     def run(self):
...         a.foo = 3
...         print(a.foo)
... 
>>> a.foo
1
>>> AnotherThread().start()
3
>>> a.foo
1
>>> 

```
笔记：threading.local()返回的对象在不同的线程中有不同的状态，原理是在不同的线程中有不同的拷贝，在当前线程访问这个对象的时候，对象返回当前线程id对应的实体。这是Flask应用上下文对象 current_app g 和 请求上下文对象 request session 以及 Flask_Login插件中current_user
的原型。
