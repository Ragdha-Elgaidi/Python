"""
Given 8 space-separated integers, find the sum of those in even places and
the sum of those in odd places.
○ Note: Even place means the 2nd, 4th, 6th or 8th numbers,
 odd places are the 1st, 3rd, 5th and 7th numbers.
○ Note: the 8 numbers will be on the same line
○ Note: Don’t print any welcome or by messages.
● Input: 11 2 7 9 12 -8 3 -1
● Output: 2 33
● Example Explanation:
○ 2 + 9 + (-8) + (-1) = 2 for the even places
○ 11 + 7 + 12 + 3 = 33 for the odd places
"""

odd1, even1, odd2, even2, odd3, even3, odd4, even4 = map(int, input().split())

sum_even = even1 + even2 + even3 + even4
sum_odd = odd1 + odd2 + odd3 + odd4

print(sum_odd, sum_even)
