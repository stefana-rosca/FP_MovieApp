class film:
    def __init__(self, titlu, an, nota, actori, pret):
        self.titlu = titlu
        self.an = an
        self.nota = nota
        self.actori = actori
        self.pret = pret

    def adaugare_film(self, titlu, an, nota, actori, pret):
        """Funktion welche Filme in einen File hinzufugt.

                    Man soll Titel, Jahr, Note, Schauspielern und Preis des Filmes geben.
                    Jahr, Note, Preis = Int
                    Titel, Schauspielern = String
                    Mehrere Schauspielern sollten mit ' , ' getrennt werden.
                """
        self.titlu = titlu
        self.an = an
        self.nota = nota
        self.actori = actori
        self.pret = pret
        return self

    def adaugare_in_fisier(self):
        f = open("filme.txt", 'a')
        f.write('\n' + self.titlu + "/" + str(self.an) + "/" + str(self.nota) + "/" + str(
            self.pret) + "/," + self.actori + ",")

    def modificare_pret(self, key, new_price):
        """Funktion wird den Preis des Filmes aktualisieren.
            Man gebe den Titel fur den Film und den neuen Preis.
            Preis wird in File aktualisiert.
        """
        with open("filme.txt", 'r') as f:  # modificam si in fisier
            lines = f.readlines()
        with open("filme.txt", 'w') as f:
            for line in lines:
                line_sep = line.split('/')
                if line_sep[0] != key:
                    f.write(line)
                if line_sep[0] == key:
                    f.write(
                        line_sep[0] + "/" + line_sep[1] + "/" + line_sep[2] + "/" + str(new_price) + "/" + line_sep[4])

    def afisare_filme(self, list):
        """Funktion wird die Liste mit allen Filme zeigen.
            Sie bekommt keinen Input.
            Output = Liste von Filme
                """
        with open("filme.txt", 'r') as f:  # modificam si in fisier
            lines = f.readlines()
            for line in lines:
                line_sep = line.split('/')
                list.append(
                    line_sep[0] + " " + line_sep[1] + " " + line_sep[2] + " " + str(line_sep[3]) + " " + line_sep[4] + "\n")
        return list

    def extragere_filme(self, list):
        """Funktion wird die Liste mit allen Filme zeigen.
            Sie bekommt keinen Input.
            Output = Liste von Filme
                """
        with open("filme.txt", 'r') as f:  # modificam si in fisier
            lines = f.readlines()
            for line in lines:
                line_sep = line.split('/')
                list.append(line_sep[0])
        return list