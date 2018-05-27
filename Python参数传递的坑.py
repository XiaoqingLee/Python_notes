# 可变类型做参数和不可变类型做参数,
# 只有可变类型list dict才能对参数原地操作,
# 也即函数内部通过参数影响外部变量,
# 其他的不可变类型会在函数体内创建新的拷贝

a, b, c, d, e = 5, (1, 2), "Hello", [1, 2], {}


def change(x):
    if isinstance(x, int):
        x = 10
    if isinstance(x, tuple):
        x = (1, 2, 3)
    if isinstance(x, str):
        x *= 10
    if isinstance(x, list):
        x.append("good")
    if isinstance(x, dict):
        x.update({1: "dddd"})
    print("inner", x)


for x in (a, b, c, d, e):
    change(x)
    print("outer", x)


# 结果:
# inner 10
# outer 5
# inner (1, 2, 3)
# outer (1, 2)
# inner HelloHelloHelloHelloHelloHelloHelloHelloHelloHello
# outer Hello
# inner [1, 2, 'good']
# outer [1, 2, 'good']
# inner {1: 'dddd'}
# outer {1: 'dddd'}
