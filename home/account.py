from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from home.models import Item, Request, User


def profile(request):
    username = request.session.get('username', None)
    name = request.session.get('name', None)
    if username:
        open_requests = Request.objects.filter(buyer_username=username, status='Ordered').order_by('-created_time')
        ongoing_requests = Request.objects.filter(buyer_username=username,
                                                  status__in=['Assigned, Shipped, Delivered']).order_by('-created_time')
        completed_requests = Request.objects.filter(buyer_username=username, status='Completed').order_by('-created_time')

        ongoing_purchases = Request.objects.filter(provider_username=username, status='Assigned').order_by('-created_time')
        template = loader.get_template('profile.html')
        context = RequestContext(request, {
            'name': name,
            'open_requests': open_requests,
            'ongoing_requests': ongoing_requests,
            'completed_requests': completed_requests,
            'ongoing_purchases': ongoing_purchases
        })
        return HttpResponse(template.render(context))
    else:
        return HttpResponseRedirect('/')