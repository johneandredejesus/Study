from force_type import  force_type

@force_type
def plus(value: int, value2 : int):

    return value + value2

class  Test:

    @force_type
    def plus(self,value: int, value2 : int):

        return value + value2

def main():
    
    result = plus(value=2, value2=4) # Accepts the correct type, in this case int.
    print(f'The result is: {result}')
    
    result = plus(value='2', value2=4) # Don't Accepts the incorrect type, in this case string.
    print(f'The result is: {result}')
    

    test = Test()

    result = test.plus(value=2, value2=4) # Accepts the correct type, in this case int.
    print(f'The result is: {result}')
    
    result = test.plus(value='2', value2=4) # Don't Accepts the incorrect type, in this case string.
    print(f'The result is: {result}')

if __name__ == '__main__':
    main()

