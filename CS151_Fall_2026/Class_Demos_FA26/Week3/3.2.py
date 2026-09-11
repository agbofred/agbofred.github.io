def smart_control(current_temp,target_temp):
    if abs(current_temp - target_temp)< 5:
        print("Off")
    elif current_temp < target_temp:
        print("Heating")
    else:
        print("Cooling")
    if abs(current_temp - target_temp) > 25:
        print("Warning: High Load!")

if __name__ == "__main__":
    smart_control(20, 50)