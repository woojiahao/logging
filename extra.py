import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(a)s %(b)s %(result)s :: %(message)s")

def exp(a, b):
    result = a
    for i in range(1, b + 1):
        logging.info("Iteration...", extra={'a': a, 'b': b, 'result': result})
        result *= a

    return result

exp(2, 3)
