import logging

def getSQALogger():
    logging.basicConfig(filename='Forensics.Test.log', level=logging.INFO, format='%(asctime)s:%(name)s:%(levelname)s:%(message)s', datefmt='%d-%b-%y %H-%M-%S')
    logObj = logging.getLogger('sqa-logger')
    logObj.setLevel(logging.DEBUG)
    return logObj 
