def part_c(initial_deposit):
	best_r = 0
	steps = 1 # we set this equal to one because in order for the while loop to start, we need to calculate expected savings with a starting interest rate. This is simply the first step of the bisection search, which means r = .5. But since that starts outside of the while loop, I start the steps counter with a value of 1 instead of
	required_savings = 1000000 * 0.25
	integer_guess = 5000
	high_bound = 10000
	low_bound = 0
	expected_savings = initial_deposit * (1 + (integer_guess / (10000 * 12))) ** 36
	
	# Test if the initial deposit is never to get within $100 of the down payment at the maximum possible interest rate
	if initial_deposit * (1 + (1 / 12)) ** 36 - 100 < required_savings:
	    best_r = "no r possible"
	    print(best_r)
	
	elif initial_deposit > required_savings:
	    best_r = 0.0
	    print("Best savings rate:", best_r)
	    print("Steps in bisection search:", steps)
	
	else:
	    while abs(required_savings - expected_savings) > 100:
	        if expected_savings > required_savings:
	            high_bound = integer_guess
	        else:
	            low_bound = integer_guess
	        integer_guess = (high_bound + low_bound) / 2
	        expected_savings = initial_deposit * (1 + (integer_guess / (10000 * 12))) ** 36 # calculate the new current savings
	        steps += 1
	
	    best_r = integer_guess / 10000
	    print("Best savings rate:", best_r)
	    print("Steps in bisection search:", steps)
	return best_r, steps