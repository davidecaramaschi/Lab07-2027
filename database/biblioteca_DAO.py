from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    # TODO
    def get_biblioteche(self):
        conn = DBConnect.get_connection()

        if conn is None:
            return []

        risultato = []

        try:
            cursor = conn.cursor(dictionary=True)

            query = """
                SELECT id, nome, indirizzo
                FROM biblioteca
                ORDER BY nome
            """

            cursor.execute(query)
            righe = cursor.fetchall()

            for riga in righe:
                biblioteca = Biblioteca(
                    id=riga["id"],
                    nome=riga["nome"],
                    indirizzo=riga["indirizzo"]
                )

                risultato.append(biblioteca)

            cursor.close()

        except Exception as e:
            print(f"Errore durante il recupero delle biblioteche: {e}")

        finally:
            conn.close()

        return risultato

