def time_to_coincide(hour):
    
    t = (60 * hour) / 11
    return t


hour = float(input("Enter the hour (in 24-hour format): "))


minutes_to_coincide = time_to_coincide(hour % 12)


print(f"The hands coincide at {minutes_to_coincide:.2f} minutes past {hour % 12} o'clock in the next hour.")
