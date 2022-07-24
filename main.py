"""
Author: Navid A. Ehyaee
Projects For Fun

"""

from timeRange import TimeRange
from people import People
import helperFunctions as helpers

""" This problem  will be done by solving the complement problem. Instead of finding shared free times, we exclude all busy times.
    Remaining intervals are free for all
"""


def main():

     #***test cases: Uncomment***

    # f1 = People("james")
    # f1.add_busy_intervals(TimeRange("12:00", "13:00"))
    # f1.add_busy_intervals(TimeRange("00:00", "01:00"))
    # f1.add_busy_intervals(TimeRange("05:00", "17:00"))
    # f2 = People("Emily")
    # f2.add_busy_intervals(TimeRange("16:00", "21:00"))


    """
    output should be:
    [range(720, 780), range(0, 60), range(300, 1020)]
    [[60, 299], [1020, 1439]]

    Free times are:
    01:00  to  04:59
    17:00  to  23:59

    """

    print(People.all_busy_range)  # see busy_range
    free_list = []  # a list of lists showing free ranges
    free_list = helpers.free_time_finder(free_list, People.all_busy_range)
    print(free_list)  # see free_list

    return helpers.show_pretty_time(free_list) # Final results in Clock readable form



#
# if __name__ == "__main__":
#     main()
