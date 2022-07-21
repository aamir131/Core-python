data1 = {'Aamir':20000, 'Khan':30000}
print("{0[Aamir]:d} {0[Khan]:d}". format(data1))
print("{g[Aamir]:d} {g[Khan]:d}". format(g=data1))
print("{Aamir} {Khan}".format(**data1))
