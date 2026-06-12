from ._anvil_designer import Form7Template
from anvil import *

class Form7(Form7Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    # Any code you write here will run before the form opens.
