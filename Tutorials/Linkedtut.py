class Node:
    def __init__(self, data, next = None):
        self._data = data;
        self._next = next;

    def get_data(self):
        return self._data;

    def set_data(self, data):
        self._data = data;
    
    def get_next(self):
        return self._next;
    
    def set_next(self, next):
        self._next = next;
    
    def __str__(self):
        ret = "Data:{}".format(self.get_data());
        if self.get_next():
            ret += ", Next:{}".format(self.get_next().get_data());
        else:
            ret += ", Next: none";
        return ret #:3



node = Node("A", None)
print(str(node))
node2 = Node("B", node)
print(str(node2))

#list initialisationL
ptr = None;
for count in range(5):
    ptr = Node(count + 1, ptr);

probe = ptr



def search_linked(ll, item):
    probe = ll
    index = 0
    while probe :
        print(probe)
        if probe.get_data() == item:
            print(f"Item found at index {index}")
            return True
        probe = probe.get_next()
        index += 1
    return False

def insert(ll, item, dest):
    probe = ll
    index = 0

    if dest == 0:
        item.set_next(ll)
        return item

    while probe:
        if index == dest - 1:
            item.set_next(probe.get_next())
            probe.set_next(item)
            return ll

        probe = probe.get_next()
        index += 1
# this insert is a bit weird
new = insert(ptr, Node(10), 4)
print(search_linked(new, 10))

def app(ll, item):
    probe = ll
    while probe:
        if not probe.get_next():
            probe.set_next(item)
            return ll
        probe = probe.get_next()

def prepp(ll, item):
    return insert(ll, item, 0)

new1 = app(ptr, Node(11))
print(search_linked(new1, 11))
