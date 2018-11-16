import sys

for pair in list(sys.stdin)[1:]:
	id, n = map(int, pair.split())
	print("%d %d %d %d" % (id, ((n*(n+1))/2), n**2, n*(n+1)))




