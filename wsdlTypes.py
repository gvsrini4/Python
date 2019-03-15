from zeep import Client
import operator
import time
import logging
import traceback


#Logging
logger = logging.getLogger('wsdlDataParse')
hdlr = logging.FileHandler('wsdlDataParse.log')
formatter = logging.Formatter('%(asctime)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

wsdlName = 'test.wsdl'
typeName = "Assess_Candidate_Response_DataType"

def wsdlParse(wsdlName,typeName):
    try:
        client = Client(wsdlName)  
        logger.info("Able to parse the %s "%wsdlName)
        for t in client.wsdl.types.types:
            a = t
            b = (a.name,str(a))
            if a.name == typeName:
                print b
            
    except Exception as e:
        logger.error(e)
        
wsdlParse(wsdlName,typeName)