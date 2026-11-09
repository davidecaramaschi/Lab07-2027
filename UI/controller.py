import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    # TODO
    def popola_dropdown(self):
        biblioteche = self._model.get_biblioteche()
        generi = self._model.get_generi()

        self._view.dd_biblioteca.options.clear()
        self._view.dd_genere.options.clear()

        self._view.dd_biblioteca.options.append(
            ft.dropdown.Option(key="nessuno", text="Nessun filtro")
        )

        self._view.dd_genere.options.append(
            ft.dropdown.Option(key="nessuno", text="Nessun filtro")
        )

        for biblioteca in biblioteche:
            self._view.dd_biblioteca.options.append(
                ft.dropdown.Option(
                    key=str(biblioteca.id),
                    text=biblioteca.nome
                )
            )

        for genere in generi:
            self._view.dd_genere.options.append(
                ft.dropdown.Option(genere)
            )

        self._view.dd_biblioteca.value = "nessuno"
        self._view.dd_genere.value = "nessuno"

        self._view.update()

    # CALLBACKS DROPDOWN

    # TODO
    def on_biblioteca_change(self, e):
        if e.control.value == "nessuno":
            self.biblioteca_selezionata = None
        else:
            self.biblioteca_selezionata = e.control.value

    def on_genere_change(self, e):
        if e.control.value == "nessuno":
            self.genere_selezionato = None
        else:
            self.genere_selezionato = e.control.value

    # AZIONE: MOSTRA LIBRI
    # TODO
    def mostra_libri(self, e):
        self._view.lv_libri.controls.clear()

        libri = self._model.get_libri_filtrati(
            self.biblioteca_selezionata,
            self.genere_selezionato
        )

        if not libri:
            self._view.show_alert(
                "Nessun libro trovato con i filtri selezionati."
            )
            self._view.update()
            return

        for libro in libri:
            self._view.lv_libri.controls.append(
                ft.Text(str(libro))
            )

        self._view.update()

