
"""
Write a generator that returns the following "special" dates (datetime objects) for PyBites:

- Our birthday! What is the date every year going forward from the PYBITES_BORN date (datetime.datetime(2017, 12, 19, 0, 0), datetime.datetime(2018, 12, 19, 0, 0), ...)?

- Return every 100th day counting forward from the PYBITES_BORN date (datetime(2017, 3, 29, 0, 0), datetime(2017, 7, 7, 0, 0), ...)

As this is a beginner challenge we're only calculating/ testing a few years ahead of the PYBITES_BORN date. This will omit the next leap year (2020) from the challenge making it a bit easier for you (we will revisit this in an intermediate challenge).

Here is how the generator would work if you import and use it in your REPL:

>>> from gendates import gen_special_pybites_dates
>>> gen = gen_special_pybites_dates()
>>> for _ in range(10):
...     next(gen)
...
datetime.datetime(2017, 3, 29, 0, 0)  # PyBites 100 days old
datetime.datetime(2017, 7, 7, 0, 0)  # PyBites 200 days old
datetime.datetime(2017, 10, 15, 0, 0)  # PyBites 300 days old
datetime.datetime(2017, 12, 19, 0, 0)  # PyBites turned 1 year
datetime.datetime(2018, 1, 23, 0, 0)  # PyBites 400 days old
datetime.datetime(2018, 5, 3, 0, 0)  # PyBites 500 days old
datetime.datetime(2018, 8, 11, 0, 0)  # PyBites 600 days old
datetime.datetime(2018, 11, 19, 0, 0)  # PyBites 700 days old
datetime.datetime(2018, 12, 19, 0, 0)  # PyBites turned 2 years
datetime.datetime(2019, 2, 27, 0, 0)  # PyBites 800 days old

"""


from datetime import datetime
import datetime as dt

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    day_now = PYBITES_BORN
    day_output = day_now

    while True:
        day_now += dt.timedelta(1)
        if day_now.month == 12 and day_now.day == 19:
            yield day_now
        elif day_now == day_output + dt.timedelta(100):
            day_output = day_now
            yield day_now


gen = gen_special_pybites_dates()

for _ in range(10):
    print(next(gen))
