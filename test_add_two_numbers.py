from unittest import TestCase
from add_two_numbers import Solution, ListNode


class Test(TestCase):
    def test_two_zero_return_zero(self):
        zero_list = ListNode()
        self.assertTrue(Solution.addTwoNumbers(self, ListNode(),ListNode()).val == zero_list.val)

    def test_add_two_numbers_from_same_index(self):
        number_list_1 = ListNode(2)
        number_list_2 = ListNode(1)
        answer_list = ListNode(3)
        self.assertTrue(Solution.addTwoNumbers(self, number_list_1, number_list_2).val == answer_list.val)

    # def test_add_two_list_nodes_with_two_nodes_with_same_number(self):
    #     node2 = ListNode(2)
    #     node1 = ListNode(2, node2)
    #
    #     answer_list = ListNode(8)
    #     self.assertTrue(Solution.addTwoNumbers(self, node1, node1).val == answer_list.val)

    def test_add_two_numbers_single_node_but_response_double_node(self):
        number_list_1 = ListNode(6)
        number_list_2 = ListNode(4)
        answer_list2 = ListNode(1)
        answer_list1 = ListNode(0, answer_list2)
        self.assertTrue(Solution.addTwoNumbers(self, number_list_1, number_list_2).val == answer_list1.val)

    def test_add_two_numbers_multiple_node_response_multiple_node(self):
        # 5 -> 2 == 25
        second_number_list_1 = ListNode(2)
        root_number_list_1 = ListNode(5, second_number_list_1)
        # 0 -> 5 == 50
        second_number_list_2 = ListNode(5)
        root_number_list_2 = ListNode(0, second_number_list_2)
        # 5 -> 7 == 75
        second_answer_list = ListNode(7)
        root_answer_list = ListNode(5, second_answer_list)
        # 5 + 0 = 5
        # invert 5 == 5
        # 5 == 7[5]
        resultRootNode = Solution.addTwoNumbers(self, root_number_list_1, root_number_list_2)
        self.assertTrue(resultRootNode.val == root_answer_list.val)
        self.assertTrue(resultRootNode.next.val == root_answer_list.next.val)

