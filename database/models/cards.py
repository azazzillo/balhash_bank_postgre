import datetime

from database.core import Connection

from database.models.accounts import Accounts

class Card:
    """Object from db. Card."""

    id: int
    number: str
    account: Accounts
    cvv: str
    date_end: datetime.datetime
    is_active: bool
    pin: str

    @staticmethod
    def create(
        conn: Connection,
        number:str,
        account_id: Accounts,
        cvv: str,
        date_end: datetime,
        is_active:bool,
        pin:str
    ):
        with conn.cursor() as cur:
            cur.execute(
                f"""
                INSERT INTO cards(
                    number,
                    account_id,
                    cvv,
                    date_end,
                    is_active,
                    pin
                )
                VALUES(
                    '{number}',
                    '{account_id}',
                    '{cvv}',
                    '{date_end}',
                    '{is_active}',
                    '{pin}'
                )"""
            )

    @staticmethod
    def get(
        conn: Connection,
        **kwargs: dict[str,any]
    ) -> 'Card':

        condition: list[str] = []
        for i in kwargs:
            if isinstance(kwargs[i],str):
                condition.append(
                    f"{i}={kwargs[i]}"
                )

            else:
                condition.append(
                    f"{i}='{kwargs[i]}'"
                )
        with conn.cursor() as cur:
            cur.execute(
                f'''
                SELECT * FROM cards
                WHERE {' AND '.join(condition)}
                LIMIT 1
                '''
            )
            print(cur.fetchone())
            return cur.fetchone()
        
    @staticmethod 
    def filtr(
        conn: Connection,
        **kwargs: dict[str,any]
    ) -> 'Card':
        condition: list[str] = []
        for i in kwargs:
            if isinstance(kwargs,str):
                condition.append(
                    f"{i}={kwargs[i]}"
                )
            else:
                condition.append(
                    f"{i}='{kwargs[i]}'"
                )
        with conn.cursor() as cur:
            cur.execute(
                f'''
                SELECT * FROM cards
                WHERE {' AND '.join(condition)}
                '''
            )
            print(cur.fetchall())
            return(cur.fetchall())
