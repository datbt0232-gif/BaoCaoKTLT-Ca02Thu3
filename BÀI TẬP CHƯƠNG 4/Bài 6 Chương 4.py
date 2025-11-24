def computepay(hours, rate):
    try:
        h = float(hours)
        r = float(rate)
    except:
        return "Error: Invalid numeric input."
    if h > 40:
        base_hours = 40
        overtime_rate = r * 1.5
        base_pay = base_hours * r
        overtime_hours = h - base_hours
        overtime_pay = overtime_hours * overtime_rate
        total_pay = base_pay + overtime_pay
    else:
        total_pay = h * r
    return total_pay
hours_1 = input("Enter Hours: ")
rate_1 = input("Enter Rate: ")
pay_1 = computepay(hours_1, rate_1)
print("Pay:", pay_1)