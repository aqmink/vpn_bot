import random
from string import ascii_letters, digits

print(''.join([random.choice(ascii_letters + digits) for _ in range(random.randint(3, 10))]))