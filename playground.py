from model import db

cardnr = 0
print(str(db))

def card_view():
    global cardnr
    card = db[cardnr]
    return card

print(cardnr)

while cardnr < len(db):
    print(card_view())
    cardnr += 1
    print(str(cardnr) + "Numer z while'a")