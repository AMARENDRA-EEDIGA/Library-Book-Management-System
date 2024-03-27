# •Create a deque from an existing iterable object.
# •For example, say you’re building an application that scrapes data from search engines and social media sites. At some point, you need to keep track of the three last sites your application requested data from.
# •To solve this problem, you can use a deque with a maxlen of 3
# •Create a deque and append a few elements to the left and right. Next, remove some elements from the left and right sides and reverse the deque.

from collections import deque as dq

l = [1, 2, 3, 4, 5]
deque_obj = dq(l)

print(deque_obj)
print("Adding")
deque_obj.appendleft(0)
deque_obj.append(6)
print(deque_obj)

print("Removing")
deque_obj.popleft()
deque_obj.pop()
print(deque_obj)

print("Reversing")
deque_obj.reverse()
print(deque_obj)