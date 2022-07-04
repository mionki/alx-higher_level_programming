"""Defines an inherited list class MyList."""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))

def main():
    p = MyList()
    p.append(1,3,4,5)
    p.print_sorted()

            
