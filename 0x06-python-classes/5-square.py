#!/usr/bin/python3

'''
    class Square is initialize size
'''

class Square:
    '''
    initialize a size
    '''
    def __init__(self, size=0):
        '''
        Args:
            size(int): square
        '''
        if not type(size) is int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise  ValueError('size must be >= 0')
        self.size = size

    def area(self):
        '''
            returns area
        '''
        return self.__size * self.__size

    @property
    def size(self):
        '''
            returns size
        '''
        return self.__size
    
    @size.setter
    def size(self, value):
        '''
            Args:
                value(int) sets value
        '''
        if not type(value) is int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise  ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        '''
            returns with character
        '''
        if self.__size == 0:
            print('')
        else: 
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#',end='')
                print('')