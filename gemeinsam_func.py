class comanda1:
    def __init__(self, id, total, filme):
        self.id=id
        self.total=total
        self.filme=filme
    def preluare_comanda(self,id,lista):
        """Funktion welche Bestellungen von den Usern bekommt.
            Man soll den ID des Users fur wem man bestellt gibt.
            Man schreibt die Titel von der Filme und trennt sie mit einen 'Enter' voneinander.
            Wen die Bestellung fertig ist, soll man die Taste 'v' drucken, damit man die Bestellung befertigt.

        return: In den File comenzi.txt werden wir sehen auf jeder Zeile eine Bestellung mit den Total zu bezahlen am Ende.
        """
        self.id=id
        ok=0
        with open("benutzer.txt", 'r') as f:  # modificam in fisier
            lines = f.readlines()
            for line in lines:
                line_sep = line.split(' ')
                if line_sep[0] == str(self.id):
                    ok = 1
                    id_om=line_sep[0]
                    nume_om=line_sep[1]
                    prenume_om=line_sep[2]
        if ok==1:
            f=open("comenzi.txt",'a')
            f.write(id_om + "," + nume_om + "," + prenume_om + ",")
            optiune=1
            total=0
            for film in lista:
                with open("filme.txt", 'r') as f:
                    lines = f.readlines()
                    for line in lines:
                        line_sep=line.split('/')
                        if line_sep[0] == film:
                                total = total + int(line_sep[3])
            f=open("comenzi.txt",'a')
            for film in lista:
                f.write(film+" ")
            f.write(str(total)+",\n")

    def afisare_comenzi(self,list):
        """
        Funktion welche die Liste mit den aktuellen Bestellungen zeigt.
        Keinen Input, nur Output.
        """
        with open("comenzi.txt",'r') as f:
            lines = f.readlines()
            for line in lines:
                line_sep = line.split(',')
                list.append(line_sep[0] + " " + line_sep[1] + " " + str(line_sep[3]) + " " + str(line_sep[4]))
        return list

    def cautare_actori(self,l, actor):
        """Funktion welche ein gemeinsames Schauspieler in der Liste mit Filme sucht.
            Input: Name des Schauspielers
            Output: Titel der Filme in welche dieser Schauspieler gespielt hat.
            Wenn Output = leer, dann gibt es keine Filme mit diesen Schauspielern.
        """
        l=[]
        with open("filme.txt",'r') as f:
            lines=f.readlines()
            for line in lines:
                line_sep=line.split('/')
                titlu = line_sep[0] #titlu filmului de pe fiecare linie
                line_sep = line.split(',') #lista de actori din fiecare film
                n = len(line_sep) - 1
                i = 1
                while i < n: #parcurg lista de actori, daca il gasesc, il adaug la lista pe care o afisez
                    if line_sep[i] == actor:
                        l.append(titlu)
                    i+=1
            return l

    def cautare_nota(self,l,nota):
        """Funktion welche Filme sucht, deren Note grosser als ein gegebenes Wert sei.
        Input = Note
        Output = Filme welche die Note grosser als die gegebene sind.
        Wenn Output = leer, dann gibt es keine solche Filme.
        """
        l = []
        with open("filme.txt", 'r') as f:
            lines = f.readlines()
            for line in lines:
                line_sep = line.split('/')
                titlu = line_sep[0]  # obtin titlu filmului de pe fiecare linie
                if float(line_sep[2]) >= float(nota):
                    l.append(titlu)
            return l