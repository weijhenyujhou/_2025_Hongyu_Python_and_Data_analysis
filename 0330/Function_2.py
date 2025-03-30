# args 將傳入值轉換成tuple
def foo(*args):
    for item in args:

        print(item, end=' ')
    print(type(args))

foo (1,2,3,4,'hello')

# **kwargs 將傳入值轉換成Dict
def foo2(**kwargs):
    #print(type(kwargs))
    for name,value in kwargs.items():
        print(f'{name}:{value}', end=' \n')

foo2(name =' Chen', email = 'asdf@gmail.com')

# arge跟kwargs同時存在
def foo3(*arge,**kwargs):
    print(arge)
    print(kwargs)

foo3([1,2,3,4,'hello'],name =' Chen', email = 'asdf@gmail.com')

# 三種同時存在
def foo4(x,y,*args,**kwargs):
    print(x,y,args,kwargs)
    test = list(args)
    print(type(test))
foo4(2,3,2,3,4,5,name =' Chen', email = 'asdf@gmail.com')
