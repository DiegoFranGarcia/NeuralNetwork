from src.notifications import NotificationCenter


def test_notification_center_emits_real_time_events():
    center = NotificationCenter()
    received = []

    def handler(event, payload):
        received.append((event, payload))

    center.subscribe(handler)
    center.notify("model_trained", {"accuracy": 0.92})

    assert received == [("model_trained", {"accuracy": 0.92})]


def test_notification_center_does_not_emit_non_important():
    center = NotificationCenter()
    received = []

    def handler(event, payload):
        received.append((event, payload))

    center.subscribe(handler)
    center.notify("info", {"detail": "ignore"}, important=False)

    assert received == []


def test_notification_center_unsubscribe():
    center = NotificationCenter()
    received = []

    def handler(event, payload):
        received.append((event, payload))

    center.subscribe(handler)
    center.unsubscribe(handler)
    center.notify("model_saved", {})

    assert received == []
