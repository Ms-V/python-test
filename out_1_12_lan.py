from out_1_12_que import Asurvey as survey
que="What player you like?"
my_s=survey(que)
my_s.show_question()
print("q to exit\n")
while True:
    res=input("Player:")
    if res=='q':
        break
    my_s.store_respon(res)
print("\n All Down")
my_s.show_respon()