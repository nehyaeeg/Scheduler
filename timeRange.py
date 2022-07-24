from dataclasses import dataclass, field
import helperFunctions as helper


@dataclass
class TimeRange:
    # times will converted to a minutes from 0 -> 24x60 = [0,1,2,3,4... 1440]

    # start and end time in a format 00:00 to 01:30 for example
    start_time: str
    end_time: str

    # times converted to minutes spent from 0, so 01;30 will be 90
    start_minutes: int = field(init=False)
    end_minutes: int = field(init=False)
    busy_range: range = field(init=False)  # Busy range

    # for init = false fields
    def __post_init__(self):  # O(1)
        self.start_minutes = helper.timernage_to_minutes(self.start_time)
        self.end_minutes = helper.timernage_to_minutes(self.end_time)
        self.busy_range = range(self.start_minutes, self.end_minutes)
