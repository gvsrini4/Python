import xml.etree.ElementTree as etree
 
def xsdParser():
    
    root = etree.parse('testSample.xsd').getroot() 
    
    for element in root.iter():
        print("%s , %s , %s" % (element.tag, element.attrib, element.text))    


xsdParser()