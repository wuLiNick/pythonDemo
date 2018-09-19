print('100 + 1 =',100+1)
#number = input('please input a number :')
#print('halo,',number)
print('''line1
line2
line3''')
print(r'''line1\n
line2
line3''')
print('这是中文!')
print('Halo, %s %%' % 'MaLo')
print('%2d-%02d' % (3,1))
print('%.2f' % 3.1495926)
print('{3}{1}{2}{0}'.format('1',2,3,'  d'))
s1=72
s2=85
r=(s1/s2)*100
rr= '%.1f %%' % r
print(rr)
haloList = ['1','2','3']
print(haloList)
print(len(haloList))
haloList.append(1)
print(haloList)
haloList.pop()
print(haloList)
sum = 0
n = 100
while n > 0 :
	sum = sum + n
	n = n - 1
print(sum)

# hello.py

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]

