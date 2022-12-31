# one can = 5 sq m
# random height and width
# how many cans you need
# num of cans = wall height x wall width \ cov per can
# result rounded to full numbers
import math
test_height = int(input("Height of the wall is: "))
test_width = int(input("Width of the wall is: "))
test_cover = int(input("What's your paint coverage in square meters? "))
def cans_of_paint(height=test_height, width=test_width, coverage=test_cover):
    number_of_cans = (height * width)/coverage
    num_of_cans_round = math.ceil(number_of_cans)
    print(f"You have to buy {num_of_cans_round} cans of paint.")

cans_of_paint()