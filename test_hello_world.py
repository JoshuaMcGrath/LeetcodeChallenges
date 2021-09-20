from unittest import TestCase
from hello_world import hello

class Test(TestCase):
    def test_hello(self):
        self.assertTrue(hello("foo"))
