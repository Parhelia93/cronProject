from django.shortcuts import render
from .models import PlcMessage
from bokeh.models import ColumnDataSource, OpenURL, TapTool
from bokeh.plotting import figure
from bokeh.embed import file_html
from bokeh.resources import CDN
from django.urls import reverse
from bokeh.models import BoxAnnotation

def printLastMessage(request):
    lastMessageStack = PlcMessage.objects.all().order_by('-id')[:15]
    context = {'lastMessageStack':lastMessageStack}
    return render(request, 'cronJob/LastMessagePage.html', context=context)


def printMainPage(request):
    return render(request, 'cronJob/mainScreen.html')

def showGraph(request):
    p = figure(plot_width=900, plot_height=500,
               tools="tap", title="Click the Dots")
    # prepare some data
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15]
    y1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    source = ColumnDataSource(data=dict(
        x=[1, 2, 3, 4, 5, 10, 11, 12, 14, 15],
        y=[2, 2, 8, 2, 17, 22, 45, 18, 22, 17],
        color=[125, 126, 127, 128, 129, 130, 131, 132, 133, 134]
    ))

    p.circle('x', 'y', color='red', size=10, source=source)
    #p.line('x', 'y', color="navy", line_width=1, source=source)
    p.line(x, y1, legend_label="Temp.", color="blue", line_width=2)

    low_box = BoxAnnotation(top=10, fill_alpha=0.2, fill_color="#F0E442")
    mid_box = BoxAnnotation(bottom=10, top=20, fill_alpha=0.2, fill_color="#009E73")
    high_box = BoxAnnotation(bottom=20, fill_alpha=0.2, fill_color="#F0E442")

    p.add_layout(low_box)
    p.add_layout(mid_box)
    p.add_layout(high_box)

    taptool = p.select(type=TapTool)


    sttr = reverse('currentPoint',args=('color',))

    sttr = sttr.replace('color', '@color')

    taptool.callback = OpenURL(url=sttr, same_tab=True)

    html = file_html(p, CDN, 'my_plot')
    return render(request, 'cronJob/showGraph.html',{'html1':html})


def currentPoint(request, numPoint):
    return render(request, 'cronJob/CurrentPoint.html', {'numPoint': numPoint})
