from __init__ import CONN, CURSOR
from venue import Venue
from band import Band
from concert import Concert
import ipdb



Venue.create_table()
Band.create_table()
Concert.create_table()

ipdb.set_trace()