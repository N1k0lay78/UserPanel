def check_password(password_1: str, password_2: str):
    if len(password_1) > 16:
        return "Пароль больше 16 символов", False
    if len(password_1) < 8:
        return "Пароль меньше 8 символов", False
    if not all([ch in "qwertyuiopasdfghjklzxcvbnm1234567890-_" for ch in password_1.lower()]):
        return "Пароль состоит не только из символов английского алфавита и чисел, а так же символов -_", False
    if not any([ch in password_1.lower() for ch in "qwertyuiopasdfghjklzxcvbnm"]):
        return "В пароле нет символов английского алфавита", False
    if not any([ch in password_1.lower() for ch in "1234567890"]):
        return "В пароле нет цифр", False
    if password_1 != password_2:
        return "Пароли не совпадают", False
    return "", True


if __name__ == '__main__':
    print("Start testing")
    if check_password("aaaabbbb111122223", "aaaabbbb111122223")[1]:
        print("Error in check max length of password")
    if check_password("aaaabb1", "aaaabb1")[1]:
        print("Error in check min length of password")
    if check_password("aaaabb1!b", "aaaabbb")[1]:
        print("Error in check correct chars")
    if check_password("1234567890", "1234567890")[1]:
        print("Error in check alpha chars")
    if check_password("aaaabbbb", "aaaabbbb")[1]:
        print("Error in check number chars")
    if check_password("aaaabbb1", "aaaabbb2")[1]:
        print("Error in check is equal password chars")
    print("End testing")
