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
    {  'week': 23,
        'days': {
            'Mon': "Workday",
            'Tue': "Independence Day!",
            'Wed': "Workday",
            'Thu': "Workday",
            'Fri': "Workday",
            'Sat': "Weekend",
            'Sun': "Weekend"
        }
    },
    {  'week': 24,
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

with open("summer_calendar.txt", "w") as file:

     for dic in data:

         file.write(f"Week: {dic["week"]}")

         file.write("--------")

     for key, item in dic["days"]:

         file.write(f"{key}: {item}")