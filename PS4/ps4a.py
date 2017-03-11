# Problem Set 4A
# Authors: {oceliker, kmahar}@mit.edu
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx
# Late Days Used: x

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the tests named data_representation should pass.
tree1 = [2, [1, 10]]
tree2 = [[15,9],[10,[9,8]]]
tree3 = [[12,21], [17,2],[6]]


# Part A1: Addition on tree leaves

def add_tree(tree):
    """
    Recursively computes the total of all tree leaves.
    Returns an integer representing the sum.

    Inputs
       tree: A list (potentially containing sublists) that
       represents a tree structure.
    Outputs
       total: An int equal to the sum of all leaves of the tree.

    """

    # TODO: Your code here
    pass


# Part A2: Arbitrary operations on tree leaves

def addem(a,b):
    """
    Example operator function.
    Takes in two integers, returns their sum.
    """
    return a + b

def prod(a,b):
    """
    Example operator function.
    Takes in two integers, returns their product.
    """
    return a * b

def operate_tree(tree, op, base_case):
    """
    Recursively runs a given operation on tree leaves.
    Return type depends on the specific operation.

    Inputs
       tree: A list (potentially containing sublists) that
       represents a tree structure.
       op: A function that takes in two inputs and returns the
       result of a specific operation on them.
       base_case: What the operation should return as a result
       in the base case (i.e. when the tree is empty).
    """

    # TODO: Your code here
    pass

# Part A3: Searching a tree

def search9(a, b):
    """
    Operator function that searches for the integer value 9 within its inputs.

    Inputs
        a, b: integers or booleans
    Outputs
        True if either input is equal to True or 9, and False otherwise
    """

    # TODO: Your code here
    pass

if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # Do not erase the pass statement below.
    pass
