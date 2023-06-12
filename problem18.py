# Find the maximum total from top to bottom of the triangle below:

# Node class to make the tree structure easier
class Node:
    def __init__(self, val, final = True, n1 = None, n2 = None):
        self.val = val
        self.final = final
        self.n1 = n1
        self.n2 = n2
    
    def __str__(self):
        return "Node: " + str(self.val) + ", contains " + str(self.n1) + " and " + str(self.n2)

# === Functions ===

# Function to load nodes from a file, returns the top node with the rest nested, and height of the tree (as a touple)
def loadNodes(fileName):
    # Loading file data
    data = []
    with open(fileName, "r") as f:
        data = f.read().strip().split("\n")
    # Processing data into nodes
    data.reverse() # Going from the bottom up
    tmpNodes = [] # Temporary list, for the nodes of the current line between iterations
    # Getting the bottom line
    for n in data.pop(0).strip().split(" "):
        tmpNodes.append(Node(int(n)))
    # Processing the rest of the lines
    for line in data:
        elems = line.strip().split(" ")
        tmpLine = []
        for i in range(len(elems)):
            el = elems[i]
            tmpLine.append(Node(int(el), False, tmpNodes[i], tmpNodes[i+1]))
        tmpNodes = tmpLine
    # Here, the tmpNodes (list containing current line) should contain the top layer, and thus (for an expected pyramid) only one element
    # Returning touple as described in the function description comment
    return ((tmpNodes[0] if len(tmpNodes) == 1 else tmpNodes), len(data)+1)

# Returns an array of touples, returns the sums of the given node (or start value) and the values of the 2 nested nodes (TLDR sums smallest triangle)
def nextSum(node, startVal = 0):
    if node.final:
        return [(node, (node.val if startVal == 0 else startVal))]
    else:
        return [(node.n1, (node.val if startVal == 0 else startVal) + node.n1.val), (node.n2, (node.val if startVal == 0 else startVal) + node.n2.val)]

# === Code ===

top, layers = loadNodes("problem18.txt")

# Getting the smallest triangle from the top
sums = nextSum(top)
# Continuing for all further layers
for i in range(layers-1):
    tmpList = []
    for t in sums:
        tmpList += nextSum(t[0], t[1])
    sums = tmpList

# Finding the largest sum
biggest = max(sums, key=lambda a: a[1])

print(biggest[1])

# NOTE: Works decently for this small problem, but for larger pyramids, a more efficient solution would have to be thought of