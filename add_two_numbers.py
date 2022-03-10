from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # def __eq__(self, other):
    #     if (isinstance(other, C)):
    #         return self.number == other.number and self.letter == other.letter
    #     return false


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        listOneSum = ""
        listTwoSum = ""
        #125: 5 -> 2 -> 1
        #521 -> reserse -> 125
        while l1 is not None:
            listOneSum += str(l1.val)
            l1 = l1.next

        while l2 is not None:
            listTwoSum += str(l2.val)
            l2 = l2.next

        listOneSum = listOneSum[::-1]
        listTwoSum = listTwoSum[::-1]
        sum = (int(listOneSum) + int(listTwoSum))
        sumOfListsAsArr = int_to_array(sum)
        sumOfListsAsArr = sumOfListsAsArr[::-1]
        rootListNode = ListNode(sumOfListsAsArr[0])
        previousNode = rootListNode
        for x in range(1, len(sumOfListsAsArr)):
            currentListNode = ListNode(sumOfListsAsArr[x])
            previousNode.next = currentListNode
            previousNode = currentListNode
        return rootListNode

def int_to_array(sum):
    return [int(x) for x in str(sum)]

