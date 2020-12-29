


class NameNode:

    def __init__(self,name):

        self.name = name


if __name__ == '__main__':

    n1 = NameNode("xm")
    print(id(n1))
    n2 = NameNode("xh")
    print(id(n2))
    n3 = NameNode("xl")
    print(id(n3))
    n3 = n1
