import sys
sys.path.append('../')
import unittest
import test_cases
from recursion.recursive_floyd_done import FW


class TestRecursion(unittest.TestCase):
    """Running unit tests. """
    """Original GRAPH"""
    def test_0(self):
        self.assertEqual(test_cases.expected0,FW(test_cases.test0))
    """5x5 matrix"""
    def test_1(self):
       self.assertEqual(test_cases.expected1,FW(test_cases.test1))
    """8x8 matrix"""
    def test_2(self):
       self.assertEqual(test_cases.expected2,FW(test_cases.test2))
    """Float values"""
    def test_3(self):
       self.assertEqual(test_cases.expected3,FW(test_cases.test3))
    """Non-square matrix-> errors"""
    def test_4(self):
       self.assertError(FW(test_cases.test4))
    """16x16 matrix"""
    def test_5(self):
       self.assertEqual(test_cases.expected5,FW(test_cases.test5))
    """Contains negative weights but no negative cycles"""
    def test_6(self):
       self.assertEqual(test_cases.expected6,FW(test_cases.test6))
    """Fully connected graph to ensure all paths are correctly calculated"""
    def test_7(self):
        self.assertEqual(test_cases.expected7, FW(test_cases.test7))
    """#A graph that contains a negative cycle.
    The expected behavior should be defined (e.g., returning an error or a specific value)."""
    def test_8(self):
       self.assertEqual(test_cases.expected8,FW(test_cases.test8))
    """A single node should return zero distance to itself."""
    def test_9(self):
       self.assertEqual(test_cases.expected9,FW(test_cases.test9))
    """Test with a graph where some nodes are not connected at all."""
    def test_10(self):
       self.assertEqual(test_cases.expected10,FW(test_cases.test10))
    """Test with a graph that has self-loops."""
    def test_11(self):
       self.assertEqual(test_cases.expected11,FW(test_cases.test11))
    """A non-square adjacency matrix should raise an error."""
    def test_12(self):
       self.assertError(FW(test_cases.test12))
    """A more complex graph with multiple nodes and varying paths."""
    def test_13(self):
       self.assertEqual(test_cases.expected13,FW(test_cases.test13))


if __name__ == '__main__':
    unittest.main()


