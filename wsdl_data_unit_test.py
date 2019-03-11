import os

#import pytest
#import requests_mock

#from tests.utils import load_xml
from zeep import client, xsd
from zeep.exceptions import Error


def test_bind():
    client_obj = client.Client("test.wsdl")
    operations = [op for op in dir(client_obj.service) if not op.startswith("_")]
    print operations
    #for operation in operations:
    val = client_obj.service.Close_Evergreen_Requisition.__doc__
    print val
    #service = client_obj.bind('RecruitingService','Recruiting')
    '''
    operations = [op for op in dir(client_obj.service) if not op.startswith("_")]
    print operations
    '''
    #print (client_obj.service.operations[1].__doc__)
    #assert service
def readComplexType():
    from zeep import Client
    import operator    
    wsdl = "test.wsdl"
    client = Client(wsdl)
    # get each operation signature
    for service in client.wsdl.services.values():
        print("service:", service.name)
        for port in service.ports.values():
            operations = sorted(
                port.binding._operations.values(),
                key=operator.attrgetter('name'))
    
            for operation in operations:
                print("method :", operation.name)
                print("  input :", operation.input.signature())
                print()
        print()
    
    # get a specific type signature by name
    complextype = client.get_type('ns0:Dynamic_Business_Process_ParametersType')
    print(complextype.name)
    print(complextype.signature())


test_bind()
#readComplexType()