import time 
from datetime import datetime,timedelta,timezone

def date_to_timestamp(year,month,day):
    tz=timezone(timedelta(hours=8))