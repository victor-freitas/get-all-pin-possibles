def solution(seconds):
    if seconds == 0:
        return "now"

    # define the time units in seconds
    units = [("year", 365 * 24 * 60 * 60),
             ("day", 24 * 60 * 60),
             ("hour", 60 * 60),
             ("minute", 60),
             ("second", 1)]

    res = []

    for unit_name, unit_seconds in units:
        if seconds >= unit_seconds:
            # returns a tuple containing the quotient and remainder when dividing two numbers
            unit_count, seconds = divmod(seconds, unit_seconds)
            if unit_count > 1:
                unit_name += "s"
            res.append(f"{unit_count} {unit_name}")

    if len(res) > 1:
        return ', '.join(res[:-1]) + ' and ' + res[-1]

# Test cases
print(solution(62)) 
print(solution(3662))
print(solution(0))    
print(solution(3600))
