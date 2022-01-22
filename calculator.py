from typing import Union


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Add two numbers.

    Parameters
    ----------
    a : Union[int, float]
        First number.
    b : Union[int, float]
        Second number.

    Returns
    -------
    Union[int, float]
        Sum of a and b.
    """
    return a + b

def multiply(a: Union[float, int], b: Union[float, int])-> Union[float, int]:
    """Returns the product of two numbers.

    Parameters
    ----------
    a : Union[float, int]
        First number.
    b : Union[float, int]
        Second number. 

    Returns
    -------
    Union[float, int]
        Product of a and b.
    """    
    return a*b