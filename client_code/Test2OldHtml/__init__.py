from ._anvil_designer import Test2OldHtmlTemplate
from anvil import *


class Test2OldHtml(Test2OldHtmlTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    # Any code you write here will run before the form opens.
