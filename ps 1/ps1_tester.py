import put_in_function as pif

student_a, student_b, student_c = 0 , 0 , 0

pif.put_in_functions_a()
import ps1a_in_function as student_a
pif.put_in_functions_b()
import ps1b_in_function as student_b
pif.put_in_functions_c()
import ps1c_in_function as student_c


total_number_of_tests = 8
tests_passed = 0
a_tests = 0
b_tests = 0
c_tests = 0
if student_a:
	print('----PART A Test 1----')
	print('RUNNING with annual_salary: 120000, portion_saved: .1, total_cost: 1000000')
	annual_salary = 120000
	portion_saved = .1
	total_cost = 1000000
	actual = 146
	student = student_a.part_a(annual_salary, portion_saved, total_cost)
	if actual != student:
		print('FAILED')
		print("Part A test 1 failed. Correct answer:", actual, "Your answer:", student)
	else:
		print('PASSED')
		tests_passed += 1
		a_tests +=1

	print('----PART A Test 2----')
	print('RUNNING with annual_salary: 80000, portion_saved: .15, total_cost: 500000')
	annual_salary = 80000
	portion_saved = .15
	total_cost = 500000
	actual = 84
	student = student_a.part_a(annual_salary, portion_saved, total_cost)
	if actual != student:
		print("FAILED")
		print("Part A test 2 failed. Correct answer:", actual, "Your answer:", student)
	else:
		print("PASSED")
		tests_passed += 1
		a_tests +=1

	print('----PART A Test 3----')
	print('RUNNING with annual_salary: 1000000, portion_saved: .5, total_cost: 823983349')
	annual_salary = 1000000
	portion_saved = .5
	total_cost = 823983349
	actual = 689
	student = student_a.part_a(annual_salary, portion_saved, total_cost)
	if actual != student:
		print("FAILED")
		print("Part A test 3 failed. Correct answer:", actual, "Your answer:", student)

	else:
		print("PASSED")
		tests_passed += 1
		a_tests += 1

if student_b:
	print('----PART B Test 1----')
	print('RUNNING with annual_salary: 120000, portion_saved: .05, total_cost: 500000, semi_annual_raise: .03')
	annual_salary = 120000
	portion_saved = .05
	total_cost = 500000
	semi_annual_raise = .03
	actual = 119
	student = student_b.part_b(annual_salary, portion_saved, total_cost, semi_annual_raise)
	if actual != student:
		print("FAILED")
		print("Part B test 1 failed. Correct answer:", actual, "Your answer:", student)
	else:
		print("PASSED")
		tests_passed += 1
		b_tests +=1



	print('----PART B Test 2----')
	print('RUNNING with annual_salary: 75000, portion_saved: .05, total_cost: 1500000, semi_annual_raise: .05')
	annual_salary = 75000
	portion_saved = .05
	total_cost = 1500000
	semi_annual_raise = .05
	actual = 231
	student = student_b.part_b(annual_salary, portion_saved, total_cost, semi_annual_raise)
	if actual != student:
		print("FAILED")
		print("Part B test 2 failed. Correct answer:", actual, "Your answer:", student)

	else:
		print("PASSED")
		tests_passed += 1
		b_tests += 1


if student_c:
	print('----PART C Test 1----')
	print('RUNNING with initial_deposit: 150000')
	initial_deposit = 150000
	high_r = .1716
	low_r = .1713
	actual_steps = 12
	student_r, student_steps = student_c.part_c(initial_deposit)
	if not (student_r >= low_r and student_r <= high_r  and abs(student_steps - actual_steps) < 3):
		print("FAILED")
		print("Part C Test 1 failed. Correct answer:", actual_r, "in", actual_steps, "steps")

	else:
		print("PASSED")
		tests_passed += 1
		c_tests += 1



	print('----PART C Test 2----')
	print('RUNNING with initial_deposit: 250050')
	initial_deposit = 250050
	actual_r = 0.0
	student_r, student_steps = student_c.part_c(initial_deposit)
	if not (abs(actual_r - student_r) <= .00001):
		print("FAILED")
		print("Part C test 2 failed. Correct answer:", actual_r, "in", actual_steps, "steps")

	else:
		print("PASSED")
		tests_passed += 1
		c_tests += 1


	print('----PART C Test 3----')
	print('RUNNING with initial_deposit: 250050')
	initial_deposit = 10000
	actual_r = "no r possible"
	student_r, student_steps = student_c.part_c(initial_deposit)
	if not (student_r == actual_r):
		print("FAILED")
		print("Part C test 3 failed. Correct answer:", actual_r, "your_answer", student_r)

	else:
		print("PASSED")
		tests_passed += 1
		c_tests += 1

print("END OF TEST SUITE")
print("You have passed", tests_passed, "out of ", total_number_of_tests, "tests.")
print("PART A", a_tests, " out of 3")
print("PART B", b_tests, " out of 2")
print("PART C", c_tests, " out of 3")
