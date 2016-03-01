from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from home.models import Item, Request, User
from datetime import datetime


def load_request(request):
    """
    Landing page to load a new request
    :param request: HTTP request
    :return:
    """
    template = loader.get_template('request.html')
    context = RequestContext(request, {
        'name': request.session.get('name', None),
    })
    return HttpResponse(template.render(context))


def create_request(request):
    """
    Customer to create a new request
    :param request: HTTP request
    :return:
    """
    username = request.session['username']
    item_type = request.POST.get('item_type', '0')
    item_name = request.POST.get('item_name', '')
    item_country = request.POST.get('item_country', '')
    item_quantity = int(request.POST.get('item_quantity', '1'))
    existing_item = Item.objects.filter(name=item_name, country=item_country)
    if not existing_item:
        item = Item(name=item_name, country=item_country,
                    type=item_type)
        item.save()
    else:
        item = existing_item[0]
    now = datetime.now()
    # request id is the last 20 digits of username and timestamp hash
    request_id = "".join([str(hash(username)), str(now.microsecond)])[-20:]
    order_request = Request(id=request_id, buyer_username=username, item=item,
                            quantity=item_quantity, created_time=now)
    order_request.save()
    template = loader.get_template('request.html')
    context = RequestContext(request, {
        'item': item,
        'request': order_request,
        'request_created': True,
        'name': request.session['name']
    })
    return HttpResponse(template.render(context))


def take_request(request, request_id):
    """
    Traveller to take a request
    :param request: HTTP request
    :param request_id: order request id
    :return:
    """
    username = request.session.get('username')
    if not username:
        return HttpResponseRedirect('/')
    order_request = Request.objects.get(id=request_id)
    if order_request:
        template = loader.get_template('detail.html')
        context = RequestContext(request, {
            'order_request': order_request,
            'name': request.session.get('name', None)
        })
        return HttpResponse(template.render(context))


def assign_request(request, request_id):
    """
    Assign a request to traveller
    :param request: HTTP request
    :param request_id: order request id
    :return:
    """
    username = request.session.get('username')
    if not username:
        return HttpResponseRedirect('/')

    order_request = Request.objects.get(id=request_id)
    order_request.provider_username = username
    order_request.status = 'Assigned'
    order_request.save()

    template = loader.get_template('request.html')
    context = RequestContext(request, {
        'name': request.session.get('name', None),
        'request': order_request,
        'request_assigned': True
    })
    return HttpResponse(template.render(context))


def cancel(request, request_id):
    """
    Customer to cancel a request
    :param request:
    :param request_id:
    :return:
    """
    username = request.session.get('username')
    cancel_request = Request.objects.get(id=request_id)
    if cancel_request.buyer_username != username:
        return HttpResponseRedirect('/')
    cancel_request.status = 'Canceled'
    cancel_request.save()
    return HttpResponseRedirect('/account/profile')


def ship(request, request_id):
    """
    Traveller to ship a order
    :param request:
    :param request_id:
    :return:
    """
    username = request.session.get('username')
    shipped_request = Request.objects.get(id=request_id)
    if shipped_request.provider_username != username:
        return HttpResponseRedirect('/')
    else:
        shipped_request.status = 'Shipped'
        shipped_request.save()
        return HttpResponseRedirect('/account/profile')


def deliver(request, request_id):
    """
    Traveller to deliver and complete a order
    :param request:
    :param request_id:
    :return:
    """
    username = request.session.get('username')
    completed_request = Request.objects.get(id=request_id)
    if completed_request.provider_username != username:
        return HttpResponseRedirect('/')
    else:
        completed_request.status = 'Completed'
        completed_request.save()
        return HttpResponseRedirect('/account/profile')


def complete(request, request_id):
    """
    Customer to confirm a order, order is completed
    :param request:
    :param request_id:
    :return:
    """
    username = request.session.get('username')
    completed_request = Request.objects.get(id=request_id)
    if completed_request.buyer_username != username:
        return HttpResponseRedirect('/')
    else:
        completed_request.status = 'Completed'
        completed_request.save()
        return HttpResponseRedirect('/account/profile')