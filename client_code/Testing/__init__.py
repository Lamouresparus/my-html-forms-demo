from ._anvil_designer import TestingTemplate
from anvil import *


class Testing(TestingTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    # Any code you write here will run before the form opens.
