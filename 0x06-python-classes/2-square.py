#!/usr/bin/python3

'''
    class Square is initialize size
'''

class Square:
    '''
    Empty Square class
    '''
    def __init__(self, size=0):
        '''
        Arg:
            size(int): square
        '''
        if not type(size) is int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise  ValueError('size must be >= 0')
        self.__size = size