import pymysql

class Repository:

    # metodo per ottenere la connessione al database quando serve
    @staticmethod
    def _get_connection():
        return pymysql.connect(
            host='localhost',
            password="",
            port=3306,
            user="root",
            database="project_work",
        )

    # metodo generico per recupero set di dati singolo (DQL: select)
    def recupero_singolo(self, sql, valori):
        try:
            with self._get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(sql, valori)
                    return cursor.fetchone()
        except Exception as e:
            print(e)
            return "Errore Database"

    # metodo generico per recupero set di dati singolo (DQL: select) (metodo valido anche per future JOIN)
    def recupero_multiplo(self, sql, valori=None):
        # valori è opzionale nel caso in cui voglia fare un select senza where
        try:
            with self._get_connection() as connection:
                with connection.cursor() as cursor:
                    if valori:
                        cursor.execute(sql, valori)
                    else:
                        cursor.execute(sql)
                    return cursor.fetchall()
        except Exception as e:
            print(e)
            return "Errore Database"