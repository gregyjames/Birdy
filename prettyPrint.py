from tinydb import TinyDB, Query
from collections import Counter
import plotly
import plotly.graph_objs as go

db = TinyDB('db.json')

#USER LANGS
a = []
for item in db:
  a.append(item['lang'])

keys = list(Counter(a).keys())
vals = list(Counter(a).values())

trace = go.Pie(labels=keys, values=vals)
plotly.offline.plot([trace], filename='basic_pie_chart.html')

print("Created language pie chart")

#HOW MANY USERS ARE YOU FOLLOWING BACK
b = []
for item in db:
  b.append(item['following'])

vals = list(Counter(b).values())

data = go.Bar(x=["false","true"],y=vals)
plotly.offline.plot([data], filename='basic_bar_chart.html')

print("Created your following bar chart")

#DEFAULT PROFILE IMAGE
c = []
d = []
e = []

for item in db:
  if item['default_profile_image'] is True:
    c.append(item['screen_name'])
    d.append(item['id'])
    e.append(item['default_profile_image'])
    
trace = go.Table(header=dict(values=['Screen Name', 'ID', 'default_profile_image']),cells=dict(values=[c, d, e]))

data = [trace] 
plotly.offline.plot(data, filename='basic_table_html.html')
print("Created Table")