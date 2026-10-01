def delete_bookmark_by_id(bookmarks, bookmark_id):
    return [bookmark for bookmark in bookmarks if bookmark.get("id") != bookmark_id]
