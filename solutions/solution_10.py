def calculate_minute_hand_angle(hour_hand_angle):
  minute_hand_angle = (hour_hand_angle % 30) * 12
  return minute_hand_angle
hour_hand_angle = float(input("Enter the angle by which the hour hand has turned since the beginning of the day: "))
minute_hand_angle = calculate_minute_hand_angle(hour_hand_angle)
print("The angle by which the minute hand has turned since the beginning of the last hour is:", minute_hand_angle)

