# Following a youtube tutorial to learn about the syntax and concepts of TDD using python.
# During CS2800 we were tough a lot about TDD, but I'm quite unfamiliar with the specifics in python.
# Code used in this file is from https://www.youtube.com/watch?v=ibVSPVz2LAA&ab_channel=PythonSimplified
import unittest
import string


def encrypt(message):
    abc = string.ascii_letters + string.punctuation + string.digits + " "
    encrypted_message = "".join(
        [
            abc[abc.find(char) + 1] if len(abc) > (abc.find(char) + 1) else abc[0]
            for idx, char in enumerate(message)
        ]
    )
    return encrypted_message


class TestEncryption(unittest.TestCase):
    # Initialise variables for test cases
    def setUp(self):
        self.my_message = "Testing! a;lsdj[2-2lksd;alskd]"

    # Test cases have to start with test_
    def test_inputExists(self):
        self.assertIsNotNone(self.my_message)

    # assertIsInstance checks the type of the first argument and passes if return type = second argument
    def test_inputType(self):
        self.assertIsInstance(self.my_message, str)

    # Function can be passed as argument for assertIsNotNone
    def test_functionReturnsSomething(self):
        self.assertIsNotNone(encrypt(self.my_message))

    # assertEqual checks if two arguments passed to method are equal
    def test_lenio(self):
        self.assertEqual(len(self.my_message), len(encrypt(self.my_message)))

    # assertNotIn checks if argument1 is revealed in argument2 - 'test' unexpectedly found in 'test'
    def test_differentIO(self):
        self.assertNotIn(self.my_message, encrypt(self.my_message))

    def test_outputType(self):
        self.assertIsInstance(encrypt(self.my_message), str)

    def test_shiftedCipher(self):
        abc = string.ascii_letters + string.punctuation + string.digits + " "
        encrypted_message = "".join(
            [
                abc[abc.find(char) + 1] if len(abc) > (abc.find(char) + 1) else abc[0]
                for idx, char in enumerate(self.my_message)
            ]
        )
        self.assertEqual(encrypted_message, encrypt(self.my_message))


if __name__ == "__main__":
    unittest.main()
