from app.observers.isubject import ISubject

class SensorSubject(ISubject):
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SensorSubject, cls).__new__(cls)
            cls._instance._observers = []
        return cls._instance
    def attach(self, observer):
        self._observers.append(observer)
    def detach(self, observer):
        self._observers.remove(observer)
    def notify(self, data: dict):
        for o in self._observers:
            o.update(data)