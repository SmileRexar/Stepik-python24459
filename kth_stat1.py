def kth_stat(iterable, m):
    """
    Compute m elements in iterable
    >>> kth_stat([2, 45, 5, 0], 1)
    0
    
    >>> kth_stat([i for i in range(100) if i %3==0], 4)
    9
    """
    return sorted(iterable)[m-1]
 
def calc_elements(a: int, b:int, operation:str):
    """
    Check add/sum
    >>> calc_elements(10, 2, 'add')
    12
    
    >>> calc_elements(10, 2, 'sub')
    8
    
    >>> calc_elements(10, 2, 'muldf')
    Traceback (most recent call last):
    Exception: Unknown operation
    >>> calc_elements(10, 0, 'div')
    Traceback (most recent call last):
    ZeroDivisionError: division by zero

    """
    
    if(operation == 'add'):
        return a+b
    if(operation == 'div'):
        return a/b
    if(operation == 'mul'):
        return a*b
    if(operation == 'sub'):
        return a-b 
    
    else:
        raise Exception("Unknown operation")
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    
 '''
 python.exe -m doctest kth_stat.py
 '''