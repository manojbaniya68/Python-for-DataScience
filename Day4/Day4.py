# import pdb

# aList = [1,2,3,4,5]
# def fact(n):
#     f = 1
#     for i in range(1,n+1):
#         f = f*i

# pdb.set_trace()

# fact(5)


import logging
#There are different levels
logging.basicConfig(level=logging.WARNING,
                    filename="Day4.log",
                    filemode="a",
                    format="%(asctime)s %(levelname)s %(message)s")

logging.debug("THIS IS A DEBUG VALUE")
logging.info("THIS IS A INFO")
logging.warning("THIS IS A WARNING")
logging.error("THIS IS A ERROR")
logging.critical("DANGER")