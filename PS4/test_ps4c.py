# for running unit tests on 6.00/6.0001/6.0002 student code 

import os
import string
import sys
import unittest
from contextlib import redirect_stdout

import ps4c as student


# A class that inherits from unittest.TestCase, where each function
# is a test you want to run on the student's code. For a full description
# plus a list of all the possible assert methods you can use, see the
# documentation: https://docs.python.org/3/library/unittest.html#unittest.TestCase 
class TestPS4C(unittest.TestCase):

	def setUp(self):
		self.text1 = 'testing message'
		self.text2 = 'A message with punctuation in it... Fun!'
		self.text3 = 'dig in'

		self.encrypt1 = 'tosteng mossago'
		self.encrypt2 = 'A mossago weth pinctiateun en et... Fin!'
		self.encrypt3 = 'deg en'

		# do this so "loading words" doesn't print out every time
		with redirect_stdout(open(os.devnull, "w")):

			self.smsg1 = student.SubMessage(self.text1)
			self.smsg2 = student.SubMessage(self.text2)
			self.smsg3 = student.SubMessage(self.text3)

			self.esmsg1 = student.EncryptedSubMessage(self.encrypt1)
			self.esmsg2 = student.EncryptedSubMessage(self.encrypt2)
			self.esmsg3 = student.EncryptedSubMessage(self.encrypt3)


	def test_submessage_get_message_text(self):
		response = self.smsg1.get_message_text()
		self.assertEqual(response, self.text1, 
			"get_message_text returned %s, but %s was expected" % (response, self.text1))

	def test_submessage_get_valid_words(self):
		with redirect_stdout(open(os.devnull, "w")):
			expected_word_list = student.load_words(student.WORDLIST_FILENAME)
		student_list = self.smsg1.get_valid_words()
		self.assertEqual(expected_word_list, student_list, 
			"get_valid_words does not return expected word list")

		student_list.remove('a')
		new_student_list = self.smsg1.get_valid_words()
		self.assertEqual(len(expected_word_list), len(new_student_list),
			"get_valid_words should return a *copy* of self.valid_words, but your code returns the original list.")

	def test_submessage_build_transpose_dict(self):
		vowels = 'oaeiu'

		expected = {'A' : 'O', 'a' : 'o', 'E' : 'A', 'e' : 'a', 'I': 'E', 'i' : 'e', 'O' : 'I', 'o' : 'i', 'U': 'U', 'u' : 'u'}

		sd1 = self.smsg1.build_transpose_dict(vowels)

		self.assertEqual(52, len(sd1), "The shift dictionary should contain 52 keys, one for each uppercase and lowercase letter.")

		error_msg = "With vowel ordering %s, %s should map to %s, but instead maps to %s"

		for ll in string.ascii_lowercase:
			actual = sd1[ll]
			if ll not in 'aeiou':
				self.assertEqual(ll, actual, error_msg % (vowels, ll, ll, actual))
			else:
				exp = expected[ll]
				self.assertEqual(exp, actual, error_msg % (vowels, ll, exp, actual))

		for ul in string.ascii_uppercase:
			actual = sd1[ul]
			if ul not in 'AEIOU':
				self.assertEqual(ul, actual, error_msg % (vowels, ul, ll, actual))
			else:
				exp = expected[ul]
				self.assertEqual(exp, actual, error_msg % (0, ul, exp, actual))

	def test_submessage_apply_transpose(self):
		error_msg = "Encoding message '%s' with vowel ordering %s failed. Expected %s, got %s"

		sd1 = self.smsg1.build_transpose_dict('aoeui')

		msg1_encoded = self.smsg1.apply_transpose(sd1)
		msg2_encoded = self.smsg2.apply_transpose(sd1)
		msg3_encoded = self.smsg3.apply_transpose(sd1)

		self.assertEqual(msg1_encoded, self.encrypt1, error_msg % (self.text1, 3, self.encrypt1, msg1_encoded))
		self.assertEqual(msg2_encoded, self.encrypt2, error_msg % (self.text2, 1, self.encrypt2, msg2_encoded))
		self.assertEqual(msg3_encoded, self.encrypt3, error_msg % (self.text3, 2, self.encrypt3, msg3_encoded))

	def test_encrypted_submessage_decrypt_message(self):

		error_msg = "Failed to properly decrypt the message '%s'; expected %s, got %s"

		dc1 = self.esmsg1.decrypt_message()
		self.assertEqual(dc1, self.text1, error_msg % (self.encrypt1, self.text1, dc1))

		dc2 = self.esmsg2.decrypt_message()
		self.assertEqual(dc2, self.text2, error_msg % (self.encrypt2, self.text2, dc2))


# Dictionary mapping function names from the above TestCase class to 
# the point value each test is worth. 
point_values = {
	'test_submessage_get_message_text' : 0.0,
	'test_submessage_get_valid_words' : 0.0,
	'test_submessage_build_transpose_dict' : 0.0, 
	'test_submessage_apply_transpose' : 0.5,
	'test_encrypted_submessage_decrypt_message' : 0.5,
}

# Subclass to track a point score and appropriate
# grade comment for a suit of unit tests
class Results_600(unittest.TextTestResult):

    # We override the init method so that the Result object
    # can store the score and appropriate test output. 
    def __init__(self, *args, **kwargs):
        super(Results_600, self).__init__(*args, **kwargs)
        self.output = []
        self.points = 2

    def addFailure(self, test, err):
        test_name = test._testMethodName
        msg = str(err[1])
        self.handleDeduction(test_name, msg)
        super(Results_600, self).addFailure(test, err)

    def addError(self, test, err):
        test_name = test._testMethodName
        self.handleDeduction(test_name, None)
        super(Results_600, self).addError(test, err)

    def handleDeduction(self, test_name, message):
        point_value = point_values[test_name]
        if message is None:
            message = 'Your code produced an error on test %s.' % test_name
        self.output.append('[-%s]: %s' % (point_value, message))
        self.points -= point_value

    def getOutput(self):
        if len(self.output) == 0:
            return "All correct!"
        return '\n'.join(self.output)

    def getPoints(self):
        return self.points

if __name__ == '__main__':

	suite = unittest.TestSuite()
	suite.addTest(unittest.makeSuite(TestPS4C))
	result = unittest.TextTestRunner(verbosity=2, resultclass=Results_600).run(suite)

	output = result.getOutput()
	points = result.getPoints()

	# weird bug with rounding 
	if points < .1:
		points = 0

	print("\nProblem Set 4C Unit Test Results:")
	print(output)
	print("Points: %s/2\n" % points)
