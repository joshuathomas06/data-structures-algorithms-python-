def reverse_between(self, start_index, end_index):
    # Base case: If the list is empty, has one node, or indices are identical, nothing to do.
    if self.length <= 1 or start_index == end_index:
        return None
        
    # Create a dummy node to handle edge cases (like reversing from index 0).
    # This prevents 'head' from becoming a special case.
    dummy = Node(0)
    dummy.next = self.head
    self.head.prev = dummy
    
    # 1. Position 'prev' at the node immediately BEFORE the reversal section.
    prev = dummy
    for _ in range(start_index):
        prev = prev.next
    
    # 'current' is the first node in the section to be reversed. 
    # It will stay the same node but eventually end up at the 'end_index' position.
    current = prev.next
    
    # 2. Start the reversal loop. 
    # We perform (end_index - start_index) swaps to move all subsequent nodes to the front.
    for _ in range(end_index - start_index):
        # 'move' is the node we are currently plucking out to move to the front.
        move = current.next
        
        # --- PHASE A: Detach 'move' from its current spot ---
        # Connect 'current' to the node AFTER 'move', effectively skipping 'move'.
        current.next = move.next
        
        # If there's a node after 'move', update its backward pointer to 'current'.
        if move.next:
            move.next.prev = current
        
        # --- PHASE B: Insert 'move' at the beginning of the sub-section ---
        # Connect 'move' forward to the node currently at the front of the reversed section.
        move.next = prev.next
        
        # Update that front node's backward pointer to point back to 'move'.
        prev.next.prev = move
        
        # Connect 'prev' forward to our newly moved node.
        prev.next = move
        
        # Connect 'move' backward to 'prev' to complete the insertion.
        move.prev = prev
        
    # 3. Cleanup: Set the head to the actual first node (skip the dummy) 
    # and remove the dummy's backward link for a clean list.
    self.head = dummy.next
    self.head.prev = None