from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    # TODO
    def get_generi(self):
        conn = DBConnect.get_connection()

        if conn is None:
            return []

        risultato = []
        cursor = None

        try:
            cursor = conn.cursor()

            query = """
                   SELECT DISTINCT genere
                   FROM libro
                   WHERE genere IS NOT NULL
                   ORDER BY genere
               """

            cursor.execute(query)
            righe = cursor.fetchall()

            for riga in righe:
                risultato.append(riga[0])

        except Exception as e:
            print(f"Errore durante il recupero dei generi: {e}")

        finally:
            if cursor is not None:
                cursor.close()

            conn.close()

        return risultato

    def get_libri_filtrati(self, biblioteca, genere):
        conn = DBConnect.get_connection()

        if conn is None:
            return []

        risultato = []
        cursor = None

        try:
            cursor = conn.cursor(dictionary=True)

            query = """
                   SELECT id, titolo, autore, genere,
                          anno_pubblicazione, id_biblioteca
                   FROM libro
                   WHERE (%s IS NULL OR id_biblioteca = %s)
                     AND (%s IS NULL OR genere = %s)
                   ORDER BY titolo
               """

            parametri = (
                biblioteca,
                biblioteca,
                genere,
                genere
            )

            cursor.execute(query, parametri)
            righe = cursor.fetchall()

            for riga in righe:
                libro = Libro(
                    id=riga["id"],
                    titolo=riga["titolo"],
                    autore=riga["autore"],
                    genere=riga["genere"],
                    anno_pubblicazione=riga["anno_pubblicazione"],
                    id_biblioteca=riga["id_biblioteca"]
                )

                risultato.append(libro)

        except Exception as e:
            print(f"Errore durante il recupero dei libri: {e}")

        finally:
            if cursor is not None:
                cursor.close()

            conn.close()

        return risultato

