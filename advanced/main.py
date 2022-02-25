import logging
import calculator

logger = logging.getLogger('advanced.main')
logger.setLevel(logging.INFO)

# Create console handler for INFO and up, any other messages should be handled by the individual modules
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

logger.addHandler(ch)

def main():
    logger.info('Starting advanced')
    sum = calculator.summation(1, 15)
    logger.info('Summation returned %i', sum)
    calculator.divide(sum, 3)
    calculator.divide(sum, 0)
    logger.info('Finished...')

if __name__ == '__main__':
    main()
