def hr_to_sec(hrs):
    if hrs<0:
        raise ValueError("hours cannot be negative")
    sec=hrs*3600
    return sec

hrs=7
print(hr_to_sec(hrs),"Seconds")