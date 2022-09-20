from unicodedata import category


def pH2Category(pH):
    if pH < 3:
        category = "Strongly acidic"
    elif (3 <= pH) and (pH < 6):
        category = "Weakly acidic"
    elif (6 <= pH) and (pH < 8):
        category = "Neutral"
    elif (8 <= pH) and (pH < 11):
        category = "Weakly basic"
    elif (11 < pH) and (pH <= 14):
        category = "Strongly basic"
    else:
        category = "pH out of range"
    return category