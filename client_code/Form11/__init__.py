from ._anvil_designer import Form11Template
from anvil import *


class Form11(Form11Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    # Any code you write here will run before the form opens.
