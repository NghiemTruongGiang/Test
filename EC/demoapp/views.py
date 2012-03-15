# Create your views here.
from django.http import HttpResponse
from django.template import Context, Template
import datetime
from mysite.demoapp.forms import ContactForm

def contact(request):
    form = ContactForm()
    fp = open('C:\Users\KingDraGon\Desktop\mysite\demoapp\contact.html')
    t = Template(fp.read())
    fp.close()
    html = t.render(Context({'form': form}))
    return HttpResponse(html)
def current_datetime(request):
    now = datetime.datetime.now()
    fp = open('C:\Users\Saiury\Desktop\mysite\demoapp\hello.html')
    t = Template(fp.read())
    fp.close()
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)
