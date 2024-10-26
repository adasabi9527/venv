import random
import string

def generate_random_alphanumeric(length=5):
    # 所有字母（大写和小写）
    letters = string.ascii_letters

    # 从字母表中随机选择字母
    random_alphanumeric = ''.join(random.choice(letters) for _ in range(length))

    return random_alphanumeric