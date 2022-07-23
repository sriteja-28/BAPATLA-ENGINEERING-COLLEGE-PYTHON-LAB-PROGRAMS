import itertools
z={'1':['a','b'],'2':['c','d']}
for i in itertools.product(*[z[k] for k in z.keys()]):
	print("\n".join(i))
	