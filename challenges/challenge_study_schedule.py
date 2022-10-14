def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    count = 0

    for t1, t2 in permanence_period:
        if not (isinstance(t1, int) and isinstance(t2, int)):
            return None
        if t1 <= target_time <= t2:
            count += 1

    return count
