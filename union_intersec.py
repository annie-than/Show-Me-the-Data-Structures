class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    if llist_1.size() > llist_2.size():
        union_list_1 = llist_1
        union_list_2 = llist_2
    else:
        union_list_1 = llist_2
        union_list_2 = llist_1

    union_dict = {}
    node_1 = union_list_1.head
    while node_1:
        if node_1.value not in union_dict:
            union_dict[node_1.value] = 1
        else:
            union_dict[node_1.value] += 1

        node_1 = node_1.next

    node_2 = union_list_2.head
    while node_2:
        if node_2.value in union_dict and union_dict[node_2.value] > 0:
            union_dict[node_2.value] -= 1
        else:
            union_list_1.append(node_2.value)

        node_2 = node_2.next

    return union_list_1


def intersection(llist1, llist2):

    inter_dict = {}
    node_1 = llist1.head
    while node_1:
        if node_1.value not in inter_dict:
            inter_dict[node_1.value] = 1
        else:
            inter_dict[node_1.value] += 1

        node_1 = node_1.next

    inter_list = []
    node_2 = llist2.head
    while node_2:
        if node_2.value in inter_dict and inter_dict[node_2.value] > 0:
            inter_dict[node_2.value] -= 1
            inter_list.append(node_2.value)

        node_2 = node_2.next

    inter_llist = LinkedList()
    for i in inter_list:
        inter_llist.append(i)

    return inter_llist


# Test case 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)


print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))


# Test case 2
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(intersection(linked_list_3, linked_list_4))
print(union(linked_list_3, linked_list_4))








