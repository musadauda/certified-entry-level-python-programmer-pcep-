def calculate_tip(bill_amount, percentage_tip):
    total_bill = bill_amount + (bill_amount*(percentage_tip/100))
    return float(total_bill)

print(calculate_tip(100000, 5))

def discounted_cal(original_price, discount_percentage):
    discounted_price = original_price - (original_price*(discount_percentage/100))
    return discounted_price

print(discounted_cal(1000, 10))

def travel_time(distance, avg_speed):
    travel_time = distance / avg_speed
    return travel_time

print(travel_time(1000, 120))

def calories_calculator(br_cal, lu_cal, di_cal, exercise_cal):
    net_cal = br_cal + lu_cal + di_cal - exercise_cal
    return net_cal


print(calories_calculator(689, 900,400, 1000))