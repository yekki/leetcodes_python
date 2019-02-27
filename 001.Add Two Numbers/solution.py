#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        quot = 0
        p = head = ListNode(quot)

        while l1 or l2 or quot != 0:
            if l1:
                quot += l1.val
                l1 = l1.next

            if l2:
                quot += l2.val
                l2 = l2.next

            quot, rem = divmod(quot, 10)

            p.val = rem
            p.next = ListNode(rem)
            p = p.next

        return head

