import pandas as pd
from math import pi
from datetime import datetime as dt
from bokeh.io import output_file
from bokeh.plotting import show
from bokeh.models import DatetimeTickFormatter
from bokeh.plotting import figure

df = pd.DataFrame(data=[1,2,3],
                  index=[dt(2015, 1, 1), dt(2015, 1, 2), dt(2015, 1, 3)],
                  columns=['foo'])
p = figure(plot_width=400, plot_height=400)
p.line(df.index, df['foo'])
p.xaxis.formatter=DatetimeTickFormatter(
        hours=["%d %B %Y"],
        days=["%d %B %Y"],
        months=["%d %B %Y"],
        years=["%d %B %Y"],
    )
p.xaxis.major_label_orientation = pi/4
output_file('myplot.html')
show(p)