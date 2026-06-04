from ._anvil_designer import CustomComponentTemplate
from anvil import *


class CustomComponent(CustomComponentTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        super().__init__(**properties)

        # Any code you write here will run before the form opens.

    @property
    def text(self):
        return self.dom_nodes['text'].innerText

    @text.setter
    def text(self, value):
        self.dom_nodes['text'].innerText = value