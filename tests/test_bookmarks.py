import sqlite3

from src.bookmarks import get_bookmark_by_raw_sql_query


def test_get_bookmark_by_raw_sql_query_returns_row_mapping():
    connection = sqlite3.connect(":memory:")
    connection.execute(
        "CREATE TABLE bookmarks (id INTEGER PRIMARY KEY, url TEXT, title TEXT)"
    )
    connection.execute(
        "INSERT INTO bookmarks (url, title) VALUES (?, ?)",
        ("https://example.com", "Example"),
    )
    connection.commit()

    result = get_bookmark_by_raw_sql_query(
        connection, "SELECT id, url, title FROM bookmarks WHERE url='https://example.com'"
    )

    assert result == {"id": 1, "url": "https://example.com", "title": "Example"}


def test_get_bookmark_by_raw_sql_query_returns_none_when_missing():
    connection = sqlite3.connect(":memory:")
    connection.execute(
        "CREATE TABLE bookmarks (id INTEGER PRIMARY KEY, url TEXT, title TEXT)"
    )
    connection.commit()

    result = get_bookmark_by_raw_sql_query(
        connection, "SELECT id, url, title FROM bookmarks WHERE id=1"
    )

    assert result is None
