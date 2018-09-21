def count():
	def f(j):
		return lambda : j*j
    fs=[]
    for i in range(1,4):
        fs.append(f(i))
    return fs