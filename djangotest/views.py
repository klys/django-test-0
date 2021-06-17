from django.http import HttpResponse
from datetime import datetime

def test(request):
    return HttpResponse('<h1>this is a test</h1>')

def time(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Current Time: {now}'.format(now=now))

def debug_test(request):
    import pdb; pdb.set_trace();
    return HttpResponse('check terminal')

def get(request):
    print(request.GET['numbers'])
    return HttpResponse('get Numbers')