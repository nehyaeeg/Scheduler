import helperFunctions as helpers
from timeRange import TimeRange
from dataclasses import dataclass, field
from typing import ClassVar


@dataclass
class People:
    all_busy_range : ClassVar[list] = []  # holds all busy ranges
    name: str
    busy_intervals: list = field(default_factory=list, repr=False)

    def add_busy_intervals(self, time_range_obj: TimeRange):  # O(1)

        self.busy_intervals.append(time_range_obj)
        People.all_busy_range.append(time_range_obj.busy_range)
