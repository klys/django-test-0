from django.http import HttpResponse
from datetime import datetime
import json

def test(request):
    return HttpResponse('<h1>this is a test</h1>')

def time(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Current Time: {now}'.format(now=now))

def debug_test(request):
    import pdb; pdb.set_trace();
    return HttpResponse('check terminal')

def get(request):
    """Sort integers splitted by comma, example: get?numbers=10,50,60,40 """
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status' : 'ok',
        'numbers' : sorted_ints,
        'message' : 'Integers sorted successfully.'
    }
    return HttpResponse(
        json.dumps(data), 
        content_type='application/json'
        )


def path_test(resquest, name, age):
    """Return a greetings"""
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}! Welcome to the Djungle!'.format(name)
    return HttpResponse(message)
