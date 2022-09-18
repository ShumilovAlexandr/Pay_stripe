def checking_positive_numbers(price):
    try:
        if price > 0:
            return price
    except ValueError:
        print('Стоимость Item не может быть меньше или равна 0')
