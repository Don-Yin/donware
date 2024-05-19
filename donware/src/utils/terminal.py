from rich import print
import shutil


def banner(content: str, symbol: str = "-") -> None:
    """
    Print a banner to the terminal with the given content centered and padded with the specified symbol.

    Parameters:
    content (str): The text to be displayed in the banner.
    symbol (str): The character used to pad the content to the terminal width. Default is '-'.

    Example:
    >>> banner("hello world")
    ---- hello world ----
    """
    terminal_width, _ = shutil.get_terminal_size()
    content = " " + content.strip() + " "
    content = content.center(terminal_width, symbol)
    print(content)
