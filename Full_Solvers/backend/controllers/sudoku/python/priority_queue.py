class PriorityQueue:
    """
    A class used to implement a priority queue.

    ...

    Attributes
    ----------
    front : PriorityQueueNode
        the front node of the priority queue

    Methods
    -------
    is_empty()
        Checks if the priority queue is empty.
    get_length()
        Returns the length of the priority queue.
    pop_min()
        Removes and returns the node with the minimum priority.
    insert(data, priority)
        Inserts a new node into the priority queue.
    peek_min()
        Returns the node with the minimum priority without removing it.
    """

    def __init__(self):
        """
        Constructs a new PriorityQueue object.
        """
        self.front = None

    def is_empty(self):
        """
        Checks if the priority queue is empty.

        Returns
        -------
        bool
            True if the priority queue is empty, False otherwise
        """
        if self.front == None:
            return True
        else:
            return False

    def get_length(self):
        """
        Returns the length of the priority queue.

        Returns
        -------
        int
            the length of the priority queue
        """
        length = 0
        if not self.is_empty():
            length = 1
            temp_node = self.front
            while temp_node.next:
                length += 1
        return length

    def pop_min(self):
        """
        Removes and returns the node with the minimum priority.

        Returns
        -------
        PriorityQueueNode
            the node with the minimum priority
        """
        if not self.is_empty():
            temp_node = self.front
            self.front = self.front.next
            return temp_node

    def insert(self, data, priority):
        """
        Inserts a new node into the priority queue.

        Parameters
        ----------
        data : any
            the data to be stored in the new node
        priority : int
            the priority of the new node
        """
        # create new node with the data in the argument
        new_node = PriorityQueueNode(data, priority)

        # check if queue is empty, if yes add to front of queue
        if self.is_empty():
            self.front = new_node

        # check if front priority is greater than new_node, add to front if yes
        elif self.front.priority > priority:
            new_node.next = self.front
            self.front = new_node

        # traverse the rest of the nodes
        else:
            temp_node = self.front

            while temp_node.next:
                if priority < temp_node.next.priority:
                    break
                temp_node = temp_node.next

            # put the new_node in the middle of temp_node and temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node

    def peek_min(self):
        """
        Returns the node with the minimum priority without removing it.

        Returns
        -------
        PriorityQueueNode
            the node with the minimum priority
        """
        return self.front


class PriorityQueueNode:
    """
    A class used to represent a node in a priority queue.

    ...

    Attributes
    ----------
    data : any
        the data stored in the node
    priority : int
        the priority of the node
    next : PriorityQueueNode
        the next node in the priority queue

    Methods
    -------
    __init__(data, priority)
        Constructs a new PriorityQueueNode object.
    """

    def __init__(self, data, priority):
        """
        Constructs a new PriorityQueueNode object.

        Parameters
        ----------
        data : any
            the data to be stored in the node
        priority : int
            the priority of the node
        """
        self.data = data
        self.priority = priority
        self.next = None
