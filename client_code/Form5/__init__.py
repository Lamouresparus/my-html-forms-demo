from ._anvil_designer import Form5Template
from anvil import *

class Form5(Form5Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    # Any code you write here will run before the form opens.
