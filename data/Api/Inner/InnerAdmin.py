from data import db_session
from data.user import User
from data.Api.Inner.main_file import raise_error, check_params


def check_password(password):  
    errors = {0: 'Пароль должен быть в длину 8 или более символов', 1: 'Пароль должен содержать хотя бы 1 букву',
              2: 'Пароль должен содержать хотя бы 1 цифру'}
    if not len(password) >= 8:
        return raise_error(errors[0])[0]
    if password.isdigit():
        return raise_error(errors[1])[0]
    if password.isalpha():
        return raise_error(errors[2])[0]
    return True


def find_by_id(id, session):
    user = session.query(User).get(id)
    if not user:  
        return raise_error(f"Пользователь не найден", session)
    return user, session


def user_check_password(user_email, password):
    session = db_session.create_session()
    user = session.query(User).filter(User.email == user_email)
    if user and user.check_password(password):
        res = {"success": "Добро пожаловать"}
    else:
        res = {"error": "Неправильный пароль или почта"}
    session.close()
    return res


def get_user(user_email):
    user, session = check_params(user_email)
    if type(user) is dict:
        return user
    data = user.to_dict()
    session.close()
    return data


def get_list_user(user_email):
    user, session = check_params(user_email)  
    if type(user) is dict:  
        return user
    users = session.query(User).all()  
    data = [item.to_dict() for item in users]
    session.close()
    return data


def put_user(user_email, args):  
    user, session = check_params(user_email)
    if type(user) is dict:
        return user
    count = 0  
    user_dict = user.to_dict(only=('fullname', 'email'))
    keys = list(filter(lambda key: args[key] is not None and key in user_dict and args[key] != user_dict[key],
                       list(args.keys())))  
    
    for key in keys:
        count += 1  
        if key == 'email':
            if session.query(User).filter(User.email == args["email"]).first():  
                return raise_error("Этот email уже занят", session)[0]
            user.email = args['email']
        if key == 'fullname':
            user.fullname = args["fullname"]
    if "change_password" in args:  
        if not user.check_password(args["password_1"]):
            return raise_error("Пароль не совпадает с текущим паролем", session)[0]  
        r = check_password(args['password_2'])
        if type(r) is dict:
            return r
        user.set_password(args['password_2'])
        count += 1  
    if count == 0:  
        return raise_error("Пустой запрос", session)[0]
    session.commit()  
    
    session.close()  
    return {"success": f"Ваши личные данные успешно изменены"}


def create_new_user(args):
    session = db_session.create_session()

    if session.query(User).filter(User.email == args["email"]).first():
        return raise_error("Этот email уже занят", session)

    ch = check_password(args["password_1"])
    if type(ch) is dict:
        return ch
    if args["password_1"] != args["password_2"]:
        return raise_error("Пароли не совпадают", session)

    new_user = User()
    new_user.fullname = args["fullname"]
    new_user.nickname = args["nickname"]
    new_user.email = args["email"]
    new_user.set_password(args["password_1"])

    session.add(new_user)
    session.commit()
    new_id = new_user.id
    session.close()

    return {"success": f"Вы успешно зарегистрировались", "id": new_id}
