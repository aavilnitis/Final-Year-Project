import unittest
from PriorityQueue import PriorityQueue
from PriorityQueue import PriorityQueueNode


class TestPriorityQueueNode(unittest.TestCase):
    def setUp(self):
        self.pq_node = PriorityQueueNode(10, 1)

    def test_node_data(self):
        self.assertIsNotNone(self.pq_node.data)

    def test_node_priority(self):
        self.assertIsNotNone(self.pq_node.priority)


class TestPriorityQueue(unittest.TestCase):
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
