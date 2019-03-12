import xmlschema
from pprint import pprint

def xml2XSDConversion():
    
    xs = xmlschema.XMLSchema('test_1.xsd')
    pprint(xs.to_dict('test_1.xml'))
    
xml2XSDConversion()