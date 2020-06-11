# bounce.py
#
# Exercise 1.5

new_height = 100
bounce_height = 3/5
num_bounce = 1


while num_bounce <= 10 :
    new_height = round(new_height * bounce_height)
    print ( num_bounce ,new_height)
    num_bounce = num_bounce+1

    



