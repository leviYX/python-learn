import logging
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
# logging.disable(logging.CRITICAL)

logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('End of program')
