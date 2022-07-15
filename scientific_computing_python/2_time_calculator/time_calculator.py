def get_day_of_week(dow, num_of_days):
    dows = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
    return dows[(dows.index(dow.title()) + num_of_days) % 7]

def create_time_list(time_param):
    ampm = time_param[-2:]
    if ampm.isalpha():
        time_list = list(map(int, time_param[:-3].split(":")))
        if ampm == "PM":
            time_list[0] = time_list[0] + 12 if time_list[0] != 12 else time_list[0]
    else:
        time_list = list(map(int, time_param.split(":")))
   
    return time_list

def add_time(start, duration, day_of_week = None):
    min_in_a_day = 1440     # 24 * 60
    start_hr, start_min = create_time_list(start)
    duration_hrs, duration_mins = create_time_list(duration)
    
    # new time
    new_minute = (start_min + duration_mins) % 60
    new_hour = ((start_hr + duration_hrs) % 24) + int((start_min + duration_mins) / 60)  
    
    # number of days
    # Adding the start time to duration time to get number of days.  Converting minutes to hours
    num_of_days = int((start_hr + (start_min / 60) + duration_hrs + (duration_mins / 60)) / 24)       
    
    ampm = " AM" if new_hour < 12 or new_hour > 23 else " PM"
    new_hour = new_hour % 12 if new_hour % 12 != 0 else new_hour
    if new_hour == 24: new_hour = 12

    dow = ""
    if day_of_week:
        dow = f", {get_day_of_week(day_of_week,num_of_days)}"
    
    # format number of days
    if num_of_days == 0:
        next_day = ""
    elif num_of_days == 1:
        next_day = " (next day)"
    else:
        next_day = f" ({num_of_days} days later)"
        
    # return new time formatted
    return f"{new_hour}:{new_minute:02d}{ampm}{dow}{next_day}"

if __name__ == "__main__":
    # print(f':{add_time("3:30 PM", "2:12")}: answer: "5:42 PM"') 
    # print(f':{add_time("8:16 PM", "466:02")}: answer: "6:18 AM (20 days later)"')
    # print(f':{add_time("11:40 AM", "0:25")}: answer: "12:05 PM"') 
    # print(f':{add_time("11:59 PM", "24:05")}: answer: "12:04 AM (2 days later)"') 
    # print(f':{add_time("11:55 AM", "3:12")}: answer: "3:07 PM"') 
    print(f':{add_time("11:59 PM", "24:05")}: answer: "12:04 AM (2 days later)"') 
    print(f':{add_time("11:59 PM", "24:05", "Wednesday")}: answer: "12:04 AM, Friday (2 days later)"') 
