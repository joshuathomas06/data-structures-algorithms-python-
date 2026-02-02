def swap_pairs(self):
    dummy = Node(0)
    dummy.next = self.head
    if self.head:
        self.head.prev = dummy
    prev = dummy
    first = self.head
    
    while first and first.next:
        second = first.next
        
        # Same pointer swaps as SLL
        prev.next = second
        first.next = second.next
        second.next = first
        
        # DLL-specific: update prev pointers
        second.prev = prev
        first.prev = second
        if first.next:
            first.next.prev = first
        
        # Advance (same as SLL)
        prev = first
        first = first.next
    
    self.head = dummy.next
    if self.head:
        self.head.prev = None