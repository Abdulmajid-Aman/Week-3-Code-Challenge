# Concert Domain Assignment

## Overview

In this assignment, you will be working with a Concert domain consisting of three tables: `Band`, `Venue`, and `Concert`. The relationships between these tables are as follows:

- A `Band` has many `Concerts`.
- A `Venue` has many `Concerts`.
- A `Concert` belongs to both a `Band` and a `Venue`.
- The `Band-Venue` relationship is many-to-many.

**Note:** Sketch your domain on paper or on a whiteboard before starting to code.

**Important:** This assignment does not use SQLAlchemy. Instead, you will write raw SQL queries directly in Python methods to interact with the database.

## Schema

### Tables

1. **bands Table:**
    - `name` (String)
    - `hometown` (String)

2. **venues Table:**
    - `title` (String)
    - `city` (String)

3. **concerts Table:**
    - `id` (Integer, Primary Key, Auto-increment)
    - `band_id` (Integer, Foreign Key to `bands.id`)
    - `venue_id` (Integer, Foreign Key to `venues.id`)
    - `date` (String)

## Migrations

### Initial Setup

Before implementing the methods, set up your database and tables using raw SQL commands. Create migrations for the `concerts` table after creating and migrating the `bands` and `venues` tables.

### Create the `concerts` Table

```sql
CREATE TABLE concerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    band_id INTEGER,
    venue_id INTEGER,
    date TEXT,
    FOREIGN KEY (band_id) REFERENCES bands(id),
    FOREIGN KEY (venue_id) REFERENCES venues(id)
);
