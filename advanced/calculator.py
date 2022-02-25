import logging

logger = logging.getLogger('advanced.calculator')
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create a console handler to print logs with WARNING and up
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)

# Create a console handler to print logs with INFO and up
fh = logging.FileHandler('advanced.log')
fh.setLevel(logging.INFO)
fh.setFormatter(formatter)

logger.addHandler(ch)
logger.addHandler(fh)

def summation(start, end):
    logger.info('Starting summation')
    sum = 0
    for i in range(start, end + 1):
        logger.info('Summing %i with %i', i, sum)
        sum += i
    
    logger.info('Total sum from %i to %i is %i', start, end, sum)

    return sum

def divide(a, b):
    logger.info('Dividing %i by %i', a, b)
    try:
        result = a / b
    except Exception as exc:
        logger.error('Error occurred with dividing', exc_info=True)
