from abc import ABC, abstractmethod



class SaveHandler(ABC):
    def __init__(self, filename):
        self.filename = filename

    def save(self):
        pass

class PlainTextSave(SaveHandler):
    def __init__(self, filename, separator):
        pass
    
    def save(self, content):
        with open(self.filename) as f:
            pass


class SQLiteSaveHandler(SaveHandler):
    pass

