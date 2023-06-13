#Local
from database.core import Connection

import datetime

#Python
from decouple import config
from database.models.users import User
from database.models.accounts import Accounts
from database.models.cards import Card


my_connection: Connection = Connection(
    host=config('DB_HOST', str),
    port=config('DB_PORT', int),
    user=config('DB_USER', str),
    password=config('DB_PASSWORD', str),
    dbname=config('DB_NAME', str)
)


if __name__ == '__main__':
    my_connection.create_tables()
    # User.create(
    #     conn=my_connection.conn,
    #     first_name='nis',
    #     last_name='yy',
    #     date_of_birth=datetime.datetime(
    #     year=2000,
    #     month=1,
    #     day=3),
    #     iin='180515123334',
    #     phone_number= '9779410034'                  
    # )
    # User.get(
    #     conn=my_connection.conn,
    #     first_name='bob'    
    # )
    # Accounts.create(
    #     conn=my_connection.conn,
    #     number='24345678912345678912',
    #     owner_id=17,
    #     balance=0.0,
    #     types='.eur'
    # )
    # Card.create(
    #     conn=my_connection.conn,
    #     number='1634567891234567',
    #     account_id=4,
    #     cvv='324',
    #     date_end=datetime.datetime(
    #         year=2024,
    #         month=4,
    #         day=6),
    #     is_active=True,
    #     pin='7794'
    # )
    Accounts.filtr(
        conn=my_connection.conn,
        type='.eur'
    )
    # User.get_all(
    #     conn=my_connection.conn
    # )
    # User.filtr(
    #     conn=my_connection.conn,
    #     last_name='yy'
    # )
