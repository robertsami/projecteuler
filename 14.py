# 10/29/16
from collections import deque
def get_some_answers():
    answers = {}
    answered_nums = set()
    frontier = deque([(1, 0)])
    i_iter = 0
    while frontier:

        val, num_so_far = frontier.popleft()
        if val in answers:
            continue
        if val <= 1000000:
            answered_nums.add(val)
            if len(answered_nums) >= 999999:
                break
        answers[val] = num_so_far
        if val < 3000000:
            frontier.append((val * 2, num_so_far + 1))
        if (val - 1) % 3 == 0 and val > 1:
            frontier.append(((val - 1) / 3, num_so_far + 1))
        if i_iter % 10000 == 0:
            print 'iter {} answers {}'.format(i_iter, len(answered_nums))
        i_iter += 1
    return answers

def fill_single_answer(val, some_answers):
    num_steps = 0
    current_val = val
    while current_val not in some_answers:
        # print current_val, num_steps
        if current_val % 2 == 0:
            current_val /= 2
        else:
            current_val = current_val * 3 + 1
        num_steps += 1
    some_answers[val] = num_steps + some_answers[current_val]

def get_rest_answers(some_answers):
    print 'dankk'
    remaining_keys = set(range(1,1000000)) - set(key for key in some_answers.iterkeys() if key < 1000000)
    print 'sauce'
    num_processed = 0
    for key in remaining_keys:
        fill_single_answer(key, some_answers)
        num_processed += 1
        if num_processed == 1:
            print 'got one'
        if num_processed % 1000 == 0:
            print 'iter {}'.format(num_processed)

import time
start = time.time()

answers = get_some_answers()
get_rest_answers(answers)

max_key = 1
for k, v in answers.iteritems():
    if k < 1000000 and v > answers[max_key]:
        max_key = k
print max_key, time.time() - start
