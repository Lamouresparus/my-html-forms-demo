from ._anvil_designer import FormUsingHtmlTemplate
from anvil import *

class FormUsingHtml(FormUsingHtmlTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        super().__init__(**properties)

        # Any code you write here will run before the form opens.

    @handle("button_1", "click")
    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        alert("Hello, world")
