# purete.py


import datetime

def fct01(a):
    return a + 1

def fct02(a):
    return a + cpt

def fct03(a):
    print(a + 1)

def fct04(a):
    print(a + 1)
    return a + 1

def fct05():
    t = datetime.datetime.today()
    return f"{t.hour:02}:{t.minute:02}:{t.second:02}"

def fct06():
    return 10

def fct07(a):
    global cpt
    cpt = a + 1
    return cpt

def fct08(a):
    cpt = a + 1
    return cpt

def fct09(a):
    b = a + 1
    return b

def fct10(a, b):
    return 10

def fct11(k):
    return k + fct01(k)

def fct12(k):
    return k + fct04(k)

def fct13():
    b = int(input("Nombre ? "))
    return b

def fct14(t):
    assert isinstance(t, list)
    if len(t) > 0:
        t[0] = 100
    return t

def fct15(t):
    assert isinstance(t, tuple)
    if len(t) > 0:
        l = list(t)
        l[0] = 100
        return tuple(l)
    return ()

def fct16(t):
    assert isinstance(t, list)
    return t[0]

