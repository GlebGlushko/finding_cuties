from sqlalchemy import create_engine, Column, String, Float, Integer, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.databases import postgresql
Base = declarative_base()

class View(Base):
  __tablename__ ='views'
  id = Column(Integer, primary_key=True)
  lat = Column('lat', Float)
  lng = Column('lng', Float)
  url = Column('url', String(200))
  def __init__(self, lat, lng, url):
    self.lat=lat
    self.lng=lng
    self.url=url

class Database:
  session: sessionmaker
  def __init__(self, db='postgresql://postgres:Cn0gh0wtyny0@localhost:5432/postgres'):
    engine = create_engine(db)
    Base.metadata.create_all(engine)
    self.session = sessionmaker(bind=engine)()

# kek_view = View(36.6351738, -121.9263157, 'https://maps.googleapis.com/maps/api/streetview?size=1000x600&location=36.6351738,-121.9263157&fov=40&heading=-20&pitch=-15&key=AIzaSyCwdQHf1IAIopaVPF7KefK2SZiDOyMo-_k')
# session.add(kek_view)
# session.commit()
db = Database()

