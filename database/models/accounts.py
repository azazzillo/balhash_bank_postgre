import datetime

from database.core import Connection

class Accounts:
    
    ''' Object from db. Accounts.'''
    id: int
    number: str
    owner_id: int
    balance: float
    type: str

    @staticmethod 
    def create(
    conn: Connection,
    number: str,
    owner_id: int,
    balance: float,
    type: str
    ):
        with conn.cursor() as cur:
            cur.execute(f'''
                INSERT INTO accounts(
                    number,
                    owner_id,
                    balance,
                    type)
                VALUES(
                    '{number}',
                    '{owner_id}',
                    '{balance}',
                    '{type}')
                '''
            )
    @staticmethod
    def get(
        conn: Connection,
        **kwargs: dict[str,any]
    ) -> 'Accounts':

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
                SELECT * FROM accounts
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
    ) -> 'Accounts':
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
                SELECT * FROM accounts
                WHERE {' AND '.join(condition)}
                '''
            )
            print(cur.fetchall())
            return(cur.fetchall())
