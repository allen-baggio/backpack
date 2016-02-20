__author__ = 'leguan'
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from home.models import Itinerary
import datetime


def load_itinerary(request):
    template = loader.get_template('itinerary.html')
    context = RequestContext(request, {
        'name': request.session.get('name', None)
    })
    return HttpResponse(template.render(context))


def create_itinerary(request):
    if not request.session.get('username'):
        template = loader.get_template('login.html')
        context = RequestContext(request)
    else:
        country = request.POST.get('country', '')
        return_day = request.POST.get('day', '')
        return_month = request.POST.get('month', '')
        return_year = request.POST.get('year', '')
        if return_day and return_month and return_year:
            return_date = datetime.date(int(return_year), int(return_month), int(return_day))
        else:
            return_date = datetime.date.today()
        itinerary = Itinerary(provider_username=request.session['username'], country=country,
                              return_date=return_date, created_time=datetime.datetime.now())
        itinerary.save()
        template = loader.get_template('itinerary.html')
        context = RequestContext(request, {
            'name': request.session.get('name'),
            'itinerary': itinerary,
            'itinerary_created': True
        })
    return HttpResponse(template.render(context))
