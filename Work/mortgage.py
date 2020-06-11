# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 1

##Ex 1.8
#def_payment = payment
#mod_payment = payment + 1000

##Ex 1.9
extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000

def_payment = payment
mod_payment = payment + extra_payment


while principal > 0:
    if months >= 60 and months <= 108 :
        payment=mod_payment

    else :
        payment = def_payment


    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    months = months + 1
    print ( months-1 , total_paid ,principal  )

print('Total paid', round(total_paid,2) ,'months' , months-1)
