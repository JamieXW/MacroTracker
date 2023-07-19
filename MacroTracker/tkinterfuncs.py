"""
File that contains placeholder text functions for adding,
and handling placeholder text in tkinter entry fields.
"""

import tkinter as tk

def add_placeholder_text(entry, text):
    """
    Adds placeholder text to specific entry fields

    Args:
        entry (tkinter.Entry): Entry field widget for placeholder text adding
        text (str): Message for placeholder to display
    """

    entry.insert(0, text)
    entry.bind("<FocusIn>", lambda event: on_entry_focus_in(entry, text))
    entry.bind("<FocusOut>", lambda event: on_entry_focus_out(entry, text))

def on_entry_focus_in(entry, text):
    """
    Handles focus in of an entry field.

    Args: 
        entry (tkinter.Entry): Entry field widget that recieved focus
        text (str): Placeholder text with the entry field
    """

    if entry.get() == text:
        entry.delete(0, tk.END)
        entry.config(foreground="black")

def on_entry_focus_out(entry, text):
    """
    Handles focus out of an entry field.

    Args:
        entry (tkinter.Entry): Entry field widget that loses focus
        text (str): Placeholder text with the entry field
    """

    if entry.get() == "":
        entry.insert(0, text)
        entry.config(foreground="gray")