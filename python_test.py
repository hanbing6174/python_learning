import os
import NumPy as np
import shutil as st
from os import walk
str = raw_input("Enter your input: ");

if str == '0':
    print "hello world!"
    a = ['this', 'is', 'a', 'list']
    b = ('this', 'is', 'a', 'list')
    c = {'this': 'that', 'is': 'was', 'a':'an', 'dict':'operator'}
    for i in a:
        print i
    print '-----------------\n'

    names = {"jk1","jk2","jk3","jk4"}
    for i, name in enumerate(names):
        print(i, name)
elif str == '1':
    def say_hello():
        print "hello"

    say_hello()
elif str == '2':
    def fab(max):
        n, a, b = 0, 0, 1
        while n < max:
            print b
            c = a
            a=b
            b=c+b
            #a, b = b, a + b
            n = n + 1
    fab(19)
elif str == '3':
    print list(xrange(1, 2, 8))
elif str == '4':
    class AD():
        """Class AD"""
        def __init__(self, x, y, name):
            self.x = x
            self.y = y
            self._name = name
        pass
        def introduce(self):
            print self._name
    aa = AD(11, 12, "lee")
    print AD.__doc__
    aa.introduce()
elif str== '5':
    class Student(object):
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def introduce(self):
            print self.name
        pass
    ss = Student("lee",12)
    print ss.introduce()

elif str == '6':
    print filter(lambda x : x % 2, [y for y in range(10)])
elif str == '7':
    for z in [1, 15, 39, 45]:
        print ('the index is {:*<6d}'.format(z))
elif str == '8':
    #path = 'D:\ImageData\GJ\GJ-0206-1\src\mul'
    path = 'D:\ImageData\GJ\GJ-0206-1\src\pan'
    def printPath(path):
        files = os.listdir(path)
        for f in files:
            if os.path.isfile(path + '/' + f):
                if(f.endswith(".tiff")):
                    with open(path + '/' + f, 'r') as rf:
                        allines = rf.readlines()
                        allines[1] = allines[1].replace('E:\GJ\data', 'D:\ImageData')
                    with open(path + '/' + f, 'w') as wf:
                        wf.writelines(allines)
    printPath(path)
elif str == '9':
    print map(lambda x, y: x*y, [1, 2, 3], [4, 5, 6])
    print reduce(lambda x, y: x*y, [1, 2, 3, 5, 2, 1])
    print [x ** 3 for x in range(10)]
elif str == '10':
    str_a = "Life is Short, you need python"
    print str_a.lower()#lief is short , you need python
    print str_a.find("d py")#23
    print str_a.split('i')#['L', 'ef ', 's Short , you need python']
    dp = str_a.split()
    print '*'.join(dp)
    print [x for x in str_a]
elif str == '11':
    def SearchPath(path):
        for (root, dirs, files) in os.walk(path):
            for filename in files:
                filepath = os.sep.join([root, filename])
                filepath = unicode(filepath, "GB2312")
                print filepath
elif str == '12':
    file1 = 'data/bat/IMG_0001.jpg'
    file2 = 'data/bat/IMG_0002.jpg'
    os.system('mv {} {}'.format(file1, file2))
    print file1
    print file2
else:
    pass