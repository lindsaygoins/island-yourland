from sqlalchemy import Boolean, Column, Integer, String, text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Art(Base):
    __tablename__ = 'art'

    artid = Column(Integer, primary_key=True, server_default=text("nextval('art_artid_seq'::regclass)"))
    artname = Column(String(255), nullable=False, unique=True)
    arttype = Column(String(255), nullable=False)
    lindsay = Column(Boolean, nullable=False)
    lyrics = Column(Boolean, nullable=False)


class Bug(Base):
    __tablename__ = 'bugs'

    bugid = Column(Integer, primary_key=True)
    bugname = Column(String(255), nullable=False, unique=True)
    location = Column(String(255), nullable=False)
    sellprice = Column(Integer, nullable=False)
    lindsay = Column(Boolean, nullable=False)
    hourstart = Column(Integer, nullable=False)
    hourend = Column(Integer, nullable=False)
    monthstart = Column(Integer, nullable=False)
    monthend = Column(Integer, nullable=False)
    althourstart = Column(Integer)
    althourend = Column(Integer)
    altmonthstart = Column(Integer)
    altmonthend = Column(Integer)


class Diy(Base):
    __tablename__ = 'diys'

    diyid = Column(Integer, primary_key=True, server_default=text("nextval('diys_diyid_seq'::regclass)"))
    diyname = Column(String(255), nullable=False, unique=True)
    diycategory = Column(String(255), nullable=False)
    lindsay = Column(Boolean, nullable=False)
    lyrics = Column(Boolean, nullable=False)


class Fish(Base):
    __tablename__ = 'fish'

    fishid = Column(Integer, primary_key=True)
    fishname = Column(String(255), nullable=False, unique=True)
    location = Column(String(255), nullable=False)
    shadowsize = Column(String(255), nullable=False)
    sellprice = Column(Integer, nullable=False)
    lindsay = Column(Boolean, nullable=False)
    hourstart = Column(Integer, nullable=False)
    hourend = Column(Integer, nullable=False)
    monthstart = Column(Integer, nullable=False)
    monthend = Column(Integer, nullable=False)
    althourstart = Column(Integer)
    althourend = Column(Integer)
    altmonthstart = Column(Integer)
    altmonthend = Column(Integer)


class Flower(Base):
    __tablename__ = 'flowers'

    flowerid = Column(Integer, primary_key=True, server_default=text("nextval('flowers_flowerid_seq'::regclass)"))
    flowername = Column(String(255), nullable=False, unique=True)
    flowerfamily = Column(String(255), nullable=False)
    lindsay = Column(Boolean, nullable=False)


class Saharahitem(Base):
    __tablename__ = 'saharahitems'

    itemid = Column(Integer, primary_key=True, server_default=text("nextval('saharahitems_itemid_seq'::regclass)"))
    itemname = Column(String(255), nullable=False, unique=True)
    itemcategory = Column(String(255), nullable=False)
    rugsize = Column(String(255))
    lindsay = Column(Boolean, nullable=False)
    lyrics = Column(Boolean, nullable=False)


class Seacreature(Base):
    __tablename__ = 'seacreatures'

    seacreatureid = Column(Integer, primary_key=True)
    seacreaturename = Column(String(255), nullable=False, unique=True)
    sellprice = Column(Integer, nullable=False)
    lindsay = Column(Boolean, nullable=False)
    hourstart = Column(Integer, nullable=False)
    hourend = Column(Integer, nullable=False)
    monthstart = Column(Integer, nullable=False)
    monthend = Column(Integer, nullable=False)
    althourstart = Column(Integer)
    althourend = Column(Integer)
    altmonthstart = Column(Integer)
    altmonthend = Column(Integer)
