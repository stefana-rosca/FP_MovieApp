class benutzer:
    def __init__(self, nume, prenume, id):
        self.nume = nume
        self.prenume = prenume
        self.id = id

    def adaugare(self,nume,prenume,id):
        self.id=id
        self.nume=nume
        self.prenume=prenume
        return self

    def adaugare_in_fisier(self):
        ok=0
        with open("benutzer.txt", "r") as f:  # citim fisieru
            lines = f.readlines()
            for line in lines:
                line_sep = line.split(' ')
                if line_sep[0] == str(self.id):
                    ok=1
        if ok==0:
            f = open("benutzer.txt", 'a')
            f.write(str(self.id) + " " + self.nume + " " + self.prenume + " <3\n")

    def edit_prenume(self,key,new_name):
        self.prenume=new_name
        with open("benutzer.txt", 'r') as f:  # modificam si in fisier
            lines = f.readlines()
        with open("benutzer.txt", 'w') as f:
            for line in lines:
                line_sep = line.split(' ')
                if line_sep[0] != key:
                    f.write(line)
                if line_sep[0] == key:
                    f.write(str(key) + " " + line_sep[1] + " " + self.prenume + " " + "<3\n")

    def stergere_user(self,key):
        """Funktion welche ein User aus der File wegloscht.

        Man gebe den ID der Person(Int).
        Diese wird geloscht.

        """
        with open("benutzer.txt", "r") as f:  # citim fisieru
            lines = f.readlines()
        with open("benutzer.txt", "w") as f:  # rescriem tot fisieru cu tot ce era mai putin linia cu useru pe care vrem sa il stergem
            for line in lines:
                line_sep = line.split(' ')
                if line_sep[0] != key and line != '\n':
                    f.write(line)

    def afisare_useri(self,list):
        """Funktion welche die Liste mit allen Users aus der File zeigt.

        Keinen Input, nur Output.
        Wenn keinen Output gezeigt wird, dann ist die Liste leer.
        """
        with open('benutzer.txt', 'r') as f:
            lines = f.readlines()
        for line in lines:
            line_sep = line.split(' ')
            if not line:
                break
            list.append(line_sep[0]+" "+line_sep[1]+" "+line_sep[2])
        return list