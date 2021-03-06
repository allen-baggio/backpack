from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from home.models import Item, Request, User, Itinerary
from django.db.models import Q

import datetime
import re


def index(request):
    """
    Landing page for the website
    :param request:
    :return:
    """
    session = request.session
    if session:
        name = session.get('name', None)
    existing_requests = Request.objects.filter(status='Ordered').order_by('-created_time')[:3]
    today = datetime.date.today()
    existing_itineraries = Itinerary.objects.filter(return_date__gte=today).order_by('return_date')[:3]
    print existing_itineraries
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'name': name,
        'request_created': False,
        'existing_requests': existing_requests,
        'existing_itineraries': existing_itineraries
    })
    return HttpResponse(template.render(context))


def login(request):
    """
    User login
    :param request:
    :return:
    """
    session = request.session
    if session:
        name = session.get('name', None)
        username = session.get('username', None)
    template = loader.get_template('login.html')
    context = RequestContext(request, {
        'name': name,
        'username': username
    })
    return HttpResponse(template.render(context))


def signup(request):
    session = request.session
    if session:
        name = session.get('name', None)
        username = session.get('username', None)
    template = loader.get_template('signup.html')
    context = RequestContext(request, {
        'name': name,
        'username': username
    })
    return HttpResponse(template.render(context))


def logout(request):
    """
    User logout
    :param request:
    :return:
    """
    session = request.session
    if session:
        session['name'] = None
        session['username'] = None
    return HttpResponseRedirect('/')


def authenticate(request):
    """
    User authenticate
    :param request:
    :return:
    """
    username = request.POST['username']
    password = request.POST['password']
    user = User.objects.raw("select email, name, password from home_user where email = %s", [username])
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
    """
    User sign up
    :param request:
    :return:
    """
    email = request.POST['email']
    phone = request.POST['phone']
    password = request.POST['password']
    name = request.POST['name']
    template = loader.get_template('signup.html')
    email_match = re.match(r'([^@]+)@([a-z0-9]+)\.([a-z]+)', email)
    if not email_match:
        context = RequestContext(request, {
            'email_error': True
        })
        return HttpResponse(template.render(context))
    phone_match = re.match(r'[0-9].', phone)
    if not phone_match:
        context = RequestContext(request, {
            'phone_error': True
        })
        return HttpResponse(template.render(context))
    if len(password) < 6:
        context = RequestContext(request, {
            'password_error': True
        })
        return HttpResponse(template.render(context))
    existing_user = User.objects.filter(Q(email=email) | Q(phone=phone))
    if existing_user:
        context = RequestContext(request, {
            'dulpicate_error': True
        })
        return HttpResponse(template.render(context))
    user = User(email=email, phone=phone, password=password, name=name)
    user.save()
    request.session['username'] = email
    request.session['name'] = name
    return HttpResponseRedirect('/')


def search(request):
    """
    User search for existing request
    :param request:
    :return:
    """
    keyword = request.GET.get('q', None)
    name = request.session['name']
    if keyword:
        items = Item.objects.filter(name__icontains=keyword)
        item_ids = []
        for item in items:
            item_ids.append(item.id)
        results = Request.objects.filter(item_id__in=item_ids)
    else:
        results = None
    template = loader.get_template('search.html')
    context = RequestContext(request, {
        'name': name,
        'results': results
    })
    return HttpResponse(template.render(context))


def faq(request):
    template = loader.get_template('faq.html')
    return HttpResponse(template.render())


