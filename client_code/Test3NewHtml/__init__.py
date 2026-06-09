from ._anvil_designer import Test3NewHtmlTemplate
from anvil import *


class Test3NewHtml(Test3NewHtmlTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    # Any code you write here will run before the form opens.
