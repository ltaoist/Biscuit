import tkinter as tk

from biscuit.core.components.utils import Frame, IconButton


class BaseGame(Frame):
    """
    Base class for games.
    """
    def __init__(self, master, path=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.config(**self.base.theme.editors)
        self.path = path
        self.filename = None

        self.exists = False
        self.showpath = False
        self.diff = False
        self.editable = False        
        
        self.__buttons__ = (('refresh', self.reload), )

    def create_buttons(self, editorbar):
        self.__buttons__ = [IconButton(editorbar, *button) for button in self.__buttons__]

    def reload(self, *_):
        ...    
        
    def save(self, *_):
        ...
