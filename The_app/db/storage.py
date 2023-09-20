"""
Module for handling database operations.

This module provides functions for initializing the database and establishing connections.
"""

from models.basemodel import Base
import sqlite3

def get_db_connection():
    """
    Purpose: one
    """
    conn = sqlite3.connect('blog.db')
    conn.row_factory = sqlite3.Row
    return conn


def init_user():
    """
    Purpose: initializes the users
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR NOT NULL,
            email VARCHAR NOT NULL,
            password VARCHAR NOT NULL,
            post_id INTEGER,
            Foreign Key (post_id) REFERENCES posts(id)
        );
        '''
    )


def init_post():
    """
    Purpose: initializes the posts
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            topic VARCHAR NOT NULL
        );
        '''
    )