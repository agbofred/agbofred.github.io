from pgl import GWindow, GArc

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
                  'Mon': "Workday",
                  'Tue': "Independence Day!",
                  'Wed': "Workday",
                  'Thu': "Workday",
                  'Fri': "Workday",
                  'Sat': "Weekend",
                  'Sun': "Weekend"
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
from pgl import GWindow, GArc  
from pgl import GWindow, GArc, GMouseEvent, GCompound
from math import pi
COLORS = ["red", "green", "blue", "orange"] #colors
GW_WIDTH = 500 # width of window
GW_HEIGHT = 500 # height of window
CHART_RADIUS = 150 # radius of pie chart
HIGHLIGHT_THICKNESS = 10 # line thickness when clicked
CHART_X = (GW_WIDTH / 2) - CHART_RADIUS
CHART_Y = (GW_HEIGHT / 2) - CHART_RADIUS
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
r = CHART_RADIUS

space = "---------"
with open(data) as f:
    lines = f.read().splitlines()
    def weeks(week):
        weeks = week
        print(week)
        print(space)
        print(days)
        week = weeks + 1
