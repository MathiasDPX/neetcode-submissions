# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        nodes_values = []

        while list1:
            nodes_values.append(list1.val)
            list1 = list1.next

        while list2:
            nodes_values.append(list2.val)
            list2 = list2.next

        nodes_values.sort()

        nodes = []
        for val in nodes_values[::-1]:
            if len(nodes) != 0:
                nodes.append(ListNode(val, next=nodes[-1]))
            else:
                nodes.append(ListNode(val))

        if len(nodes) == 0:
            return None
        else:
            return nodes[-1]