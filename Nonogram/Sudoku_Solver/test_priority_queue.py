import unittest
from priority_queue import PriorityQueue
from priority_queue import PriorityQueueNode


class TestPriorityQueueNode(unittest.TestCase):
    """
    A class used to test the PriorityQueueNode class.

    ...

    Attributes
    ----------
    pq_node : PriorityQueueNode
        a PriorityQueueNode object used for testing

    Methods
    -------
    setUp()
        Sets up the test environment.
    test_node_data()
        Tests the data attribute of the PriorityQueueNode object.
    test_node_priority()
        Tests the priority attribute of the PriorityQueueNode object.
    """

    def setUp(self):
        self.pq_node = PriorityQueueNode(10, 1)

    def test_node_data(self):
        self.assertIsNotNone(self.pq_node.data)

    def test_node_priority(self):
        self.assertIsNotNone(self.pq_node.priority)


class TestPriorityQueue(unittest.TestCase):
    """
    A class used to test the PriorityQueue class.

    ...

    Attributes
    ----------
    py : PriorityQueue
        a PriorityQueue object used for testing

    Methods
    -------
    setUp()
        Sets up the test environment.
    test_insert()
        Tests the insert method of the PriorityQueue object.
    test_pop_min()
        Tests the pop_min method of the PriorityQueue object.
    test_insert_multiple()
        Tests the insert method of the PriorityQueue object with multiple inputs.
    test_peek()
        Tests the peek_min method of the PriorityQueue object.
    """

    def setUp(self):
        self.py = PriorityQueue()

    def test_insert(self):
        self.assertEqual(self.py.get_length(), 0)
        self.py.insert(10, 1)
        self.assertEqual(self.py.get_length(), 1)

    def test_pop_min(self):
        self.py.insert(10, 1)
        self.assertEqual(self.py.get_length(), 1)
        self.py.pop_min()
        self.assertEqual(self.py.get_length(), 0)

    def test_insert_multiple(self):
        self.py.insert(10, 2)
        self.py.insert(8, 3)
        self.py.insert(9, 1)
        pq_node = PriorityQueueNode(9, 1)
        self.assertEqual(self.py.pop_min().priority, pq_node.priority)
        self.py.insert(9, 1)
        pq_node = PriorityQueueNode(9, 1)
        self.assertEqual(self.py.pop_min().data, pq_node.data)

    def test_peek(self):
        self.py.insert(10, 2)
        pq_node = PriorityQueueNode(10, 2)
        self.assertEqual(self.py.peek_min().priority, pq_node.priority)
        self.assertEqual(self.py.peek_min().data, pq_node.data)


if __name__ == "__main__":
    unittest.main()
