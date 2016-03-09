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
    index = int(request.GET.get('startIndex', 0))
    if username:
        # Requests
        order_requests = Request.objects.filter(buyer_username=username).order_by('-created_time')

        # Purchases
        order_purchases = Request.objects.filter(provider_username=username).order_by('-created_time')

        template = loader.get_template('profile.html')
        context = RequestContext(request, {
            'name': name,
            'requests': order_requests[index: index + 10],
            'requests_page_size': range(0, len(order_requests)/10 + 1),
            'purchases': order_purchases[index: index + 10],
            'purchases_page_size': range(0, len(order_purchases)/10 + 1)
        })
        return HttpResponse(template.render(context))
    else:
        return HttpResponseRedirect('/login')
