from ._anvil_designer import BlankPanelFormTemplate
from anvil import *


class BlankPanelForm(BlankPanelFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    # Any code you write here will run before the form opens.
