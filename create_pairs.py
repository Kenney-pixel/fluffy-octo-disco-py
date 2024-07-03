from typing import Set, Tuple, Any

def create_pairs(set1: Set[Any], set2: Set[Any]) -> Set[Tuple[Any, Any]]:
    """
    Create a set of tuples where each tuple contains one element from each of the two input sets.

    Args:
    set1 (Set[Any]): The first input set
    set2 (Set[Any]): The second input set

    Returns:
    Set[Tuple[Any, Any]]: A set of tuples containing pairs of elements from the input sets.
    
    Raises:
    ValueError: If the input sets are not of equal size

    Examples:
    >>> boys = {"John", "Paul", "George"}
    >>> girls = {"Olivia", "Charlotte", "Michelle"}
    >>> result = create_pairs(boys, girls)
    >>> len(result)
    3
    """

    if len(set1) != len(set2):
        raise ValueError("The input sets must be of equal size.")

    return {(a,b) for a,b in zip(set1, set2)}

if __name__=='__main__':
    import doctest
    doctest.testmod()
