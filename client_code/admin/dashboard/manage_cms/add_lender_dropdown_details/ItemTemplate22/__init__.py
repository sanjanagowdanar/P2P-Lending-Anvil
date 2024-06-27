from ._anvil_designer import ItemTemplate22Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ItemTemplate22(ItemTemplate22Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    """This method is called when the link is clicked"""
    item_data = self.item
    open_form('admin.dashboard.manage_cms.add_lender_dropdown_details.edit_salary_type', selected_row=item_data)
    
