class PriorityQueue:
    def __init__(self):
        self.front = None

    def is_empty(self):
        if self.front == None:
            return True
        else:
            return False

    def get_length(self):
        length = 0
        if not self.is_empty():
            length = 1
            temp_node = self.front
            while temp_node.next:
                length += 1
        return length

    def pop_min(self):
        if not self.is_empty():
            temp_node = self.front
            self.front = self.front.next
            return temp_node

    def insert(self, data, priority):
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
        return self.front


class PriorityQueueNode:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None
