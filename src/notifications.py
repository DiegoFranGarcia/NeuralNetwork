from __future__ import annotations


class NotificationCenter:
    def __init__(self) -> None:
        self._subscribers: list[callable] = []

    def subscribe(self, callback: callable) -> None:
        if callback not in self._subscribers:
            self._subscribers.append(callback)

    def unsubscribe(self, callback: callable) -> None:
        if callback in self._subscribers:
            self._subscribers.remove(callback)

    def notify(self, event: str, payload: dict | None = None, *, important: bool = True) -> None:
        if not important:
            return
        for callback in list(self._subscribers):
            callback(event, payload or {})
