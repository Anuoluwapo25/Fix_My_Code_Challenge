#!/usr/bin/python3
"""
Module: square
Takes two arguments, casts them to integers and computes the sum
Returns an integer: the sum of 'a' and 'b'
"""


class Square:
    """
    Class representing a square.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a Square object.

        Keyword Arguments:
        *args: Additional positional arguments (not used).
        **kwargs: Additional keyword arguments to set attributes.
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """
        Calculate the area of the square.

        Returns:
        int: The area of the square.
        """
        return self.width * self.width

    def perimeter_of_my_square(self):
        """
        Calculate the perimeter of the square.

        Returns:
        int: The perimeter of the square.
        """
        return 4 * self.width

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
        str: String representation in the format "width/height".
        """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
