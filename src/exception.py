import sys

def error_message_detail(error,error_detail:sys):
    _,_,exec_tb = error_detail.exc_info()
    filename= exec_tb.tb_frame.f_code.co_filename   
    error_mesage = "Error occcoured in python script name [{0}] line number [{1}] with error message[{2}]".format(
        filename,exec_tb.tb_lineno,str(error))
    
    return error_mesage

    class Custom_Exception(Exception):
        def __init__(self,error_mesage,error_detail:sys):
            super.__init__(error_mesage)
            self.error_mesage = error_message_detail(error_mesage,error_detail=error_detail)
            
            def __str__(self):
                self.error_mesage