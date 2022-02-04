import sqlalchemy
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash
from data.db_session import SqlAlchemyBase

# print(generate_password_hash("admin123"))


class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'user'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    fullname = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)
    nickname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    image = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    type = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    __mapper_args__ = {
        'polymorphic_on': type,
    }

    def __repr__(self):
        return f'<Person> {self.id} Базовый юзер {self.nickname}'

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
