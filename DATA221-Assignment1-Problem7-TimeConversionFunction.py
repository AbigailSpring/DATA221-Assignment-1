def seconds_since_midnight_to_current_time(seconds_since_midnight):
    if not isinstance(seconds_since_midnight, int):
        return "Input must be an integer number of seconds."
    if seconds_since_midnight < 0 or seconds_since_midnight >= 24 * 60 * 60:
        return "Input must be between 0 and 86399 seconds."
    total_hours = seconds_since_midnight // 3600
    remaining_seconds = seconds_since_midnight % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    if total_hours >= 12:
        period = "PM"
    else:
        period = "AM"

    hours = total_hours % 12
    if hours == 0:
        hours = 12

    return f"{hours} {minutes} {seconds} {period}"
print(seconds_since_midnight_to_current_time(19067))