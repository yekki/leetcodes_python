#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def display(self):
        node = self
        while True:
            if node.next is None:
                print(node.val, end='')
                break
            else:
                print(node.val, '->', end='')
                node = node.next
        print()


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = ''
        n = l1
        while True:
            s1 += str(n.val)
            if n.next is None:
                break
            else:
                n = n.next
        s1 = s1[::-1]

        s2 = ''
        n = l2
        while True:
            s2 += str(n.val)
            if n.next is None:
                break
            else:
                n = n.next
        s2 = s2[::-1]

        sum = str(int(s1) + int(s2))

        sum = sum[::-1]

        head = ListNode(int(sum[0]))
        node = head
        for i in range(1, len(sum)):
            node.next = ListNode(int(sum[i]))
            node = node.next

        return head




if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    l1.display()
    l2.display()
    solution = Solution()
    solution.addTwoNumbers(l1, l2)
