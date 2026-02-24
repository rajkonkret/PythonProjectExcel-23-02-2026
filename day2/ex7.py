import openpyxl
from openpyxl.chart import Reference, BarChart
from openpyxl.chart.axis import ChartLines
from openpyxl.chart.layout import Layout, ManualLayout

filename = 'video2.xlsx'
wb = openpyxl.load_workbook(filename)
ws = wb['Total Sales by Genre']

# dane do wyjresu
values = Reference(ws,
                   min_col=2,
                   max_col=2,
                   min_row=1,
                   max_row=13)

cats = Reference(ws,
                 min_col=1,
                 max_col=1,
                 min_row=2,
                 max_row=13)

# tworzenie wykresu
chart = BarChart()
chart.add_data(values, titles_from_data=True)
chart.set_categories(cats)

chart.title = "Total Sales"
chart.x_axis.title = "Genre"
chart.y_axis.title = "Total SAles by Genre"

# więcej miejsca po lewej i na dole (etykiety osi)
chart.layout = Layout(
    manualLayout=ManualLayout(
        x=0.06,  # <- lewy "padding" (więcej miejsca na Y labels)
        y=0.08,  # <- górny margines
        w=0.70,  # <- szerokość plot area (mniejsza = więcej paddingu)
        h=0.78   # <- wysokość plot area (mniejsza = więcej miejsca na X labels)
    )
)
chart.y_axis.majorUnit = 200

chart.x_axis.delete = False
chart.y_axis.delete = False

chart.y_axis.majorGridlines = ChartLines()
chart.y_axis.tickLblPos = "low"
chart.y_axis.number_format = '0'

chart.x_axis.majorGridlines = ChartLines()

ws.add_chart(chart, 'D2')

wb.save(filename)
wb.close()
