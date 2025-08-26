#AI Usage

##Did I use AI?
>Yes, I used ChatGPT to help create a Python Unittest baseline, that I could edit to work for my project.
>
>Prompt: "Can you give me a basic Unittest example for Python?"
>
>What I did myself: I took the response chatGPT gave me and edited it to make it work for my code, I also created the rest of my Assignment by myself, no need for AI, just Python Documentation.
>
>AI Response:


'# test_calculator.py

import unittest
from calculator import add

class TestCalculator(unittest.TestCase):
    
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)
    
    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(-1, 1), 0)

if __name__ == ''__main__'':
    unittest.main()
'