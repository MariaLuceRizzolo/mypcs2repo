with open("5th Assignment/rosalind_tree.txt") as file:
    dataset = file.readlines()

    nodes = int(dataset[0])
    list = (dataset[1:])
    len = len(list)
    edges = (nodes-1-len)

    print(edges)