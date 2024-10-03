from dataclasses import dataclass

@dataclass
class TimeStamp:
    hours: int
    minutes: int
    seconds: int

def make_timestamp(hours: int=0,minutes: int=0,seconds: int=0) -> TimeStamp:
    """Returns an instance of TimeStamp. If no parameters are provided, 
    it defaults to zero."""
    return TimeStamp(hours, minutes, seconds)

def valid(hours: int, minutes: int, seconds: int) -> bool:
    """Checks whether input is a valid timestamp."""
    return (0 <= seconds < 60 and
            0 <= minutes < 60 and
            0 <= hours < 24)

def skip_second(t: TimeStamp) -> None:
    """Skips a second."""
    t.seconds = t.seconds + 1
    if t.seconds == 60:
        skip_minute(t)

def skip_minute(t: TimeStamp) -> None:
    """Skips a minute."""
    t.minutes = t.minutes + 1
    if t.minutes == 60:
        skip_hour(t)

def skip_hour(t: TimeStamp) -> None:
    """Skips an hour.""" 
    t.hours = t.hours + 1
    if t.hours == 24:
        t.hours = 0

def skip(t1: TimeStamp, t2: TimeStamp) -> None:
    """Adds a timstamp to another."""
    t1.hours = t1.hours + t2.hours
    t1.minutes = t1.minutes + t2.minutes 
    t1.seconds = t1.seconds + t2.seconds
    if t1.seconds >= 60:
        t1.seconds = t1.seconds - 60
        t1.minutes = t1.minutes + 1
    if t1.minutes >= 60:
        t1.minutes  = t1.minutes - 60
        t1.hours = t1.hours + 1
    if t1.hours >= 24:
       t1.hours = t1.hours - 24

def equals(t1: TimeStamp, t2: TimeStamp) -> bool:
    """Determines whether t1 and t2 is equal."""
    return (t1.seconds == t2.seconds and
            t1.minutes == t2.minutes and
            t1.hours == t2.hours)

def copy(t: TimeStamp) -> TimeStamp:
    """Returns a copy of t."""
    return(make_timestamp(t.hours, t.minutes, t.seconds))

def to_string(t: TimeStamp) -> str:
    """Returns a textual representation of t."""
    return(f"{t.hours}:{t.minutes}:{t.seconds}")



