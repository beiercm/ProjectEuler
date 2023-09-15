target = 600851475143 
max_prime_factor = 0

sieve_size = round(target ** .5)
sieve = [1] * sieve_size

sieve[0] = 0
sieve[1] = 0

n = 2

while n < sieve_size:
	if sieve[n] == 1:
		mult = 2
		temp_n = n * mult

		while temp_n < sieve_size:
			sieve[temp_n] = 0
			mult += 1
			temp_n = n * mult

	n += 1

for index, val in enumerate(sieve):
	if val == 1:
		if target % index == 0:

			max_prime_factor = max(max_prime_factor, index)

print(max_prime_factor)