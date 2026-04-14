from ticket_validator import validate_ticket, get_ticket_tier, calculate_total

def test_validate_ticket_is_eight(code):
    assert validate_ticket("TK123456") is True

def test_validate_ticket_is_false(code):
    assert validate_ticket("TK1234567") is False

def test_validate_ticket_string(code):
    with pytest.raises(TypeError):
        validate_ticket(12357367)

def test_get_ticket_tier_valid_General(code):
    assert get_ticket_tier(code) is "General"

def test_get_ticket_tier_valid_VIP(code):
    assert get_ticket_tier("TK567812") is "VIP"

def test_get_ticket_tier_valid_Plat(code):
    assert get_ticket_tier("TK781234") is "Platinum"

def test_calculate_total(prices,discount):
    assert calculate_total([10,20,30],0) is 60.0

def test_calculate_total_invalid_input(prices,discount):
    with pytest.raises(ValueError):
        calculate_total()

