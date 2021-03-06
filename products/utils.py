import base64

import matplotlib.pyplot as plt
import pylab as pl
import seaborn as sns
from io import BytesIO
from django.contrib.auth.models import User
def get_salesman_from_id(val):
    salesman = User.objects.get(id=val)
    return salesman



def get_image():
    # create a byte buffer
    buffer = BytesIO()
    # create a plot using BytesIO object as its file
    plt.savefig(buffer, format='png')
    # set the cursor the beginning of the stream
    buffer.seek(0)
    # retrieve  the entire content of the 'file'
    image_png = buffer.getvalue()

    graph = base64.b64encode(image_png)
    # print(graph)
    graph = graph.decode('utf-8')

    # free the memory of the buffer
    buffer.close()

    return graph


def get_simple_plot(chart_type, *args, **kwargs):
    # https://matplotlib.org/2.0.2/faq/usage_faq.html#what-is-a-backend
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(10, 4))
    x = kwargs.get('x')
    y = kwargs.get('y')
    data = kwargs.get('data')
    # df = kwargs.get('df')
    if chart_type == 'bar plot':
        title = "Total price by day(bar)"
        pl.title(title)
        plt.bar(x, y)
    elif chart_type == 'line plot':
        title = "Total price by the day(line)"
        pl.title(title)
        plt.plot(x, y)
    else:
        title = "Times item sold by the item(count)"
        pl.title(title)
        sns.countplot("name", data=data)
    plt.xticks(rotation=45)
    plt.tight_layout()

    graph = get_image()
    return graph
