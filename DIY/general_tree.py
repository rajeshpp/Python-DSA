class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        i=0
        p=self.parent
        while p:
            i+=1
            p=p.parent
        return i


    def print_tree(self):
        bars = '|__' if self.parent else ''
        prefix = ' ' * self.get_level()*2 + bars
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
    
def buildtree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cell_phone = TreeNode("Cell Phone")
    cell_phone.add_child(TreeNode("iPhone"))
    cell_phone.add_child(TreeNode("Google Pixel"))
    cell_phone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cell_phone)
    root.add_child(tv)

    root.print_tree()



if __name__ == "__main__":
    buildtree()