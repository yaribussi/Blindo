
class FileAudio:
    name = ""
    idButton = 0

    #costruttore oggetto file con campi nome file, id del pulsante associato
    def __init__(self, name, idButton):
        self.name=name
        self.idButton=idButton

    #getter e setter del file
    def get_name(self):
        return self.name

    def set_name(self, newname):
        self.name = newname

    def get_id(self):
        return self.idButton

    def setId(self, id):
        self.idButton = id




