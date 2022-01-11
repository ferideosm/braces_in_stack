from collections import deque

class Stack:

    def __init__(self):        
        self.data = deque()        

    @property
    def size(self):
        return len(self.data)

    @property
    def isEmpty(self):
        return not bool(self.data)

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

def checkbalance(value_str):
    
    open_elements_list = ['[', '{', '(']
    closing_elements_list = [']', '}', ')']

    if value_str:
        stack = Stack()
       
        for char in value_str:
            if char in open_elements_list:
                stack.push(open_elements_list.index(char))
            elif char in closing_elements_list:
                if not stack.isEmpty and stack.peek() == closing_elements_list.index(char):
                    stack.pop()
                else:
                    return print(f'Последовательность {value_str} - не верная')

        return print(f'Последовательность {value_str} - верная')

    return f'Строка пустая проверка баланса невозможна'

if __name__ == "__main__":
    checkbalance('(((([{}]))))')
    checkbalance('[([])((([[[]]])))]{()}')
    checkbalance('{{[()]}}')
    checkbalance('}{}')
    checkbalance('{{[(])]}}')
    checkbalance('[[{())}]')

