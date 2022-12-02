import logging

def getSQALogger():
    logging.basicConfig(filename='forensics.TEST.log', level=logging.DEBUG, format='%(asctime)s:%(name)s:%(levelname)s:%(message)s', datefmt='%d-%b-%y %H-%M-%S')
    logObj = logging.getLogger('sqa-logger')
    return logObj 
