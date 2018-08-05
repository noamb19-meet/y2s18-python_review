# Write your solution for 1.4 here!

def is_prime(x):
	b=2
	while b<x:
		
		if x%b==0:
			print("no")
			return False
		b=b+1

	print("hi")
	return True
			

is_prime(7)