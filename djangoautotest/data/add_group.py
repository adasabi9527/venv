import random
from djangoautotest.common.randomgroup import generate_random_alphanumeric
random_alphanumeric = generate_random_alphanumeric(5)
print(random_alphanumeric)

cases_add_group = {"account":f"{random_alphanumeric}","expected": "added successfully"}
