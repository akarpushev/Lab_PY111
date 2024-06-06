def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    stack = 0
    for i in brackets_row:
        if i == '(':
            stack += 1
        elif i == ')':
            stack -= 1
        if stack < 0:
            return False
    else:
        return False if stack !=0 else True



    # while '()' in brackets_row:
    #     text = brackets_row.replace('()', '')
    #     return not text



    # TODO реализовать проверку скобочной группы


if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
