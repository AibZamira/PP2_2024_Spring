from datetime import datetime

def date_difference_in_seconds(date1, date2):
    # Convert the dates to datetime objects
    datetime1 = datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')
    datetime2 = datetime.strptime(date2, '%Y-%m-%d %H:%M:%S')

    # Calculate the difference in seconds
    difference_seconds = abs((datetime2 - datetime1).total_seconds())
    return difference_seconds

# Example usage:
date1 = '2024-01-01 00:00:00'
date2 = '2024-02-01 12:30:15'
difference = date_difference_in_seconds(date1, date2)
print("Difference between the two dates in seconds:", difference)
