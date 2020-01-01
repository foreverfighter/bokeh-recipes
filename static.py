import random

import pandas as pd
from bokeh.io.export import export_png
from bokeh.models import ColumnDataSource, Span, Label
from bokeh.models.formatters import NumeralTickFormatter
from bokeh.palettes import all_palettes, Accent8, Spectral4, Spectral6, Inferno3, Inferno6, Inferno7
from bokeh.plotting import figure, show, output_file, output_notebook

data = {
    'periods': ['Q1 17', 'Q2 17', 'Q3 17', 'Q4 17', 'Q1 18', 'Q2 18', 'Q3 18'],
    'gmv': [
        212210.22, 249741.43, 187860.90, 3510028.06, 258004.44, 283408.59,
        403613.27
    ],
    'colors':
    Spectral4 + Spectral4[:3]
}
source = ColumnDataSource(data)
p = figure(
    x_range=data['periods'],
    title="GMV YOY QS",
    plot_width=800,
    plot_height=400,
    toolbar_location=None,
    tools="",
    y_axis_label='Total Gross Merchanise Value',
    y_minor_ticks=None,
)

p.yaxis.formatter = NumeralTickFormatter(format="($ 0.00 a)")
p.axis.major_tick_line_color = None
p.axis.minor_tick_line_color = None
p.ygrid.grid_line_color = '#D8D8D8'
p.xgrid.grid_line_color = None

p.add_layout(
    Span(location=405,
         location_units='screen',
         dimension='height',
         line_color='#B8B8B8'))

p.add_layout(
    Label(x=180,
          y=300,
          x_units='screen',
          y_units='screen',
          text='2017',
          render_mode='css',
          border_line_color=None,
          background_fill_color=None,
          background_fill_alpha=1.0))
p.add_layout(
    Label(x=550,
          y=300,
          x_units='screen',
          y_units='screen',
          text='2018',
          render_mode='css',
          border_line_color=None,
          background_fill_color=None,
          background_fill_alpha=1.0))

p.vbar(x='periods', width=0.5, top='gmv', color='colors', source=source)
#     y_axis_location=,

# output_file("myBokeh.html") with this we can output to a new html file
# output_file('static.html', title='Bokeh Plot')
# export_png(p)
# export_png(p, 'gmv.png', height=600, width=900)

show(p)