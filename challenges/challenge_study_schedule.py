def study_schedule(permanence_period, target_time):
    count = 0

    if (not isinstance(target_time, int)):
        return None

    for entry, exit in permanence_period:
        if not (isinstance(entry, int) and isinstance(exit, int)):
            return None

        if (entry <= target_time and exit >= target_time):
            count += 1

    return count
