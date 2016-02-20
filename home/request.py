from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from home.models import Item, Request, User
from datetime import datetime


def load_request(request):
    template = loader.get_template('request.html')
    name = request.session.get('name', None)
    context = RequestContext(request, {
        'name': request.session.get('name', None),
    })
    return HttpResponse(template.render(context))


def create_request(request):
    username = request.session['username']
    print username
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
    request_id = "".join([str(hash(username)), str(now.microsecond)])[-20:]
    print 'request id: ', request_id
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


def confirm_request(request, request_id):
    order_request = Request.objects.get(id=request_id)
    if order_request:
        template = loader.get_template('detail.html')
        context = RequestContext(request, {
            'order_request': order_request,
            'name': request.session.get('name', None)
        })
        return HttpResponse(template.render(context))


def assign_request(request, request_id):
    order_request = Request.objects.get(id=request_id)
    username = request.session['username']
    print 'username'
    print username

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
    print request_id
    cancel_request = Request.objects.get(id=request_id)
    cancel_request.status = 'Canceled'
    cancel_request.save()
    return HttpResponseRedirect('/account/profile')