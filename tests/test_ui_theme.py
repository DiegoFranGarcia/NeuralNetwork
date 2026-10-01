from src.ui_theme import get_ticket_app_theme


def test_ticket_app_theme_matches_cinemark_branding():
    theme = get_ticket_app_theme()

    assert theme["name"] == "cinemark"
    assert theme["colors"]["primary"] == "#d11f2d"
    assert theme["colors"]["secondary"] == "#f2c94c"
    assert theme["colors"]["background"] == "#111111"
    assert theme["colors"]["surface"] == "#1e1e1e"
    assert theme["colors"]["text"] == "#ffffff"
    assert theme["typography"]["font_family"] == "Avenir Next"
    assert theme["typography"]["headline_weight"] == "bold"
    assert theme["typography"]["body_weight"] == "regular"
    assert theme["components"]["button_radius"] == 6
    assert theme["components"]["ticket_card_radius"] == 12
