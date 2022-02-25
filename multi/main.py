import logging
import calculator

def main():
    logging.basicConfig(level='INFO', filename='main.log')
    logging.info('Starting application...')
    calculator.summation(1, 10)
    logging.info('Finished running')

if __name__ == '__main__':
    main()
