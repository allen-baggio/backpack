__author__ = 'leguan'


class Customer(object):
    def __init__(self,
                 first_name,
                 last_name,
                 phone,
                 username,
                 password):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.username = username
        self.password = password
        self.id = id(self)

    def update_info(self, new_password):
        self.password = new_password


class Request(object):
    def __init__(self, request):
        self.id = id(self)


class Item(object):
    def __init__(self):
        self.id = id(self)


class Payment(object):
    def __init__(self):
        self.id = id(self)