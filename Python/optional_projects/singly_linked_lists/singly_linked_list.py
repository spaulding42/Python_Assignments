class SList:
    def __init__(self):
        self.head = None
    
    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self
    
    def add_to_back(self, val):
        new_node = SLNode(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node
        return self

    def print_values(self):
        runner = self.head
        while (runner.next != None):
            print(runner.value)
            runner = runner.next
        print(runner.value)
        return self

    def remove_from_front(self):
        new_head = self.head
        if (new_head.next != None):
            self.head = new_head.next
        return self
    
    def remove_from_back(self):
        runner = self.head
        while (runner.next != None):
            previous = runner
            runner = runner.next
        previous.next = None
        return self

class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

my_list = SList()
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").add_to_back("totally").add_to_back("nailed it!").print_values()
print("----")
my_list.remove_from_front().print_values()
print("----")
my_list.remove_from_back().print_values().remove_from_back().print_values()
