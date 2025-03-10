<h1 align="center">CONTRIBUTING</h1>

Welcome to the contributing guidelines for Biscuit. This document will help you get started with contributing to Biscuit.

### Setting up Environment

[**Fork**](https://docs.github.com/en/get-started/quickstart/fork-a-repo) the Biscuit repository and clone locally. 
```bash
git clone http://github.com/billyeatcookies/biscuit
```
Run `pip install -r requirements.txt` or `poetry install`, your preference. Try to launch biscuit once with `python -m biscuit` and make sure everything looks good.

> [!NOTE]
> [Python](https://python.org/en/download/) 3.10 or above


# Project Structure
The codebase of Biscuit is divided into 3 main parts:
- **/biscuit**: Main codebase of the App.
- **/tests**: unit tests for Biscuit (WIP).
- **/docs**: documentation for Biscuit (WIP).

Please make sure to follow the [PEP8](https://www.python.org/dev/peps/pep-0008/) style guide.

# /biscuit

- `/config`: configuration files for the app (WIP).
- `/core`: the core codebase of the app.
- `/extensions`: extensions directory.
- `/res`: icon fonts, bitmaps, images, etc.

Main interest here is in the `/core` directory. 

- `/core/components`: all components of app such as editors, git, extension manager, views and floating views such as menu, notifications and palette, etc.
- `/core/layout`: the GUI structure, statusbar, menubar, editor-view-terminal managers, etc.
- `/core/utils`: keyboard shortcuts, events manager, etc.
- `/core/settings`: preferences, configuration manager, settings editor, themes, etc.


# The App class

Main point of having this class is to have a single point of access to all the important parts of the app. 

> [!IMPORTANT]  
> **This class holds reference to all the components of Biscuit and every class of biscuit have a reference to this `base` class**

- Example: Accessing the active editor instance from Foo class of biscuit: 
    ```py
    class Foo:
        ...
        def foo(self):
            editor = self.base.editorsmanager.active_editor 
            if (editor.content and editor.content.exists):
                print(editor.path)
                if (editor.content.editable):
                    self.base.notifications.info(":)")
    ```

- Example: Accessing the menubar from Foo class of biscuit:
    ```py
    class Foo:
        ...
        def foo(self):
            filemenu = self.base.menubar.file_menu
            filemenu.add_item("this", lambda: print("Wah"))

            xyzmenu = self.base.menubar.add_menu("Wah")
            xyzmenu.add_item("stuff", lambda: print("Wah"))
    ```
