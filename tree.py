
class Tree():

    def __init__(self, node, left = None, right = None):
        self.node = node   # content of this node
        self.left = left   # left subtree
        self.right = right # right subtree


def height(tree):
    if tree == None:
        return -1
    else:
        lefth = height(tree.left)
        righth = height(tree.right)
        return max(lefth, righth) + 1

def evaluate(tree):
    if tree.left == None and tree.right == None:
        return int(tree.node)
    else:
        if tree.node == "+":
            return evaluate(tree.left) + evaluate(tree.right)
        elif tree.node == "-":
            return evaluate(tree.left) - evaluate(tree.right)
        elif tree.node == "*":
            return evaluate(tree.left) * evaluate(tree.right)
        elif tree.node == "/":
            return evaluate(tree.left) / evaluate(tree.right)

def postfix(tree):
    output = ""
    if tree.left == None and tree.right == None:
        output = output + tree.node + " "
    elif (tree.left.node).isnumeric() and (tree.right.node).isnumeric():
        output = output + tree.left.node + " " + tree.right.node + " " + tree.node + " "
    else:
        output = output + postfix(tree.left) + postfix(tree.right) + tree.node + " "
    return output

def infix(tree): 
    output = "("
    if tree.left == None and tree.right == None:
        output = output + tree.node + ")"
    elif (tree.left.node).isnumeric() and (tree.right.node).isnumeric():
        output = output + tree.left.node + " " + tree.node + " " + tree.right.node + ")"
    else:
        output = output + infix(tree.left) + tree.node + infix(tree.right) + ")"
    return output

s = []

def rpl_to_tree(input):
    list = input.split()
    for i in range(len(list)):
        if list[i]!="+" and list[i]!="-" and list[i]!="*" and list[i]!="/":
            s.append(Tree(list[i]))
        else:
            right = s.pop()
            left = s.pop()
            s.append(Tree(list[i], left, right))
    return s.pop()


test = Tree("*", Tree("+", Tree("4"), Tree("5")), Tree("3"))
print(postfix(test))
print(infix(test))
test2 = rpl_to_tree("4 5 + 3 *")
print(test2.node)
print(test2.left.node)
print(test2.right.node)
print(test2.left.left.node)
print(test2.left.right.node)




