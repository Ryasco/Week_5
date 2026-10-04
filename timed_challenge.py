# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!

#20. Expiring Items
#Track values with timestamps. Remove items older than a threshold.
#Input: Add events at t=1, 3, 7, then filter out older than t=5
#Output: [7]

from collections import deque

class ExpiringItems:
    def __init__(self):
        self.items = deque()
    def add(self, timestamp):
        self.items.append(timestamp)
    def remove_older_than(self, threshold):
        while self.items and self.items[0] < threshold:
            self.items.popleft()
        return list(self.items)

tracker = ExpiringItems()
tracker.add(1)
tracker.add(3)
tracker.add(7)
print(tracker.remove_older_than(5))  # Output: [7]


    