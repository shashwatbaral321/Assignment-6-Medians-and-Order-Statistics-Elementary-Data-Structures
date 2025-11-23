# --- 1. Linked List Implementation ---

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, data):
        """Insert at beginning. O(1)"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_head(self):
        """Delete from beginning. O(1)"""
        if self.head:
            self.head = self.head.next

    def display(self):
        """Traversal. O(n)"""
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Linked List: " + " -> ".join(elements))

# --- 2. Stack (Array-based) ---

class StackArray:
    def __init__(self):
        self.items = []

    def push(self, item):
        """O(1) amortized"""
        self.items.append(item)

    def pop(self):
        """O(1)"""
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

# --- 3. Queue (Array-based) ---

class QueueArray:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """O(1) amortized"""
        self.items.append(item)

    def dequeue(self):
        """
        O(n) - Removing from index 0 requires shifting all other elements.
        This highlights the weakness of array-based queues compared to linked lists.
        """
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0

# --- Demonstration ---

if __name__ == "__main__":
    print("--- Linked List Demo ---")
    ll = LinkedList()
    ll.insert_head(10)
    ll.insert_head(20)
    ll.insert_head(30)
    ll.display()
    print("Deleting head...")
    ll.delete_head()
    ll.display()

    print("\n--- Stack (Array) Demo ---")
    s = StackArray()
    s.push("A")
    s.push("B")
    print(f"Peek: {s.peek()}")
    print(f"Pop: {s.pop()}")
    print(f"Pop: {s.pop()}")

    print("\n--- Queue (Array) Demo ---")
    q = QueueArray()
    q.enqueue("First")
    q.enqueue("Second")
    print(f"Dequeue: {q.dequeue()}")
    print(f"Dequeue: {q.dequeue()}")
