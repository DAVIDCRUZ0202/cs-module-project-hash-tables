# By writing in plain english line by line
# what each bit of code does and why it's produced the way it is
# I solidify logical thinking and clarify concepts which might not be very intuitive at first


# This class is used as a replacement for the node and linkedlist class learned about in unit 5
class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    # The above three values are easily recognizable as being components of a node and a linked list


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

"""
The hash table class is where all values are held. This table will hold all key value pairs. 
To deal with colliision, we will use an adopted version of a linked list.
This will essentially be a hash table, with index values. Each index value will point
to the head of a linked list. If more than one value is assigned to that index, that
new value will be the new head of the linked list in that index.
"""
class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """

    # init will track all variables which we will use across all methods of this class
    def __init__(self, capacity):
        self.capacity = max(capacity, MIN_CAPACITY)
        self.table = [None] * capacity
        self.tracker = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        Implement this.
        """
        return len(self.table)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        Implement this.
        """
        return self.tracker / len(self.table)


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit
        Implement this, and/or DJB2.
        """

        # Your code here

    # there are many different hashing functions, djb2 just happens to be a good one
    def djb2(self, key):
        the_hash = 5280

        for char in key:
            the_hash = the_hash * 33 + ord(char)
        return the_hash


    # hashing the key is necessary for every other operation.
    # we have to hash a key so that we can pass it into a valid index in our hash table.
    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    # by using a linked list structure, we deal with collisions where
    # two hashed key-value pairs would usually over-write each other, 
    # the overwrite will now only occur if the keys match.
    # regardless of hashes matching, if the keys are different, we will be able to 
    # create a linked list from the first hashed key-value pair to the next
    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        # take the passed in key, create a hash in order to index it
        index = self.hash_index(key)

        # the cur variable holds the index position of where the hashed key value pair should go
        cur = self.table[index]

        # if a key already exists in the index position of our hash table then this operation takes place
        # We will use a while loop as an exit strategy. when our cur is pointing to None, this loop exits
        while cur != None:
            # check the key value of the current position. if it is equal to the key passed into the put method...
            if cur.key == key:
                # then replace the value of the current position with the value passed into the put function
                cur.value = value
                # this blank return exits the put method without any additional operation
                return
            # if the put operation gets this far, the current position moves to the next slot
            # at which point, the while loop is either entirely executed again, or the while loop exits, which leads to the next piece of code.
            cur = cur.next

        # At this point, the only way that the put method gets this far is if our table had no value at the passed in index position
        # OR
        # if there was only one value at that index position.
        # we first create a new object with the class described above
        new_val = HashTableEntry(key, value)
        # We then assign the .next parameter to equal the table's index position.
        # this is similar to making a new head's .next point to the old head.
        # self.table[index] is technically the old head, so that is the value which our new value should point to
        new_val.next = self.table[index]
        # after setting the proper pointer, we can assign the new "head" of this index slot to be the new value we created.
        # we have to assign the .next pointer before we assign the new head, because the old head will be lost if we don't.
        # by re-assigning the index value to the new value, we have essentially created a new head which already points to the old head
        # this new entry retains .next functionality where, if .next is passed, it will be referring to the old head from above
        self.table[index] = new_val
        # update our tracker so that we have an accurate load factor
        self.tracker += 1


    # The delete function also has a lot of bits of code which all have important functionalities, and must all be 
    # described in plain english to gain a deeper understanding
    def delete(self, key):
        # It is helpful to remember what is actually being done in the deletion of a node in a linked list.
        # in a linked list, the node isn't being outright deleted.
        # The node actually gets all pointers removed from it. This makes it so that
        # nothing points to the deleted node, meaning that the deleted node can never get accessed
        # python coding language will eventually collect this un-used variable and get rid of it.
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        # We begin the same way, in getting an index value for the passed in key,
        # and creating a variable to hold our current position in the linked list of that index slot.
        index = self.hash_index(key)
        cur = self.table[index]
        # If the variable holding the current position is returning none, we print a warning.
        if cur == None:
            print("Warning: Key not found")
        # if the above doesn't work, it is definitely pointing to something.
        # we check the key of this "cur" variable to see if it matches what was passed in
        # and if it is passed in, then that means that the head of this index slot must be deleted.
        elif cur.key == key:
            # by re-assigning the index value to be that of the next item in the list
            self.table[index] = cur.next
            # we remove the only pointer for the deleting item, which was the index.
            # this means that the new index head is what was originally next in the linked list of that index slot
            # we also reduce our tracker by 1 since there is one less item in this hash table
            self.tracker -= 1
        # if the key did not match in the index position, we delete this key by some more pointer shuffling..
        else:
            # begin  by creating a variable to track what is behind the item to be deleted. AKA the "prev"ious item
            prev = cur
            # Since the above "elif" statement didn't work, we need to check the next item to see if the keys match.
            # we can do this by re-assigning our current node to point to the next item.
            cur = cur.next
            # now, while the re-assignment does not result in a None...
            while cur != None:
                # if the keys match
                if cur.key == key:
                    # make the pointer of the previous item's .next point to the next item of the "cur"rent location
                    prev.next = cur.next
                    # blank return
                    return
                # if the delete method gets this far, then we need to move both of our variables forward by one step,
                # so that we can check for deletion again with the while loop
                prev = cur
                cur = cur.next
            # if the while loop exits without returning, we return None, because there was nothing to delete after all.
            return None


    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        index = self.hash_index(key)
        cur = self.table[index]
        while cur != None:
            if cur.key == key:
                return cur.value
            cur = cur.next
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        Implement this.
        """
        #self: list, capacity, length
        old_list = self.table
        new_table = [None]*new_capacity
        self.table = new_table
        self.tracker = 0
        self.capacity = new_capacity
        for i in range(len(old_list)):
            current_entry = old_list[i]
            if current_entry:
                while current_entry:
                    self.put(current_entry.key, current_entry.value)
                    current_entry = current_entry.next


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("") 