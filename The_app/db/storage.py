"""
Module for handling database operations.

This module provides functions for initializing the database and establishing connections.
"""

import sqlite3


def get_db_connection():
    """
    Establishes a connection to the SQLite database.

    Returns:
        sqlite3.Connection: A connection to the database.
    """
    conn = sqlite3.connect('blog.db')
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """
    Initializes the database by creating necessary tables if they don't exist.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY,
            title TEXT,
            content TEXT,
            author TEXT,
            date_posted TEXT,
            topic TEXT
        )
    ''')

    conn.commit()
    conn.close()
