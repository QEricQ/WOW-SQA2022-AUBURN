import logging

def getSQALogger():
    logging.basicConfig(filename='Forensics.Test.log', level=logging.DEBUG, format='%(asctime)s:%(name)s:%(levelname)s:%(message)s', datefmt='%d-%b-%y %H-%M-%S')
    logObj = logging.getLogger('sqa-logger')
    loggerOBJ.setLevel(logging.INFO)
    return logObj 
