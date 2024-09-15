#!/usr/bin/python3
"""
Contains the class DBStorage
"""
import model
from model.BaseMachine import Base
from model.Scooter import Scooter
from model.Motor import Motor
from model.Bike import Bike
from model.user import User
# from model.CalendarDate import CalendarDate
from model.Reservation import Reservation
from model.Customer import Customer
# from os import getenv
# import sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
# from sqlalchemy import select, update, delete, values


classes = {"Scooter": Scooter, "Motor": Motor, "Bike": Bike,"Reservation": Reservation, "Customer": Customer, "User": User}

class DBStorage:
    """
    interacts with the MySQL database
    """
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        Location_TVM_MYSQL_USER = "root" # getenv('Location_TVM_MYSQL_USER')
        Location_TVM_MYSQL_PWD = "" # getenv('Location_TVM_MYSQL_PWD')
        Location_TVM_MYSQL_HOST = "localhost" # getenv('Location_TVM_MYSQL_HOST')
        Location_TVM_MYSQL_DB = "location_tvm_dev_db"# getenv('Location_TVM_MYSQL_DB')
        # Location_TVM_ENV = getenv('Location_TVM_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(Location_TVM_MYSQL_USER,
                                             Location_TVM_MYSQL_PWD,
                                             Location_TVM_MYSQL_HOST,
                                             Location_TVM_MYSQL_DB))
        # self.__session = Session(self.__engine)
        # if Location_TVM_ENV == "test":
        #     Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        query on the current database session
        """
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss: 
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    # key = obj.__class__.__name__ + '.' + obj.id
                    key = obj.__class__.__name__ + '.' + str(obj.id)
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """
        add the object to the current database session
        """
        # print("neww hna")
        self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current database session
        """
        # self.__session.reload()
        self.__session.commit()

    def delete(self, obj= None): # , obj2= None
        """delete from the current database session obj if not None"""
        if obj:
            # print("test")
            # print(obj)
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """reloads data from the database"""
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(session_factory)

    def close(self):
        """
        call remove() method on the private session attribute
        """
        self.__session.remove()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values(): # classes.keys()
            # print(cls)
            # print(classes.keys())
            # print(classes.values())
            return None
        # print("test is in class")
        # all_cls = self.all(cls)

        # Query the database for the object by `id`
        try:
            # Use filter_by to find the object by its ID field
            obj = self.__session.query(cls).filter_by(id=id).first()
            return obj  # Return the object if found
        except Exception as e:
            print(f"Error retrieving {cls.__name__} with ID {id}: {e}")
        
        return None

    def get_user(self, cls, email):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """

        if cls not in classes.values(): # classes.keys()
            print(cls)
            # print(classes.keys())
            # print(classes.values())
            return None
        # l'problem hna hwa ana entre c'est un String and for query is a class
        # Query the database for the object by `id`
        try:
            # Use filter_by to find the object by its ID field
            obj = self.__session.query(cls).filter_by(email=email).first()
            return obj  # Return the object if found
        except Exception as e:
            print(f"Error retrieving {cls.__name__} with ID {email}: {e}")
        
        return None

    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for i in all_class:
                count += len(model.storage.all(i).values())
        else:
            count = len(model.storage.all(cls).values())

        return count