def alarm_clock(day, vacation):
    """
    Return the alarm time based on day of week and vacation status.
    0=Sun, 6=Sat.
    """
    weekend = (day == 0 or day == 6)

    if vacation:
        # On vacation: weekdays → "10:00", weekends → "off"
        return "off" if weekend else "10:00"
    else:
        # Not vacation: weekdays → "7:00", weekends → "10:00"
        return "10:00" if weekend else "7:00"

alarm_clock(1, False)  #'7:00'
alarm_clock(5, False)  #'7:00'
alarm_clock(0, False)  #'10:00'
       
