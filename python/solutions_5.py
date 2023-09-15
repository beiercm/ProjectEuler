# 2 * 2 * 2 * 2 * 3 * 3 * 5 * 7 * 11 * 13 * 17 * 19

# 2 * 2 * 2 * 3 * 3 * 5 * 7

def find_smallest_mult(target):
	sieve = [1] * target
	product = 1

	current_pos = 2
	sieve[0] = 0
	sieve[1] = 0

	while current_pos < len(sieve):

		if sieve[current_pos] == 1:						
			mult = 2
			cur_product = 1
			while cur_product < target:
				cur_product = current_pos * mult
				
				if cur_product >= target:
					break

				sieve[cur_product] = 0
				mult += 1

			power = 2
			cur_res = 1
			while cur_res < target:
				product *= current_pos
				cur_res = current_pos ** power
				power += 1

		current_pos += 1

	print(product)

find_smallest_mult(20)