from __init__ import CONN, CURSOR

class Band:

    all = {}

    def __init__(self, name, hometown, id = None):
        self.id = id
        self.name = name
        self.hometown = hometown
        type(self).all[self.id] = self

    @classmethod
    def create_table(cls):
        sql = """ CREATE TABLE IF NOT EXISTS bands(id INTEGER PRIMARY KEY, name TEXT, hometown TEXT) """    

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """ DROP TABLE IF EXISTS bands """

        CURSOR.execute(sql)
        CONN.commit()


    def concerts(self):
        from concert import Concert

        sql = """ SELECT * FROM concerts WHERE band_id = ? """

        concerts = CURSOR.execute(sql, (self.id,)).fetchall()

        return [concert for concert in concerts] if concerts else None
    
    def bands(self):
        from venue import Venue

        bands = [venue for venue in Venue.all]
        return bands
    

    def play_in_venue(self, title, date):
        from venue import Venue
        from concert import Concert

        sql = """ SELECT * FROM venues WHERE venues.title = ? """

        venue = CURSOR.execute(sql, (title,)).fetchone()
        venue_id = venue[0]
        band_id= self.id
        concert_date = date
        concert = Concert(date = concert_date, venue_id = venue_id, band_id = band_id)


        sql_query = """ INSERT INTO concerts(band_id, venue_id, date) VALUE (? ,?, ?)"""

        CURSOR.execute(sql_query, (concert.band_id, concert.venue_id, concert.date))
        CONN.commit()


    def all_introductions(self):
        from venue import Venue

        all_introductions = list()

        sql = """ SELECT venues.city FROM venues"""

        venues = CURSOR.execute(sql).fetchall()
        for city in venues:
            message = f'Hello {city}!!!!! We are {self.name} and we\'re from {self.hometown}'
            all_introductions.append(message)

        return all_introductions
    

    def venues(self):
        from band import Band
        sql = """ SELECT self.name FROM bands INNER JOIN venue ON venues.id = bands.id WHERE venues.id = ?"""

        bands = CURSOR.execute(sql, (self.id,)).fetchall()
        return [band for band in bands] if bands else None

    def most_performances(self):
        sql = """
        SELECT bands.name
        FROM concerts
        INNER JOIN bands ON concerts.band_id = bands.id
        GROUP BY bands.id
        ORDER BY COUNT(concerts.id) DESC
        LIMIT 1
        """
        result = CURSOR.execute(sql).fetchone()
        if result:
            return result[0]
        return None
        