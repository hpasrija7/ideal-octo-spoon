t = 3
a = [3,4,5,6,7]
mid = a[2]
if t == mid:
	print("mil gya")
elif t>mid:
	mid = a[3]
	if t==mid:
		print("Found in 2nd Iteration (from 2nd division)")
	elif t>mid:
		mid = a[4]
		if t==mid:
			print("Found in 3rd Iteration (from 2nd division)")
		else:
			print("not found")
elif t<mid:
	mid = a[1]
	if t==mid:
		print("Found in 2nd Iteration (from 1st division)")
	elif t<mid:
		mid = a[0]
		if t==mid:
			print("Found in 3rd Iteration (from 1st division)")
		else:
			print("not found")
else:
	print("element not found")
#print(mid)
