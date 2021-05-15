def add_time(start, duration,day=''):
  days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
  start_time,hour_period=start.split()
  hour1,minutes1=start_time.split(":")
  hour2,minutes2=duration.split(":")
  days_later=''
  extra_hour,new_minutes=divmod((int(minutes1)+int(minutes2)),60)
  extra_day,new_hour=divmod((int(hour1)+int(hour2)+int(extra_hour)),12)
  new_minutes=format_minutes(new_minutes)
  if new_hour==0:
    new_hour="12"
  if extra_hour==1 and hour_period=="AM":
    extra_day=0
    hour_period=switch_hour_period(hour_period)
  if extra_day%2==1:
    hour_period=switch_hour_period(hour_period)
    extra_day=int(extra_day//2)+1
  else:
    extra_day=int(extra_day/2)
  if extra_day>1:
    days_later="({} days later)".format(extra_day)
  elif extra_day==1:
    days_later="(next day)"
  new_time="{}:{} {} {}".format(new_hour,new_minutes,hour_period,days_later).rstrip()
  if day!='':
    index=days.index(day.lower())
    for i in range(0,extra_day):
      index+=1
      if index>6:
        index=0
    day=days[index]
    new_time="{}:{} {}, {} {}".format(new_hour,new_minutes,hour_period,day.capitalize(),days_later).rstrip()
  return new_time


def switch_hour_period(period):
  if period=="AM":
    return "PM"
  else:
    return "AM"

def format_minutes(minutes):
  if minutes<9:
    return "0"+str(minutes)
  else:
    return str(minutes)