from sqlalchemy import Column , Boolean , Integer , String , ForeignKey
from sqlalchemy.orm import relationship
from db import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key= True ,index=True )
    email = Column(String, unique= True , index=True)
    user_name = Column(String, unique= True , index=True)
    fist_name = Column(String)
    last_name = Column(String)
    hash_password  = Column(String)
    is_active = Column(Boolean, default = True)

    task = relationship('Todos', back_populates= 'owner')


class Todos(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key= True ,index=True )
    title = Column(String)
    description = Column(String)
    priority  = Column(Integer)
    complete  = Column(Boolean, default = False)
    owner_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship('Users', back_populates='task')



