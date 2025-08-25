# # https://leetcode.com/problems/merge-two-sorted-lists/

# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

#--------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------- Solution ------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------

# 1- Convert the linked lists to lists and merge them.
# 2- Sort the merged list.
# 3- Convert the sorted list to a linked list and return the

def to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result
# def list_to_linked_list(lst):
#     if not lst:
#         return None
#     head = ListNode(lst[0])
#     current = head
#         for val in lst[1:]:
#             current.next = ListNode(val)
#             current = current.next
    
#     return head
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        list1 = to_list(list1)
        list2 = to_list(list2)
        list3 = list1 + list2
        list3.sort()
        return list_to_linked_list(list3)



# Time complexity : O(nlogn)
# Space complexity : O(n)

# soulution 2

# 1- Create a dummy node and a current node to keep track of the current node.
# 2- Iterate over the two linked lists and compare the values of the nodes.
# 3- Append the node with the smaller value to the current node.
# 4- Move the current node to the next node.
# 5- Move the node with the smaller value to the next node.

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        current = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 or list2
        return dummy.next