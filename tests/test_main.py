import unittest
from main import run_agent

class TestMain(unittest.TestCase):
    def test_run_agent(self):
        response = run_agent("What is the weather in Gorakhpur?")
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)

if __name__ == "__main__":
    unittest.main()