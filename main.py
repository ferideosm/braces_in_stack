class Stack:

    def __init__(self) -> None:
        self.stack_list = []

    def isEmpty(self) -> bool:
        if self.stack_list:
            return True
        return False 

    def push(self, element):
        self.stack_list.insert(0, element)

    def pop(self):
        if self.isEmpty():
            return self.stack_list.pop(0)
        else:
            return False

    def peek(self):
        if self.isEmpty():
            return self.stack_list[0]
        else:
            return False

    def size(self):
        return len(self.stack_list)

def braces_check(string_):
    # скобки ()
    stack1 = Stack()
    # скобки []
    stack2 = Stack()
    # скобки {}
    stack3 = Stack()

    for element in string_:
        if element == '(':
            stack1.push(element)
        elif element == ')':
            if not stack1.peek():
                return 'Несбалансированно'
            else:
                stack1.pop()

        elif element == '[':
            stack2.push(element)
        elif element == ']':
            if not stack2.peek():
                return 'Несбалансированно'
            else:
                stack2.pop()

        elif element == '{':
            stack3.push(element)
        elif element == '}':
            if not stack3.peek():
                return 'Несбалансированно'
            else:
                stack3.pop()
    if stack1.size() == 0 and stack2.size() == 0 and stack3.size() == 0:
        return 'Cбалансированно'
    else:
        return 'Несбалансированно'

if __name__== "__main__":
    sbal_string_1 = '(((([{}]))))'
    sbal_string_2 = '[([])((([[[]]])))]{()}'
    sbal_string_3 = '{{[()]}}'

    nesbal_string_1 = '}{}'
    nesbal_string_2 = '{{[(])]}}'
    nesbal_string_3 = '[[{())}]'

    print(f'sbal_string_1 - {braces_check(sbal_string_1)}')
    print(f'sbal_string_2 - {braces_check(sbal_string_2)}')
    print(f'sbal_string_3 - {braces_check(sbal_string_3)}')
    print(f'nesbal_string_1 - {braces_check(nesbal_string_1)}')
    print(f'nesbal_string_2 - {braces_check(nesbal_string_2)}')
    print(f'nesbal_string_3 - {braces_check(nesbal_string_3)}')
   