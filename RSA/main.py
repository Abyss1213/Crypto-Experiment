import SHA

import time
import random
import string


def create_random_message(message_size):
    return ''.join(random.choice(string.ascii_letters) for i in range(message_size))


def get_32_digest(hashed):
    return bin(int(hashed, 16))[2:].zfill(160)[0:31]


def get_index_for_element(hash, hashes_list):
    for i in range(0, len(hashes_list)):
        if hashes_list[i] == hash:
            return i


def search_for_collisions():
    dictionary = dict()
    for i in range(0, 110000):  # there's a 75% chance of finding a collision here
        message = create_random_message(random.randint(1, 100))
        cut_digest = get_32_digest(SHA.sha(message))
        collision_plain = dictionary.get(cut_digest, '-1')
        if collision_plain != '-1' and collision_plain != message:
            print('Collision found:')
            print(collision_plain, '\nand\n', message, '\nhave the same first 32 bits in the digest: ', cut_digest)
            return i
        dictionary[cut_digest] = message
    return 110000


def birthday_attack():
    print('----------- birthday attack on SHA -----------')
    print('Start singing happy birthday...')
    start = time.time()
    results = search_for_collisions()
    while results % 110000 == 0:
        results += search_for_collisions()
    end = time.time()
    print('Collision found in ', end - start, 'seconds after trying', results, ' times.')


birthday_attack()