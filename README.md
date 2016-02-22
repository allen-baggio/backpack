# backpack

Steps to connect MySQL database:
1. Set up DATABASE in backpack/settings.py
2. Create tables in MySQL

    home_user:

    Field       Type        Null    Key Default Extra
    email       varchar(10) NO      PRI NULL
    password    varchar(45) NO          NULL
    phone       varchar(45) NO      UNI NULL
    name        varchar(45) NO          NULL

    home_item:

    Field   Type        Null    Key Default Extra
    id      int(11)     NO      PRI NULL    auto_increment
    name    varchar(45) YES         NULL
    type    varchar(45) YES         NULL
    country varchar(45) YES         NULL

    home_request:

    Field               Type        Null    Key Default Extra
    id                  varchar(45) NO      PRI NULL
    buyer_username      varchar(45) YES         NULL
    item_id             varchar(45) YES         NULL
    quantity            int(11)     YES         NULL
    created_time        datetime    YES         NULL
    provider_username   varchar(45) YES         NULL
    status              varchar(45) YES         NULL
    delivery_time       datetime    YES         NULL
    price               int(11)     YES         NULL

    home_itinerary:

    Field               Type        Null    Key Default Extra
    id                  int(11)     NO      PRI NULL    auto_increment
    provider_username   varchar(45) YES         NULL
    country             varchar(45) YES         NULL
    return_date         date        YES         NULL
    created_time        datetime    YES         NULL