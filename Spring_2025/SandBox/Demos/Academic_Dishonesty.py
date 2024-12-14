##### Pattern of Copying and Pasting:
data = [
              {'week': 22,
              'days': {
                  'Mon': "Workday",
                  'Tue': "Workday",
                  'Wed': "Workday",
                  'Thu': "Workday",
                  'Fri': "Workday",
                  'Sat': "Weekend",
                  'Sun': "Weekend"
                 }
             },
             {    'week': 23,
                  'days': {
                  
                  
                  }
             },
             {    'week': 24,
                  'days': {
                  'Mon': "Workday",
                  'Tue': "Workday",
                  'Wed': "Workday",
                  'Thu': "Workday",
                  'Fri': "Workday",
                  'Sat': "Weekend",
                  'Sun': "Weekend"
                 }
            }
   ]        
with open("summer_calendar.txt", "w") as file: # Jerenimo
    for week_data in data:
        file.write(f"Week: {week_data['week']}\n")
        file.write("--------\n")
        for day, status in week_data['days'].items():
            file.write(f"{day}: {status}\n")
        file.write("\n")
##########################
with open("summer_calendar.txt", "w") as file: # Jesua
    for week_data in data:
        file.write(f"Week: {week_data['week']}\n")
        file.write("--------\n")
        for day, status in week_data['days'].items():
            file.write(f"{day}: {status}\n")
        file.write("\n")
##########################
with open("summer_calender.txt", "w") as file: #Jack
    for week_data in data:
        file.write(f"week: {week_data['week']}\n")
        file.write("--------\n")
        for day, status in week_data['days'].items():
            file.write(f"{day}: {status}\n")
        file.write("\n")
##########################
with open("summer_calendar.txt", "w") as file: # Kiernan Engen with some understanding?
    for week_data in data:
        file.write(f"Week: {week_data['week']}\n")
        file.write("--------\n")
        for day, activity in week_data.items():
            if day != "week":
                file.write(f"{day}: {activity}\n")
        file.write("\n")
##########################
with open("summer_calendar.txt", "w") as file: # Lucas Casino
    for week_data in data:
        file.write(f"Week: {week_data['week']}\n")
        file.write("--------\n")
        for day, status in week_data['days'].items():
            file.write(f"{day}: {status}\n")
        file.write("\n")

#############################
with open("summer_calendar.txt") as file: ## Suum
    for week_data in data:
        file.write(f"Week: {week_data['week']}\n")
        file.write("--------\n")
        for day, status in week_data['days'].items():
            file.write(f"{day}: {status}\n")   ##this line attempes to iterates over each day and its corresponding status in the week_data dictionary. 
        file.write("\n")  # adds a newline for better separation between weeks



