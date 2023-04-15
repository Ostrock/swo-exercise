import logging
import time

logging.basicConfig(
    filename='./logs/application.log',
    filemode='a',
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.DEBUG,
)


logging.Formatter.converter = time.gmtime

shopping_cart_logger = logging.getLogger('ShoppingCart logger')