print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
score1 = 0
score2 = 0

counting_t = name1.count("t")
counting_r = name1.count("r")
counting_u = name1.count("u")
counting_e = name1.count("e")
subtotal_true_1 = counting_t + counting_r + counting_u + counting_e

counting_t2 = name2.count("t")
counting_r2 = name2.count("r")
counting_u2 = name2.count("u")
counting_e2 = name2.count("e")
subtotal_true_2 = counting_t2 + counting_r2 + counting_u2 + counting_e2

score1 += (subtotal_true_1 + subtotal_true_2)

counting_l = name1.count("l")
counting_o = name1.count("o")
counting_v = name1.count("v")
counting_e = name1.count("e")
subtotal_love_1 = counting_l+counting_o+counting_v+counting_e

counting_l2 = name2.count("l")
counting_o2 = name2.count("o")
counting_v2 = name2.count("v")
counting_e2 = name2.count("e")
subtotal_love_2 = counting_l2+counting_o2+counting_v2+counting_e2

score2 += subtotal_love_2 + subtotal_love_1

final_score = 10*score1 + score2

if final_score < 10 or final_score > 90:
    print(f"Your score is {final_score}. You go together like coke and mentos.")
elif 40 <= final_score <= 50:
    print(f"Your score is {final_score}. You go alright together.")
else:
    print(f"Your score is {final_score}")

