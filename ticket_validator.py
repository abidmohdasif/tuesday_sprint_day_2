def validate_ticket(code):
    if len(code) != 8:
        return False

def get_ticket_tier(code):
    num = int(code[3])
    
    if 0 <= num <= 3:
        return "General"
    elif 4 <= num <= 6:
        return "VIP"
    else:
        return "Platinum"

def calculate_total(prices,discount=0):
    pass