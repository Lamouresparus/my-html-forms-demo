from ._anvil_designer import CustomButtonTemplate
from anvil import *


class CustomButton(CustomButtonTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)
    print(self.dom_nodes)
    # Any code you write here will run before the form opens.

  @property
  def text(self):
    return self._text

  @text.setter
  def text(self, value):
    self._text = value
    self.dom_nodes['custom-button-text'].innerText = value

  @property
  def bold(self):
    return self._bold

  @bold.setter
  def bold(self, value):
    self._bold = value
    if value:
      self.dom_nodes['custom-button-text'].style.fontWeight = "bold"
    else:
      self.dom_nodes['custom-button-text'].style.fontWeight = "normal" 