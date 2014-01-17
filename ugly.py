"""
See question here:
Attempts to find out which numbers are ugly
"""

def is_ugly(x):
	single_prims = [2,3,5,7]
	for num in single_prims:
		if x % num == 0:
			return True
	return False

def parse_num(num):
	'''
		123 = 123
		1 + 23 = 24
		1 - 23 = 22
		12 + 3 = 15
		12 - 3 = 9
	'''
	num = map(int, str(num))
	l = len(num)
	i = 0 # current index
	p = 0 # previous index
	while i < l:
		print p
		# print str(num[i]) + " + " + "".join(str(x) for x in num[i+1:l])
		# print str(num[i]) + " - " + "".join(str(x) for x in num[i+1:l])
		# print i
		i = i + 1

	# for n in num:
	# 	print n


def tests():
	print "14 should True: " + str(is_ugly(14))
	print "13 should False: " + str(is_ugly(13))
	parse_num(123)


tests()
