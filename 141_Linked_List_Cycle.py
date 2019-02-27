#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nset = set()

        while head:
            if head in nset:
                return True
            else:
                nset.add(head)
            head = head.next

        return False

    def hasCycle2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None: return False

        slow_node = head
        fast_node = head.next

        while slow_node != fast_node:
            if fast_node is None or fast_node.next is None: return False
            slow_node = slow_node.next
            fast_node = fast_node.next.next

        return True