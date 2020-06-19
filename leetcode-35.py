leetcode 23
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return
        vals  = []
        for l in lists:
            while l:
                vals.append(l.val)
                l = l.next
        vals.sort()
        l = ListNode('a')
        q = l
        for val in vals:
            p = ListNode(val)
            q.next = p
            q = p
        return l.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return 
        import heapq
        heap = []
        for l in lists:
            while l:
                heapq.heappush(heap,l.val)
                l = l.next
        l = ListNode('a')
        q = l
        while heap:
            p = ListNode(heapq.heappop(heap))
            q.next = p
            q = p
        return l.next




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def merge2(self,node_a,node_b):
        l = ListNode('a')
        p = l
        while node_a and node_b:
            if node_a.val<node_b.val:
                p.next = node_a
                p = node_a
                node_a = node_a.next
            else:
                p.next = node_b
                p = node_b
                node_b = node_b.next
        if node_a:
            p.next = node_a
        if node_b:
            p.next = node_b
        return l.next
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lens = len(lists)
        if lens==0:
            return None
        if lens==1:
            return lists[0]
        mid = lens//2
        return self.merge2(self.mergeKLists(lists[:mid]),self.mergeKLists(lists[mid:lens]))