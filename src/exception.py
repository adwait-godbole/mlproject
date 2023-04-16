import sys
from src.logger import logging

def error_message_details(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    filename=exc_tb.tb_frame.f_code.co_filename
    error_msg="Error occured in Python script name [{0}] line [{1}] error message [{2}]".format(
        filename,exc_tb.tb_lineno,str(error)
    )
    return error_msg

class CustomException(Exception):
    def __init__(self, error_msg, error_detail:sys):
        super().__init__(error_msg)
        self.error_message=error_message_details(error_msg,error_detail=error_detail)

    def __str__(self) -> str:
        return self.error_message
  
if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by Zero")
        raise CustomException(e,sys)