# Implement a MyCalendarTwo class to store your events. 
# A new event can be added if adding the event will not cause a triple booking.
# Your class will have one method, book(int start, int end). 
# Formally, this represents a booking on the half open interval [start, end), 
# the range of real numbers x such that start <= x < end.
# A triple booking happens when three events have some non-empty intersection 
# (ie., there is some time that is common to all 3 events.)
# For each call to the method MyCalendar.book, 
# return true if the event can be added to the calendar successfully without causing a triple booking. 
# Otherwise, return false and do not add the event to the calendar.
# Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)

# Example 1:
# MyCalendar();
# MyCalendar.book(10, 20); // returns true
# MyCalendar.book(50, 60); // returns true
# MyCalendar.book(10, 40); // returns true
# MyCalendar.book(5, 15); // returns false
# MyCalendar.book(5, 10); // returns true
# MyCalendar.book(25, 55); // returns true
# Explanation: 
# The first two events can be booked.  The third event can be double booked.
# The fourth event (5, 15) can't be booked, because it would result in a triple booking.
# The fifth event (5, 10) can be booked, as it does not use time 10 which is already double booked.
# The sixth event (25, 55) can be booked, as the time in [25, 40) will be double booked with the third event;
# the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.
 
# Note:
# The number of calls to MyCalendar.book per test case will be at most 1000.
# In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].

# Hints:
# Store two sorted lists of intervals: one list will be all times that are at least single booked, 
# and another list will be all times that are definitely double booked. 
# If none of the double bookings conflict, then the booking will succeed, 
# and you should update your single and double bookings accordingly.

class MyCalendarTwo:

    def __init__(self):
        # 每个被book了的区间
        self.booked = list()
        # 每个重叠了的区间
        self.overlaped = list()

    def book(self, start: int, end: int) -> bool:
        for os, oe in self.overlaped:
            if max(os, start) < min(oe, end):
                return False

        for bs, be in self.booked:
            ss = max(bs, start)
            ee = min(be, end)
            if ss < ee:
                self.overlaped.append((ss, ee))

        self.booked.append((start, end))
        
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)