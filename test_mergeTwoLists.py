from unittest import TestCase
from mergeTwoLists import mergeTwoLists, ListNode


class Test(TestCase):
    def test_merge_two_empty_lists_should_return_empty_list(self):
        emptyListNode = ListNode(None, None)
        list = mergeTwoLists(emptyListNode, emptyListNode)
        self.assertTrue(list.val == emptyListNode.val)
        self.assertTrue(list.next == emptyListNode.next)

    def test_merge_two_lists_of_the_same_value(self):
        l1 = ListNode(1,None)
        l2 = ListNode(20,None)
        expectedResult = ListNode(1,l2)
        list = mergeTwoLists(l1, l2)
        self.assertTrue(list.val == expectedResult.val)
        self.assertTrue(list.next == expectedResult.next)


