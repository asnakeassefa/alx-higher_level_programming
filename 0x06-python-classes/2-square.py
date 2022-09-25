#!/usr/bin/python3

#!/usr/bin/python3
'''
empty square classes that defines a square.
'''

from multiprocessing.sharedctypes import Value


class Square:
    '''
    Empty Square class
    '''
    def __init__(self, size=0):
        '''
        Arg size(int): square
        '''
        self.__size = size
        if not type(size) is int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise  ValueError('size must be >= 0')