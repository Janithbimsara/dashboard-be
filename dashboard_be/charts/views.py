from rest_framework.decorators import api_view
from rest_framework.response import Response
import random
import datetime

# Line chart data
@api_view(['GET'])
def line_chart_data(request):
    labels = [f'Day {i}' for i in range(1, 11)]
    data = [random.randint(10, 100) for _ in range(10)]
    return Response({'labels': labels, 'data': data})

# Bar chart data
@api_view(['GET'])
def bar_chart_data(request):
    labels = ['Product 1', 'Product 2', 'Product 3']
    data = [random.randint(20, 200) for _ in range(3)]
    return Response({'labels': labels, 'data': data})

# Pie chart data
@api_view(['GET'])
def pie_chart_data(request):
    labels = ['Section A', 'Section B', 'Section C']
    data = [random.randint(5, 25) for _ in range(3)]
    return Response({'labels': labels, 'data': data})

# Candlestick chart data
@api_view(['GET'])
def candlestick_chart_data(request):
    data = []
    for i in range(10):
        open_price = random.randint(100, 200)
        close_price = open_price + random.randint(-10, 10)
        high = max(open_price, close_price) + random.randint(5, 15)
        low = min(open_price, close_price) - random.randint(5, 15)
        data.append({
            'x': (datetime.datetime.now() - datetime.timedelta(days=i)).isoformat(),
            'open': open_price,
            'high': high,
            'low': low,
            'close': close_price,
        })
    return Response({'data': data})
