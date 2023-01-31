import tkinter as tk

class AboutProgram:

    def __init__(self, root):
        self.root = root

        self.get_form()

    def get_exit(self):
        self.root.destroy()

    def get_form(self):
        '''Application window settings'''

        describe = """Firma Air-Concept Sp. z o.o. z Kruszwicy realizuje projekt badawczo-rozwojowy nrRPKP.01.03.01-04-0001/19, współfinansowany ze środków Europejskiego Funduszu Rozwoju Regionalnego, w ramach poddziałania RPKP.01.03.01.Wsparcie procesów badawczo-rozwojowych w przedsiębiorstwach akademickich, Regionalnego Programu Operacyjnego Województwa Kujawsko-Pomorskiego na lata 2014-2020.

Tytuł: „Działania o charakterze badawczo-rozwojowym nad stworzeniem innowacji produktowej i procesowej w skali światowej związanej z wykorzystaniem bezzałogowego statku powietrznego, z zestawem dedykowanych urządzeń optyczno-analitycznych, do monitorowania szeregu elementów przyrody ożywionej i nieożywionej” Beneficjent: Air-Concept Sp. z o.o.

Cele projektu: Przeprowadzenie zaawansowanych prac B+R w ramach poziomów gotowości technologicznej (III-VIII TRL).

Planowane efekty: Zastosowanie bezzałogowych statków powietrznych i dedykowanych urządzeń optyczno-analitycznych, wraz z zaprojektowanym oprogramowaniem, w analizie stanu środowiska naturalnego i przyrody przez wybrane czynniki zagrożenia.

Wartość ogółem: 1 622 370,00 PLN, Wydatki kwalifikowane: 1 457 000,00 PLN, Dofinansowanie: 1 129 600,00 PLN.

Wkład UE: 1 129 600,00 PLN, Okres realizacji projektu: 01.03.2021 – 28.02.2023r.http://www.air-concept.pl/ """


        self.message = tk.Label(self.root, text="About Program")
        self.mess_box_entry = tk.Text(self.root, width=50, height=18.49, wrap=tk.WORD)
        self.mess_box_entry.insert(tk.END, describe)
        self.mess_box_entry.config(state=tk.DISABLED)

        self.button_exit = tk.Button(self.root, text="Exit", command=self.get_exit)

        self.message.grid(row=3, column=0, columnspan=2, pady=(12, 0))
        self.mess_box_entry.grid(row=4, column=0, columnspan=2, padx=30)
        self.button_exit.grid(row=5, column=0, padx=(150, 50), pady=(10, 10))



