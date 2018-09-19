m=input('请输入杨辉三角层数:')
def triangles(m):
	n = 1
	L = []
	while n<= m:#number
		l, L = L, []
		for i in range(1, n+1):
			if i== 1 or i== n :
				L.append(1)
			else:
				L.append(l[i - 2] + l[i - 1])
		print(L)
		n = n + 1
	print('done!')
triangles(int(m))
#杨辉三角   m=10
#1  [1]
#2  [1, 1]
#3  [1, 2, 1]
#4  [1, 3, 3, 1]
#5  [1, 4, 6, 4, 1]
#6  [1, 5, 10, 10, 5, 1]
#7  [1, 6, 15, 20, 15, 6, 1]
#8  [1, 7, 21, 35, 35, 21, 7, 1]
#9  [1, 8, 28, 56, 70, 56, 28, 8, 1]
#10 [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
#    done!