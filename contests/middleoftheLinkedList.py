# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def middleNode(self, head):
		l = 0
		temp = head
		while temp:
			temp = temp.next
			l += 1
		mid = l/2


		temp = head

		for i in xrange(mid):
			temp = temp.next

		return temp



a = ListNode(1)
#b = ListNode(2)
#c = ListNode(3)
#d = ListNode(4)

#a.next = b
#b.next = c
# c.next = d


x =  Solution().middleNode(a)
print x.val
