# 1. Add models for student, subject and student_subject from previous lessons in SQLAlchemy.
# 2. Find all students` name that visited 'English' classes.
# 3. (Optional): Rewrite queries from the previous lesson using SQLAlchemy.

from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date, ForeignKey 
from sqlalchemy.sql import func

Base = declarative_base()

class Client(Base):
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    role = Column(String(50), nullable=False)

    
class Room(Base):
    __tablename__ = 'room'

    id = Column(Integer, primary_key=True)
    host_id = Column(Integer, ForeignKey('client.id'), nullable=False)
    amount_of_residents = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    a_c = Column(Boolean, nullable=False)
    fridge = Column(Boolean, nullable=False)
    reservation_fee = Column(Integer, nullable=False)

class Reservation(Base):
    __tablename__ = 'reservation'

    id = Column(Integer, primary_key=True)
    guest_id = Column(Integer, ForeignKey('client.id'), nullable=False)
    room_id = Column(Integer, ForeignKey('room.id'), nullable=False)
    check_in = Column(Date, nullable=False)
    check_out = Column(Date, nullable=False)
    status = Column(String(50), nullable=False)




class Reviews(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    guest_id = Column(Integer, ForeignKey('client.id'), nullable=False)
    room_id = Column(Integer, ForeignKey('room.id'), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(String(250), nullable=False)


from sqlalchemy import create_engine

DATABASE_URI = 'postgresql://{user}:{password}@{host}:{port}/{database}'


engine = create_engine(
    DATABASE_URI.format(
        host='localhost',
        database='postgres',
        user='d.poberezhnyi',
        password='password',
        port=5432,
    )
)



from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

session = Session()

guest = session.query(Client).first()

query = session.query(Client.id, Client.name) \
    .join(Reservation, Client.id == Reservation.guest_id) \
    .group_by(Client.id, Client.name) \
    .order_by(func.count(Reservation.id).desc()) \
    .limit(1)


result = query.first()

print(result)


