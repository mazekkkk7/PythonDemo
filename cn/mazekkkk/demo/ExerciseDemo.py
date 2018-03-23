# coding=utf-8

# x = input("x:")
# y = input("y:")
# print("the multiplication result")
# print(x * y)

# if 1 == 2: print 'one equals two'
# if 1 == 1: print 'one equals one'

# name = raw_input("What is you name?")
# print 'Hello,'+name+'!'
# raw_input("Press <enter>")

# print 'C:\nowhere'
# print r'C:\nowhere'

maze = ['maze',27]
chy = ['cy',28]
database = [maze,chy]
print database

# greeting = 'Hello'
# print greeting[0]
# print greeting[-1]

# fourth = raw_input('Year:')[3]
# print fourth

# number = [1,2,3,4,5,6,7,8,9,10]
# print number[:]
# print number[0:10]
# print number[0:-1]
# print number[0:0]
# print number[::2]
# print number[-10::2]

# numberZero = [1,2,3]
# numberOne = [4,5,6]
# print numberZero+numberOne
# print 'Hello,'+'world!'
# print numberZero * 2
# print 'Hello ' * 5

# sequence = [None] * 10
# print sequence

# permissions = 'rw'
# print 'w' in permissions
# print 'w' in permissions

# users = ['liyuchun','zengyike']
# print raw_input('Enter you user name:') in users

# subject = '$$$ Get rich now!!! $$$'
# print '$$$' in subject

# database = ['chengbadan','1234'],['SB','1234'],['CHENGSB','1234']
# username = raw_input('User name:')
# pin = raw_input('PIN code:')
#
# if[username,pin] in database : print 'Access granted'

# numbers = [100,34,678]
# print len(numbers)
# print max(numbers)
# print min(numbers)
# print max(2,3)
# print min(9,3,2,5)

# print list('Hello')

# x = [1,1,1]
# x[1] = 2
# print x

# names = ['Alice','Beth','Cecil','Dee-Dee','Earl']
# del names[2]
# print names

# name = list('perl')
# print name
# name[2:] = list('ar')
# print name

# name = list('Perl')
# print name
# name[1:] = list('ython')
# print name

# numbers = [1,5]
# print numbers
# numbers[1:1] = [2,3,4]
# print numbers
# numbers[1:4] = []
# print numbers

# lst = [1,2,3]
# lst.append(4)
# print lst

# print ['to','be','or','not','to','be'].count('to')

# x = [[1,2],1,1,[2,1,[1,2]]]
# print x.count(1)
# print x.count([1,2])

# a = [1,2,3]
# b = [4,5,6]
# print a
# print b
# a.extend(b)
# print a

# knights = ['We','are','the','knight','who','say','ni']
# print knights.index('who')

# numbers = [1,2,3,5,6,7]
# print numbers
# numbers.insert(3,'four')
# print numbers

# numbers = [1, 2, 3, 5, 6,7]
# numbers[3:3] = ['four']
# print numbers

# x = [1,2,3]
# print x.pop()
# print x
# print x.pop(0)
# print x

# x = [1,2,3]
# x.append(x.pop())
# print x

# x = ['to','be','or','not','to','be']
# x.remove('be')
# print x

# x = [1,2,3]
# x.reverse()
# print x

# x = [1,2,3]
# print list(reversed(x))

# x = [4,6,2,1,7,9]
# x.sort()
# print x

# x = [4,6,2,1,7,9]
# y = x[:]
# y.sort()
# print x
# print y

# x = [4,6,2,1,7,9]
# y = sorted(x)
# print y

# print sorted('python')

# print cmp(42,32)
# print cmp(99,100)
# print cmp(10,10)
#
# numbers = [5,2,9,7]
# numbers.sort(cmp)
# print numbers

# x = ['aardvark','abalone','acme','add','aerate']
# x.sort(key=len)
# print x

# x = [4,6,2,1,7,9]
# x.sort(reverse=True)
# print x

# print (1,2,3)
# print 3*(40+2)
# print 3*(40+2,)

# x = [1,2,3]
# print tuple(x)
# y = 'abc'
# print tuple(y)

# x = 1,2,3
# print x[1]
# print x[0:2]

# string = "Hello,%s,%s enough for ya?"
# values = ('world','Hot')
# print string % values

# string = "Pi with three decimals:%.3f"
# from math import pi
# print string % pi

# from string import Template

# s = Template('$x. glorious $x!')
# print s.substitute(x='slurm')

# s = Template("It'S ${x}tastic!")
# print s.substitute(x='slurm')

# s = Template("Make $$ selling $x")
# print s.substitute(x='slurm')

# s = Template('A $thing must never $action')
# d = {}
# d['thing'] = 'gentleman'
# d['action'] = 'show his socks'
# print s.substitute(d)

# print '%s plus %s equals %s' %(1,1,2)

# print 'Price of egg: $%d' %42
# print 'Hexadecimal price of egg: %x' %42
# from math import pi
# print 'Pi: %f...' %pi
# print 'Very inexact estimate of pi: %i' % pi
# print 'Using str: %s' % 42L
# print 'Using repr: %r' % 42L
# print '%10f' % pi
# print '%10.2f' % pi
# print '%.2f' % pi
# print '%.5s' % 'Guido van Rossum'
# print '%.*s' % (5,'Guido van Rossum')
# print '%010.2f' % pi
# print '%-10.2f' % pi
# print ('%+5d' % 10) + '\n' + ('%+5d' % -10)

# phonebook = {'Beth':'9102','Alice':'2341','Cecil':'3258'}
# print phonebook
# print "Cecil'S phone number is %(Cecil)s." % phonebook
# print phonebook.get('Cecil')

# template = '''<html>
# <head><title>%(title)s</title></head>
# <body>
# <h1>%(title)s</h1>
# <p>%(text)s</p>
# </body>'''
# data = {'title':'My Home Page','text':'Welcome to my home page!'}
# print template % data
