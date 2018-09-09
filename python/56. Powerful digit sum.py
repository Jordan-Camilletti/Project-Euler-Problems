"""A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?"""

tot=0
top=0
for a in range(100):
	for b in range(100):
		tot=0
		for n in str(a**b):
			tot+=int(n)
		top=max(top,tot)
print(top)