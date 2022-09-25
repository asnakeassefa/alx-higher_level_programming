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
    '''
        positioning
    '''
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value):

        '''
            Args:
                value gets the position
        '''

        if not type(value[0]) is int and type(value[1]) is int:
            raise TypeError('position must be a tuple of 2 positive integers')       
        self.__position = value
        
    def my_print(self):
        '''
            returns with character
        '''
        if self.__size == 0:
            print('')
        else:
            print('\n' * self.__position[1],end="")
            for i in range(self.__size):
                print(' ' * self.__position[0], end="")
                for j in range(self.__size):
                    print('#',end='')
                print('')
