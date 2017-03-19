# Problem Set 4A
# Authors: {oceliker, kmahar}@mit.edu
# Name: George Mu
# Collaborators:
# Time Spent: 2:30
# Late Days Used:

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the tests named data_representation should pass.
tree1 = [[1,10], 2]
tree2 = [[15,9],[[9,8],10]]
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
    total = 0

    if not tree: # if it's an empty list
        return 0
    elif isinstance(tree[0], int): # if the first item is an int
        total += tree[0]
        return total + add_tree(tree[1:])
    else: # if the first item is a list
        return add_tree(tree[0]) + add_tree(tree[1:])

    # Using a for loop (but still recursively)
    # sum = 0
    #
    # for i in tree:
    #     if isinstance(i, int):
    #         sum += i
    #     else:
    #         sum += add_tree(i)
    # return sum


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
    op_total = base_case

    if not tree: # if it's an empty list
        return base_case

    elif isinstance(tree[0], int): # if the first item is an int
        op_total = op(op_total, tree[0])

        return op(op_total, operate_tree(tree[1:], op, base_case))

    else: # if the first item is a list
        return op(operate_tree(tree[0], op, base_case), operate_tree(tree[1:], op, base_case))


# Part A3: Searching a tree

def search9(a, b):
    """
    Operator function that searches for the integer value 9 within its inputs.

    Inputs
        a, b: integers or booleans
    Outputs
        True if either input is equal to True or 9, and False otherwise
    """

    if type(a) == int and type(b) == int:
        if a == 9 or b == 9:
            return True
    elif type(a) == bool and type(b) == bool:
        if a == True or b == True:
            return True
    elif type(a) == bool and type(b) == int:
        if a == True or b == 9:
            return True
        else:
            return False
    elif type(a) == int and type(b) == bool:
        if a == False or b == True:
            return True
        else:
            return False
    else:
        return False





if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # Do not erase the pass statement below.
    pass
