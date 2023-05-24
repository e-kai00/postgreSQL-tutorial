from sqlalchemy import(
    create_engine, Column, Float, ForeignKey, Integer, String
)

# we're not going to create tables, but instead, we'll be creating Python classes.
# These Python classes will subclass the declarative_base, meaning that
# any class we're making will extend from the main class within the ORM.
    
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from our localhost "chinook" db
db = create_engine("postgresql://postgres:<pass>@localhost/chinook")
base = declarative_base()


# create a class-based model for the "Artist" table
class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)

# create a class-based model for the "Album" table
class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))

# create a class-based model for the "Track" table
class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.Album.Id"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


# instead connecting directly to the db we will ask for a sessio
# create a new instnce of the session maker, then point to our session (the db)
Session = sessionmaker(db)
# open the actual session by calling the Session() subclass defined above
session = Session()

# create the database using declarative_base subclass
base.metadata.create_all(db)


# Query 1 - select all records from the "Artist" table
# artists = session.query(Artist)
# for artist in artists:
    # print(artist.ArtistId, artist.Name, sep=" | ")

    # Query 2 - select "Name" records from the "Artist" table
    # print(artist.Name)


# Query 3 - select "Queen" from the "Artist" table
# artist = session.query(Artist).filter_by(Name="Queen").first()
# print(artist.ArtistId, artist.Name, sep=" | ")
   

# Query 4 - select "ArtistId" #51 from the "Artist" table
# artist = session.query(Artist).filter_by(ArtistId=51).first()
# print(artist.ArtistId, artist.Name, sep=" | ")
    

# Query 5 - select albums with "ArtistId" #51 on the "Album" table
# albums = session.query(Album).filter_by(ArtistId=51)
# for album in albums:
#     print(album.AlbumId, album.Title, album.ArtistId, sep=" | ")
    

# Query 6 - select tracks where the composer is "Queen" from the "Traks" table
tracks = session.query(Track).filter_by(Composer="Queen")
for track in tracks:
    print(
        track.TrackId, track.Name, track.AlbumId, track.MediaTypeId, track.GenreId, 
        track.Composer, track.Milliseconds, track.Bytes, track.UnitPrice, sep=" | "
        )