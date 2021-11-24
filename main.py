
start_stack = []


class Stack:
    #Создание функций по заданию

    def __init__(self, my_stack_: list):
        self.my_stack = my_stack_

    def isEmpty(self) -> bool:
        return True if not self.size() else False

    def push(self, i: str):
        self.my_stack.append(i)

    def pop(self):
        if self.isEmpty():
            return 'Стек пуст'
        else:
            last = self.my_stack[-1]
            del self.my_stack[-1]
            return last

    def peek(self):
        if self.isEmpty():
            return 'Стек пуст'
        else:
            return self.my_stack[-1]

    def size(self):
        return len(self.my_stack)


def chack_balance(list_in: list):

    # Функция принимает набор скобок, проверка на посторонние символы, сбалансированность

    one_dict = {'(': ')', '{': '}', '[': ']'}
    symbols_list = ['(', ')', '[', ']', '{', '}']  # для проверки посторонних символов
    temp = []
    my_stack = Stack(temp)
    for i in list_in:
        if i in symbols_list:
            if my_stack.isEmpty():
                my_stack.push(i)
            else:
                if one_dict.get(my_stack.peek()) == i:
                    my_stack.pop()
                else:
                    my_stack.push(i)
        else:
            print('Символ не является скобкой')

    if my_stack.isEmpty():
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'


def main():
    #  Проверки
    print(chack_balance('()'))
    print(chack_balance('(((([{}]))))'))
    print(chack_balance('[([])((([[[]]])))]{()}'))
    print(chack_balance('{{[()]}}'))
    print()
    print(chack_balance('}{}'))
    print(chack_balance('{{[(])]}}'))
    print(chack_balance('[[{())}]'))


if __name__ == '__main__':
    main()
