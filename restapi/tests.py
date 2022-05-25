#from django.test import TestCase
from unittest import TestCase

def sum_of_intg(a,b):
    return a + b

class TestSum(TestCase):
    def test_sum(self):
        self.assertEqual(sum_of_intg(1,2),3)
# Create your tests here.
