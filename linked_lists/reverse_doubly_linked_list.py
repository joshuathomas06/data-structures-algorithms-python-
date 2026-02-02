def reverse(self):
        temp = self.head
        while temp is not None:
            # swap the prev and next pointers of node points to
            temp.prev, temp.next = temp.next, temp.prev
            
            # move to the next node
            temp = temp.prev
            
        # swap the head and tail pointers
        self.head, self.tail = self.tail, self.head