import shelfBase as sh

""" NOTES !!!!!!
Why this janky setup, with the string definitions of python functions?
Why this, when the shelfButton works fine with a function reference?
The function references don't work with more than 1 Maya instance, that's why.
This is so artists can have more than one instance of Maya open and still have
the shelf rebuild itself correctly in each instance.
"""

apex_Button = """
import Assets
reload(Assets)

import Assets.Exporters.apex as apex
reload(apex)
    
apex.ui.create()
"""

class apexShelf(sh.shelfBase):

    def build(self):
        self.addButton("apex", "yarnYellow.png", command=apex_Button)

apexShelf(name="apex")