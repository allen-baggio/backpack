from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from home.models import Item, Request, User


def profile(request):
    """
    List all status of orders both as a customer and a traveller of the user
    :param request:
    :return:
    """
    username = request.session.get('username', None)
    name = request.session.get('name', None)
    if username:
        # Requests
        open_requests = Request.objects.filter(buyer_username=username, status='Ordered').order_by('-created_time')
        assigned_requests = Request.objects.filter(buyer_username=username,status='Assigned').order_by('-created_time')
        shipped_requests = Request.objects.filter(buyer_username=username, status='Shipped').order_by('-created_time')
        delivered_requests = Request.objects.filter(buyer_username=username, status='Delivered').order_by('-created_time')
        completed_requests = Request.objects.filter(buyer_username=username, status='Completed').order_by('-created_time')

        # Purchases
        assigned_purchases = Request.objects.filter(provider_username=username, status='Assigned').order_by('-created_time')
        shipped_purchases = Request.objects.filter(provider_username=username, status='Shippped').order_by('-created_time')
        delivered_purchases = Request.objects.filter(provider_username=username, status='Delivered').order_by('-created_time')
        completed_purchases = Request.objects.filter(provider_username=username, status='Completed').order_by('-created_time')

        template = loader.get_template('profile.html')
        context = RequestContext(request, {
            'name': name,
            'open_requests': open_requests,
            'assigned_requests': assigned_requests,
            'shipped_requests': shipped_requests,
            'delivered_requests': delivered_requests,
            'completed_requests': completed_requests,
            'assigned_purchases': assigned_purchases,
            'shipped_purchases': shipped_purchases,
            'delivered_purchases': delivered_purchases,
            'completed_purchases': completed_purchases
        })
        return HttpResponse(template.render(context))
    else:
        return HttpResponseRedirect('/login')
