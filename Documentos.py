from __future__ import annotations
from abc import ABC, abstractmethod
from xml.dom.minidom import Document

class State(ABC):

    @property
    def context(self) -> Documento:
        return self.documento

    @context.setter
    def context(self, doc: Documento) -> None:
        self.documento = doc


    @abstractmethod
    def render():
        pass

    @abstractmethod
    def publish():
        pass


class Draft(State):

    def render(self):
        return "DRAFT: Texto em estado de Draft | " + str(self.documento)[0:10]

    def publish(self):
        new_state = Moderation()
        new_state.context = self.documento
        self.documento.transition_to(new_state)

class Moderation(State):

    def render(self):
        return "MODERATION: Texto em estado de moderação | " + str(self.documento)[0:20]

    def publish(self):
        new_state = Published()
        new_state.context = self.documento
        self.documento.transition_to(new_state)

class Published(State):

    def render(self):
        return "PUBLISHED: Texto em estado de Draft | " + str(self.documento)

    def publish(self):
        new_state = Draft()
        new_state.context = self.documento
        self.documento.transition_to(new_state)

class Documento():

    def __init__(self, texto):
        self.texto = texto
        self.state = Draft()
        self.state.context = self
    
    def render(self):
        return self.state.render()

    def publish(self):
        self.state.publish()

    def transition_to(self, state):
        self.state = state

    def __str__(self):
        return self.texto

if __name__ == '__main__':
    d = Documento("Eu nunca perco. Ou eu ganho, ou aprendo!")
    print(d.render())
    d.publish()
    print(d.render())
    d.publish()
    print(d.render())

    d.publish()
    print(d.render())
