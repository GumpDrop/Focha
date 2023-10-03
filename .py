
2
3
4
5
6
7
8
9
import turtle
t=turtle
a = raw_input('Your input: ')
for number in a:
    if int(number) == 1:
        t.lt(40),t.fd(30),t.rt(130),t.fd(100)
    elif int(number) == 2:
        t.fd(30),t.rt(90),t.fd(50),t.rt(90),t.fd(30),t.lt(90),
    t.fd(50),t.lt(90),t.fd(30)
