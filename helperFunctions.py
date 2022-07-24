def timernage_to_minutes(time_str):
    """will covnert time in format HH:MM to int 
    Return: int
    Args:
        time_str (str): HH:MM 
    """
    partition = time_str.split(":")
    hours = int(partition[0])
    minutes = int(partition[1])

    return hours * 60 + minutes


def minutes_to_Str(time_int):
    hours = int(time_int // 60)
    minuts = int(time_int % 60)

    return f"{hours:02d}:{minuts:02d}"


def free_time_finder(free_list, busy_list):
    time = range(1440)  # 24x60

    # helper signal for optimization. Prevents checking remaining intervals if time candidate is rejected already
    free = True

    # find free times and add to free list
    helper_list = []
    for x in time:  # O(n) only variable is n=number of people, others are finite
        for m in busy_list:
            if not free:  # Optimization
                break
            if x in m:
                free = False
                if len(helper_list) != 0: # second element of each free time interval
                    helper_list.append(x - 1)
                    free_list.append(helper_list)
                    helper_list = []

        if not free:
            free = True
            continue
        if len(helper_list) == 0: # first element of each free time interval
            helper_list.append(x)

    if x == time[-1] and free:
        helper_list.append(x) # end case
        free_list.append(helper_list)

    return free_list


# def show_pretty_time(free_list):
#     print("\nFree times are:")
#     for time in free_list:
#         print(minutes_to_Str(time[0]), " to ", minutes_to_Str(time[1]))

def show_pretty_time(free_list):
    res = ""
    res += "\nFree times are:\n"
    for time in free_list:
         res += (minutes_to_Str(time[0]) + " to " + minutes_to_Str(time[1])) + "\n"

    return res