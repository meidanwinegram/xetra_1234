"""Custom Exceptions"""

class WrongFormatException(Exception):
    """
    WrongFormatException class

    Exception that can raised when the format type
    given as parameter is not correct.
    """

class WrongMetaFileException(Exception):
    """
    WrongMetaFileException class

    Exception that can be raised when the meta file
    format is not correct
    """