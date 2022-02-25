import logging

def summation(start, end):
    logging.info('Starting summation with %i to %i', start, end)
    sum = 0
    for i in range(start, end + 1):
        sum += i

    logging.info('Summation is %i', sum)

    return sum
