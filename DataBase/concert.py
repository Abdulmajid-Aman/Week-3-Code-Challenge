from __init__ import CONN, CURSOR
from venue import Venue
from band import Band

class Concert:

    all = {}

    def __init__(self, date, band_id, venue_id, id =None):
        self.id = id
        self.date = date
        self.band_id = band_id
        self.venue_id = venue_id
        type(self).all[self.id] = self
    
    @property
    def band_id(self):
        return self._band_id
    
    @band_id.setter
    def band_id(self, value):
        if type(value) is int:
            self._band_id = value
        else:
            raise TypeError("Band ID must be an integer.")
        
    @property
    def venue_id(self):
        return self._venue_id
    
    @venue_id.setter
    def venue_id(self, value):
        if type(value) is int:
            self._venue_id = value
        else:
            raise TypeError("Venue ID must be an integer.")
        

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if type(date) is str:
            self._date = date
        else:
            raise TypeError("Date must be a string")
        

    
    @classmethod
    def create_table(cls):
        sql = """ 
        CREATE TABLE IF NOT EXISTS concerts (
            id INTEGER PRIMARY KEY ,
            date TEXT,
            band_id INTEGER,
            venue_id INTEGER,
            FOREIGN KEY (band_id) REFERENCES bands(id),
            FOREIGN KEY (venue_id) REFERENCES venues(id)
        )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """ DROP TABLE IF EXISTS concerts """
        CURSOR.execute(sql)
        CONN.commit()

    def band(self):
        sql = """ 
        SELECT * FROM bands WHERE id = ? 
        """
        band = CURSOR.execute(sql, (self.band_id,)).fetchone()
        if band:
            band.name = band[1]
            band.hometown = band[2]
        else:
            band = Band(band[1], band[2])
            band.id = band[0]
            Band.all[band.id] = band
        return band
    

    def venue(self):
        sql = """ 
        SELECT * FROM venues WHERE id = ? 
        """
        venue = CURSOR.execute(sql, (self.venue_id,)).fetchone()
        if venue:
            venue.city = venue[1]
            venue.title = venue[2]
        else:
            venue = Venue(venue[1], venue[2])
            venue.id = venue[0]
            Venue.all[venue.id] = venue
        return venue
    

    def hometown(self):

        sql = """ SELECT 1 FROM concerts INNER JOIN  bands ON concerts.band_id = bands.id, INNER JOIN bands ON concerts.venue_id = venues.id WHERE self.id = ?AND bands.hometown = venues.city"""

        concert = CURSOR.execute(sql, (self.id,)).fetchone()

        if concert:
            return True
        else:
            return False
        

    def introduction(self):
        sql = """ SELECT bands.name, venues.city, bands.hometown FROM concerts INNER JOIN bands ON concerts.band_id = bands.id INNER JOIN venues ON concerts.venue_id = venues.id WHERE concerts.id = ? """

        concert = CURSOR.execute(sql, (self.id,)).fetchone()

        return f'Hello {concert[1]}!!!!! We are {concert[0]} and we\'re from {concert[2]}'
