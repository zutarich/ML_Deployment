import sys
# from logger import *
import logging

import sys
sys.path.insert(0, 'src/logger.py')
import logger

def error_message_detail(error,error_detail:sys):
    # the return type of sys exc_tb= gives the info regarding the complete exception
    _,_,exc_tb=error_detail.exc_info()
    #  to fecth the file name -|>
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
    file_name,exc_tb.tb_lineno,str(error))

    return error_message

#  custom exception handling try catch block etc
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
    
if __name__=="__main__":
    try: 
        a=1/0
    except Exception as e:
        logging.info("It's a divide by zero error")
        raise CustomException(e,sys)
    
 

        