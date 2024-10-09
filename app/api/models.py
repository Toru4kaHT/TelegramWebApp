from sqlalchemy import String, BigInteger, Integer, Date, Time, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
import enum


class User(Base):
    __tablename__ = 'users'

    # Основные данные пользователя

    telegram_id: Mapped[int] = mapped_column(BigInteger,
                                             primary_key=True)
    first_name: Mapped[str] = mapped_column(String, nullable=False)
    username: Mapped[str] = mapped_column(String, nullable=True)

    # Связь с заяваками (Один ко многим)

    applications: Mapped[list["Application"]] = relationship(back_populates='user')

class Master(Base):
    __tablename__ = 'masters'

    # Основыне данные мастеров

    master_id: Mapped[int] = mapped_column(BigInteger, primary_key=True,
                                           autoincrement=True)
    master_name: Mapped[str] = mapped_column(String, nullable=False)

    # Связь с заявками (Один ко многим)

    applications: Mapped[list["Application"]] = relationship(back_populates='master')

class Service(Base):
    __tablename__ = 'services'

    service_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)

    service_name: Mapped[str] = mapped_column(String, nullable=False,
                                              autoincrement=True)
    
    # Связь с заявками (у одной услуги может быть несколько заявок)

class Application(Base):
    __tablename__ = 'applications'

    class GenderEnum(enum.Enum):
        male = 'Мужской'
        female = 'женский'