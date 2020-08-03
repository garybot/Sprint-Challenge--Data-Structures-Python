class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # recursive insert
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value);
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value);
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    # recursive contains
    def contains(self, target):
        if self.value == target:
            return True
        elif target <= self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # STRETCH:
    def delete(self, value):
        return "Don't!"

    # Return the maximum value found in the tree
    def get_max(self):
        max = self
        while max.right is not None:
            max = max.right
        return max.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # self and fn(self.value)
        # self.right and self.right.for_each(fn)
        # self.left and self.left.for_each(fn)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)
        fn(self.value)
