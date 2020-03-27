#!/usr/bin/python
import os, shutil, time
base_dir = raw_input('Enter a directory: ')
working_dir = ('%s/test_dir' % (base_dir))
try:
    os.mkdir(working_dir)
except:
    print('%s already exists' % (working_dir))

for files in range(0,10):
    f = open('%s/file%s.txt' % (working_dir,files),'w')
    f.write('basic text')
    f.close()

a = open('%s/file%s.txt' % (working_dir,1),'a')
a.write('basic text')

b = open('%s/file%s.txt' % (working_dir,2),'a')
b.write('basic text')

c = open('%s/file%s.txt' % (working_dir,3),'a')
c.write('basic text')

d = open('%s/file%s.txt' % (working_dir,4),'a')
d.write('basic text')

e = open('%s/file%s.txt' % (working_dir,5),'a')
e.write('basic text')

f = open('%s/file%s.txt' % (working_dir,6),'a')
f.write('basic text')

g = open('%s/file%s.txt' % (working_dir,7),'a')
g.write('basic text')

h = open('%s/file%s.txt' % (working_dir,8),'a')
h.write('basic text')

i = open('%s/file%s.txt' % (working_dir,9),'a')
i.write('basic text')

j = open('%s/file%s.txt' % (working_dir,10),'a')
j.write('basic text')

time.sleep(100)

for files in os.listdir(working_dir):
    print(files)

#shutil.rmtree(working_dir, ignore_errors=True)
