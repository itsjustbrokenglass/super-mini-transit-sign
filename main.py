from transit import get_formatted_arrival_times

# one for outbound one for inbound? press button to calculate each

def main():
    stop_codes_outbound = [13428, 15201] #7, N Judah
    for stop_code in stop_codes_outbound:
        print(get_formatted_arrival_times(stop_code))

main()