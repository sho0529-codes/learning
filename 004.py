# 硬貨による支払い

def pay_coins(value):  # valueに金額
    en500 = 0
    en100 = 0
    en50 = 0
    en10 = 0
    en5 = 0
    en1 = 0
    
    while value > 0:
        if value >= 500:
            value -= 500
            en500 += 1
        elif value >= 100:
            value -= 100
            en100 += 1
        elif value >= 50:
            value -= 50
            en50 += 1
        elif value >= 10:
            value -= 10
            en10 += 1
        elif value >= 5:
            value -= 5
            en5 += 1
        elif value >= 1:
            value -= 1
            en1 += 1
    
    return f"{500 * en500 + 100 * en100 + 50 * en50 + 10 * en10 + 5 * en5 + 1 * en1}円は、500円玉: {en500}, 100円玉: {en100}, 50円玉: {en50}, 10円玉: {en10}, 5円玉: {en5}, 1円玉: {en1}"

print(pay_coins(1987))