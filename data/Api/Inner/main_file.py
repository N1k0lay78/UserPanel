from data.user import User
from data import db_session


def raise_error(error, session=None):
    if session:
        session.close()
    return {"error": error}, 1


def check_admin_status(email, need_status=1):
    admin, session = check_admin(email)
    if type(admin) is dict:
        return admin, session
    if admin.status < int(need_status):
        return raise_error("У вас недостаточно прав для этого", session)
    return admin, session


def check_admin(email):
    session = db_session.create_session()
    user = session.query(User).filter(User.email == email).first()
    if not user:
        return raise_error(f"Админ {email} не найден", session)
    return user, session


def check_params(admin_email, args=None, params=None, status=0):
    if params is not None:
        if not all(key in args and args[key] is not None for key in params):
            return raise_error("Отсутствуют важные параметры")
    return check_admin_status(admin_email, status)
