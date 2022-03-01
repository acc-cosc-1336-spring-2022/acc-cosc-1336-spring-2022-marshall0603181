def get_time(hour, minutes, seconds, time_type, meridien='AM'):
    if hour < 10:
        hour = "0" + str(hour)

    if minutes < 10:
        minutes = "0" + str(minutes)

    if seconds < 10:
        seconds = "0" + str(seconds)

    time = str(hour) + ":" + str(minutes) + ":" + str(seconds)

    if time_type == 12:
        time = time + " " + meridien

    return  time

def get_hour(epoch_seconds):
    pass

def get_minutes(epoch_seconds):
    pass

def get_seconds(epoch_seconds):
    pass

def time_from_utc(utc_offset, utc_zero):
    return utc_zero % utc_offset