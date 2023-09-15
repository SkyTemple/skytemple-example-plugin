from __future__ import annotations

from typing import List, Optional

from skytemple.core.abstract_module import AbstractModule
from skytemple.core.item_tree import ItemTree, ItemTreeEntryRef
from skytemple.core.open_request import OpenRequest
from skytemple.core.rom_project import RomProject


class ExamplePluginModule(AbstractModule):
    """
    This is the entry-point of your plugin.
    """

    rom_project: RomProject

    def __init__(self, rom_project: RomProject):
        """
        Your plugin gets passed in the RomProject when it is created.
        This is your primary way to interact with the game and other modules.
        """
        self.rom_project = rom_project

    @classmethod
    def depends_on(cls) -> List[str]:
        """
        This returns a list of modules that your plugin needs. This can be another module or one
        of the built-in modules, which are listed in SkyTemple's setup.py
        (or in the future it's pyproject.toml).

        You can reference these other modules and rely on functionality in them.
        """
        return ["dungeon", "monster"]

    @classmethod
    def sort_order(cls) -> int:
        """
        A number that is used to sort all of the items in the main item tree of the SkyTemple UI.

        Experiment with this until you find a value you are happy with.
        """
        return 0

    def load_tree_items(self, item_tree: ItemTree):
        """
        This is the heart of your plugin (if your plugin's purpose is to show views in the UI.
        You can add new views to the main item tree on the left of SkyTemple's UI here.

        You must implement this, but you can also do just nothing,
        if your UI does not actually provide new views.

        You can also manipulate other items in the item tree, but this is not recommended, since
        it could easily break with updates.
        """

    def handle_request(self, request: OpenRequest) -> Optional[ItemTreeEntryRef]:
        """
        This allows your plugin to handle a request to open something. Your module or other modules
        can send these requests to SkyTemple and SkyTemple will ask all modules whether they can
        handle the request. If your module can handle a request, return an entry you added to the
        item tree.
        Implementing this is optional.
        """
        return None
