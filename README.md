# PyMenu
The new library for making beautiful menus on numworks with dynamic accent colors. Thanks to [cent20's library, menu.py](https://my.numworks.com/python/cent20/menu), for inspiring me for this library.

To give a little aspect, [here is a demo script](https://my.numworks.com/python/zetamap/pymenu_demo) showing the options menu of my [game snake_lite](https://my.numworks.com/python/zetamap/snake_lite).


## How to use
This is simple, you just need to create an instance of ``Menu`` class and set menu title, menu confirm label, and options, like this : 
```python
menu = Menu(
  "My Title",  # Replace by your menu title (e.g. "Game Options")
  "Close menu",  # Replace by your menu confirm label (e.g. "Start Game")
  [  # And here is the options of menu. 
     #Must be formatted like this: ["<option label>", "<default value>", <values...>],
    ["My option", 0, "value 1", 2, [0,1]],
])
```
**Note:** The default option value must be an index of the list of values, not the value itself.

And after, just open the menu like this: 
```python
menu.open()
```
This will automatically clear the screen, format and display options, add a scrollbar if list exceed **6 options per page**, handle keys to move through the menu, clear again the screen at end and return the result of selected options. <br>
You can open the menu as many times you want by recalling the function, the last selected option will be automatically focused.

When you navigating through the menu, you can press **EXE** or **OK** to reset value of selected option. <br>
To validate the menu, press **EXE** or **OK** on the action label, this will return selected values for options, in a simple list without the option label. Also to cancel the menu, press **BACK**, **BACKSPACE** or press **EXE** or **OK** on the arrow at the top left, this will return an empty list, so you can handle that to open another menu if you wish.


## To go further...
You can change all colors of menu, the palette is stored in this variable : ``Menu.colors``, and formatted like this:
  0) Default font color in darkmode or the background color in light mode.
  1) Background color in darkmode or the default font color in light mode.
  2) Font color for not selected options values.
  3) Accent color for focused option value.
  4) Font color for menu title.

There is also an hidden feature. You can automatically switch between light and dark mode by adding an option named “darkmode” with “enabled”/“disabled” as values. <br>
And when user will change its value, the background and fonts colors will be changed.

Selected options values can be obtained without reopening the menu, by calling the method ``.options()`` of your menu object. If the menu has never opened, this will return default values.

The function ``accent_colors()`` has been created to get the accent and background colors for most common OSes. You can copy it for your own scripts if you want.


## Limitations
There are some limitations with labels, to avoid text overlaps. <br>
The title is limited to **25 characters**, the confirm action to **28 characters**, options label to **12 characters**, options value to **15 characters**, and multi-lines labels are not allowed, this will break the menu. <br>
**Note:** A convertion is done for options label and values, so you don't need to convert it to string before. <br>


## Public Content
**wait_key()**: 
* Parameters: ``k...``
* Description: Wait for one of specified keys to be pressed and released.

**accent_colors()**: 
* Parameters: *no parameters*
* Description: Return accent color and background color according to most common OSes.

**Menu()**:
* Parameters: ``title``, ``action``, ``options...``
* Description: Create a menu, with a ``title``, an ``action`` name to confirm the menu, and the list of ``options``. <br>Options must be formatted like this: ``["<label>", <default option>, [option values ...]],``
* Note: The default option value must be an index of the list of values, not the value itself.

**Menu.open()**:
* Parameters: *no parameters*
* Description: Open the menu and display everything beautifully =).

**Menu.close()**:
* Parameters: *no parameters*
* Description: Close the menu, so clear the screen and return selected options values.

**Menu.options()**:
* Parameters: *no parameters*
* Description: Return the list of selected options values (without the option label, just value), or default values if the menu has never been opened.
