from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from home.models import Item, Request, User
from datetime import datetime


def index(request):
    session = request.session
    if session:
        name = session.get('name', None)
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'name': name,
        'request_created': False
    })
    print 'hello'
    return HttpResponse(template.render(context))


def login(request):
    session = request.session
    if session:
        name = session.get('name', None)
    template = loader.get_template('login.html')
    context = RequestContext(request, {
        'name': name
    })
    return HttpResponse(template.render(context))


def logout(request):
    session = request.session
    if session:
        session['name'] = None
    return HttpResponseRedirect('/')


def authenticate(request):
    username = request.POST['username']
    password = request.POST['password']
    print username
    user = User.objects.raw("select email, name, password from home_user where email = %s", [username])
    print user
    if not list(user) or password != user[0].password:
        template = loader.get_template('login.html')
        context = RequestContext(request, {
            'error': True
        })
        return HttpResponse(template.render(context))
    else:
        request.session['username'] = username
        request.session['name'] = user[0].name
        return HttpResponseRedirect('/')


def register(request):
    email = request.POST['email']
    phone = request.POST['phone']
    password = request.POST['password']
    name = request.POST['name']
    user = User(email=email, phone=phone, password=password, name=name)
    user.save()
    request.session['username'] = name
    return HttpResponseRedirect('/')


def load_request(request):
    template = loader.get_template('request.html')
    context = RequestContext(request, {
        'name': request.session.get('name', None)
    })
    return HttpResponse(template.render(context))


def create_request(request):

    username = request.session['name']

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
    request_id = hash(username) + hash(now)
    print request_id
    order_request = Request(id=str(request_id), buyer_username=request.session['username'], item=item, quantity=item_quantity, created_time=now)
    order_request.save()
    template = loader.get_template('request.html')
    context = RequestContext(request, {
        'name': username,
        'item': item,
        'request': order_request,
        'request_created': True
    })
    return HttpResponse(template.render(context))

