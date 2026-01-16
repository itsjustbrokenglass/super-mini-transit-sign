import requests
import json
from datetime import datetime, timedelta
import pytz
#import os
#from dotenv import load_dotenv


def getJson(stop_code):
    url = (f'http://api.511.org/transit/StopMonitoring?api_key=25d83814-eb1d-450c-8465-63d477c76f79&agency=SF&stopCode={stop_code}')
    response = requests.get(url)
    api_data = response.content.decode('utf-8-sig')
    data = json.loads(api_data)
    return data

# gets next 3 arrival times 
def get_formatted_arrival_times(stop_code):
    data = getJson(stop_code)
    arrival_times = []
    for i in range(0, 3):
        arrival_time = data['ServiceDelivery']['StopMonitoringDelivery']['MonitoredStopVisit'][i]['MonitoredVehicleJourney']['MonitoredCall']['ExpectedArrivalTime']
        arrival_times.append(convert_from_iso(arrival_time, True))
    
    arrival_times = calculate_arrival(arrival_times)
    return arrival_times

# converts from iso format (returned from API) to datetime object for processing
def convert_from_iso(time, is_iso):
    if is_iso:
        time = datetime.fromisoformat(time)

    return time

def calculate_arrival(arrival_times):
    arrival_time_minutes = []
    local_timezone = pytz.timezone('America/Los_Angeles')
    current_time = datetime.now(local_timezone)
    for time in arrival_times:
        time_difference = time - current_time
        time_until_arrival = time_difference.total_seconds() / 60
        arrival_time_minutes.append(int(time_until_arrival))

    return arrival_time_minutes


















