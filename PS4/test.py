tree1 = [[1,10], 2]

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

    result = 0

    if not tree: # if it's an empty list
        return int(base_case)

    elif isinstance(tree[0], int): # if the first item is an int
        result = op(result, tree[0])
        print(op(result, operate_tree(tree[1:], op, base_case)))
        return op(result, operate_tree(tree[1:], op, base_case))

    else: # if the first item is a list
        print(op(operate_tree(tree[0], op, base_case), operate_tree(tree[1:], op, base_case)))
        return op(operate_tree(tree[0], op, base_case), operate_tree(tree[1:], op, base_case))

print (operate_tree(tree1, prod, 1))
