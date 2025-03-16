# Linked List

A **linked list** is a linear data structure consisting of a chain of nodes. Each node contains:

1. **Data** - Stores the value.
2. **Reference (Link)** - Points to the next node (in singly linked lists) or both the next and previous nodes (in doubly linked lists).

### Key Features of Linked Lists:

- **Dynamic Data Structure:** Can grow and shrink during runtime.
- **Non-contiguous Storage:** Elements are not stored in continuous memory locations.

## Advantages of Linked Lists:

- Dynamic size adjustment.
- Efficient insertion and deletion operations.
- Suitable for implementing stacks, queues, and graphs.
- Useful for representing and manipulating polynomials.
- Applied in real-world applications like music players and websites.

## Disadvantages of Linked Lists:

- Extra memory required for storing references.
- Sequential access only (no random access like arrays).

---

## Singly Linked List

A **singly linked list** is a type of linked list where each node contains:

1. **Data** - Holds the value.
2. **Next** - Reference to the next node.

### Structure:

```
Head         Tail
  ↓            ↓
+---+    +---+    +---+    +---+    +---+
| A | -> | B | -> | C | -> | D | -> | E |
+---+    +---+    +---+    +---+    +---+
None
```

- **Head**: Points to the first node.
- **Tail**: The last node points to `None`, indicating the end of the list.

### Singly Linked List Operations:

- **Insertion**: At the beginning, end, or between nodes.
- **Deletion**: Removing nodes by updating the references.
- **Traversal**: Iterating through nodes in one direction.
- **Searching**: Finding a node by its value.

---

## Doubly Linked List

A **doubly linked list** is a type of linked list where each node contains:

1. **Data** - Holds the value.
2. **Next** - Reference to the next node.
3. **Previous** - Reference to the previous node.

### Structure:

```
Head                     Tail
  ↓                        ↓
+---+ <-> +---+ <-> +---+ <-> +---+
| A |     | B |     | C |     | D |
+---+     +---+     +---+     +---+
None                            None
```

### Advantages of Doubly Linked Lists:

- **Bidirectional Traversal:** Can traverse forward and backward.
- **Efficient Deletion:** Easier to remove nodes without full traversal.

### Doubly Linked List Operations:

- **Insertion**: At the beginning, end, or between nodes.
- **Deletion**: Removing nodes efficiently with two pointers.
- **Traversal**: Iterate both forward and backward.
- **Searching**: Locate a node by value.

---

## Circular Linked List

In a **circular linked list**, the last node's next pointer links back to the head node, forming a circular chain.

### Structure of Circular Singly Linked List:

```
Head
  ↓
+---+ -> +---+ -> +---+
| A |    | B |    | C |
+---+ <- +---+ <- +---+
```

---

## Conclusion

Linked lists are versatile data structures used for dynamic storage. Understanding their variations (singly, doubly, and circular) is essential for implementing complex data-handling algorithms efficiently.

