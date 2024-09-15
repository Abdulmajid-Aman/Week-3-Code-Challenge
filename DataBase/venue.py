from __init__ import CURSOR, CONN

class Venue:

    all = {}

    def __init__(self, title, city, id = None):
        self.id = id
        self.title = title
        self.city = city
        type(self).all[self.id] = self
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if type(title) is str:
            self._title = title
        else:
            raise ValueError('Title must be a string')
        

    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, city):
        if type(city) is str:
            self._city = city
        else:
            raise ValueError('City must be a string')
        
    @classmethod
    def create_table(cls):
        sql = """ CREATE TABLE IF NOT EXISTS venues(id INTEGER PRIMARY KEY, city TEXT, title TEXT) """


        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """ DROP TABLE IF EXISTS venues """

        CURSOR.execute(sql)
        CONN.commit()


    def concerts(self):
        from concert import Concert

        sql = """ SELECT * FROM concerts WHERE venue_id = ? """

        venues = CURSOR.execute(sql, (self.id,)).fetchall()

        return [venue for venue in venues] if venues else None
    
    def concert_on(self, date):
        from concert import Concert

        sql = """ SELECT * FROM concerts WHERE concerts.date = ? AND  venue_id = ? """

        concert = CURSOR.execute(sql, (date, self.id)).fetchone()

        return concert
    
    def bands(self):
        from venue import Venue
        sql = """ SELECT self.name FROM bands INNER JOIN venue ON venue.id = bands.id WHERE bands.id = ?"""

        bands = CURSOR.execute(sql, (self.id,)).fetchall()
        return [band for band in bands] if bands else None
    


    def most_frequent_band(self):
        sql = """
        SELECT bands.name
        FROM concerts
        INNER JOIN bands ON concerts.band_id = bands.id
        WHERE concerts.venue_id = ?
        GROUP BY bands.id
        ORDER BY COUNT(concerts.id) DESC
        LIMIT 1
        """
        result = CURSOR.execute(sql, (self.id,)).fetchone()
        if result:
            return result[0]
        return None