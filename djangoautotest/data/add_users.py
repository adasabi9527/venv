import random
import string

random_letters1 = ''.join(random.choice(string.ascii_letters) for _ in range(3))
random_letters2 = ''.join(random.choice(string.ascii_letters) for _ in range(3))
# 生成五个随机数字
random_digits1 = ''.join(random.choice(string.digits) for _ in range(5))
random_digits2 = ''.join(random.choice(string.digits) for _ in range(5))

# 将随机字母和数字组合在一起
random_combo1 = random_letters1 + random_digits1
random_combo2 = random_letters2 + random_digits2
# print(random_combo)

cases_user_group = {"account":f"{random_combo1}","password":f"{random_combo2}","password1":f"{random_combo2}","expected": "added successfully"}