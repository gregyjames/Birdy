from tinydb import TinyDB, Query
from collections import Counter
import plotly
import plotly.graph_objs as go
from genData import get_last_tweet
import time
import progressbar

db = TinyDB('db.json')

#USER LANGS
def User_Lang():
  a = []
  for item in db:
    a.append(item['lang'])

  keys = list(Counter(a).keys())
  vals = list(Counter(a).values())

  trace = go.Pie(labels=keys, values=vals)
  plotly.offline.plot([trace], filename='basic_pie_chart.html')

  print("Created language pie chart")

#HOW MANY USERS ARE YOU FOLLOWING BACK
def Follow_back():
  b = []
  for item in db:
    b.append(item['following'])

  vals = list(Counter(b).values())

  data = go.Bar(x=["false","true"],y=vals)
  plotly.offline.plot([data], filename='basic_bar_chart.html')

  print("Created your following bar chart")

#DEFAULT PROFILE IMAGE
def Default_profile():
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

#Last tweet
def Tweet_Line():
  f = []
  g = []
  h = []
  notweet_user = []

  count = 0;

  bar = progressbar.ProgressBar(redirect_stdout=True, max_value=len(db))
  for item in db:
    last_tweet = get_last_tweet(item['id']);
    if(last_tweet != None):
      f.append(item['screen_name'])
      g.append(last_tweet);
      h.append(item['statuses_count'])
      #print(f[count])
      #print(g[count].year)
    else:
      notweet_user.append(item['screen_name'])
      #print(f[count])
      #print(g[count])
    count = count + 1
    time.sleep(0.1)
    bar.update(count)

  data = [go.Scatter(x=g,y=h,mode='markers',text=f)]

  layout = dict(
      title='User last tweet time',
      xaxis=dict(
          rangeselector=dict(buttons=list([
                dict(count=1,label='1d',step='day',stepmode='backward'),
                dict(count=1,label='1m',step='month',stepmode='backward'),
                dict(count=6,label='6m',step='month',stepmode='backward'),
                dict(step='all')
          ])),
      rangeslider=dict(),
      type='date'
      )
  )
  fig = dict(data=data, layout=layout)

  plotly.offline.plot(fig, filename='linechart.html')
  print("Created user last tweet line chart!")
  

#DEFINE WHAT GRAPHS YOU WANT HERE BY CALLING THE FXN
Follow_back();
Default_profile();
User_Lang();
Tweet_Line();