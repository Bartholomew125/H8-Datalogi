from timestamp import *

# Testing make_timestamp
print(make_timestamp(12, 34, 56))  # Output: TimeStamp(hours=12, minutes=34, seconds=56)
print(make_timestamp())            # Output: TimeStamp(hours=0, minutes=0, seconds=0)
print(make_timestamp(seconds=23))  # Output: TimeStamp(hours=0, minutes=0, seconds=23)
print()

# Testing valid function
print(valid(12, 34, 61))  # Output: False (Invalid seconds)
print(valid(12, 34, 59))  # Output: True  (Valid timestamp)
print(valid(24, 0, 0))    # Output: False (Invalid hour)
print()

# Testing skip_hour, skip_minute, skip_second
t1 = make_timestamp(12, 34, 56)
print(t1)  # Output: TimeStamp(hours=12, minutes=34, seconds=56)
skip_hour(t1)
print(t1)  # Output: TimeStamp(hours=13, minutes=34, seconds=56)
skip_minute(t1)
print(t1)  # Output: TimeStamp(hours=13, minutes=35, seconds=56)
skip_second(t1)
print(t1)  # Output: TimeStamp(hours=13, minutes=35, seconds=57)
print()

# Testing skip across hour and day boundaries
t1 = make_timestamp(23, 59, 59)
t2 = make_timestamp(0, 0, 1)
print(t1)  # Output: TimeStamp(hours=23, minutes=59, seconds=59)
skip(t1, t2)
print(t1)  # Output: TimeStamp(hours=0, minutes=0, seconds=0)
print()

# Testing skip that impacts minutes and hours
t1 = make_timestamp(22, 59, 59)
t2 = make_timestamp(1, 0, 2)
print(t1, t2)  # Output: TimeStamp(hours=22, minutes=59, seconds=59) TimeStamp(hours=1, minutes=0, seconds=2)
skip(t1, t2)
print(t1)  # Output: TimeStamp(hours=0, minutes=0, seconds=1)
print()

# Testing equals function
t1 = make_timestamp(12, 0, 0)
t2 = make_timestamp(12, 0, 0)
print(equals(t1, t2))  # Output: True
print()
t3 = make_timestamp(13, 0, 0)
print(equals(t1, t3))  # Output: False
print()

# Testing copy function
t1 = make_timestamp(5, 30, 15)
t_copy = copy(t1)
print(t_copy)          # Output: TimeStamp(hours=5, minutes=30, seconds=15)
print(equals(t1, t_copy))  # Output: True
print()

# Testing to_string function
t1 = make_timestamp(14, 5, 9)
print(to_string(t1))   # Output: "14:5:9"
