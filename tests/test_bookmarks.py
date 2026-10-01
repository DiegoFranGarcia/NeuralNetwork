from src.bookmarks import delete_bookmark_by_id


def test_delete_bookmark_by_id_removes_matching_id():
    bookmarks = [
        {"id": 1, "url": "https://example.com"},
        {"id": 2, "url": "https://openai.com"},
    ]

    result = delete_bookmark_by_id(bookmarks, 1)

    assert result == [{"id": 2, "url": "https://openai.com"}]


def test_delete_bookmark_by_id_keeps_non_matching_ids():
    bookmarks = [
        {"id": 1, "url": "https://example.com"},
        {"id": 2, "url": "https://openai.com"},
    ]

    result = delete_bookmark_by_id(bookmarks, 3)

    assert result == bookmarks
