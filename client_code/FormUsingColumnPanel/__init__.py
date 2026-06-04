from ._anvil_designer import FormUsingColumnPanelTemplate
from anvil import *

class FormUsingColumnPanel(FormUsingColumnPanelTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        super().__init__(**properties)

        # Any code you write here will run before the form opens.
