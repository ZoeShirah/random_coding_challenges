# Given a list of numbers in random order, write an algorithm that works in
# O(nlog(n)) to find the kth smallest number in the list.
# Can you improve the algorithm from the previous problem to be linear? Explain.


def kth_smallest_num(k, nums):
    """given k and a list of numbers, return the kth smallest number in
    O(nlog(n)) time"""

    nums.sort()  # the Python sort is O(nlog(n))

    return nums[k]


def kth_smallest(k, nums):
    """given k and a list of numbers, return the kth smallest number in
    O(n) time"""

    #use min heap?
