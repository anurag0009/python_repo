import logging



logging.basicConfig(filename='loger.log',level=logging.DEBUG,format='%(asctime)s %(message)s')




logging.info("This is the info log")
logging.warning("this is my warniung log")
logging.error("this is the error log")



print(logging.__file__)
