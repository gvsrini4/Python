import csv, ConfigParser, re, datetime, time
from lxml import etree

elemdict = {}
parser = etree.XMLParser()
data = etree.parse(open("mar13.xsd"),parser)
root = data.getroot()
version = root.get("version")

print root
rootelement = root[0]

elements = rootelement.getchildren()

for e in elements:
    ename = e.get("name")
    elemdict[ename] = [] 
    subelements = e[0][0].getchildren()
    for se in subelements:
        elemdict[ename].append(se.attrib)

specials = root.getchildren()[1:]

specialtypes = {}

for sp in specials:
    #print sp
    sname = sp.get("name") 
    print (sname)
    specialtypes[sname] = {}
    specialtypes[sname]["type"] = sp.tag.split('}')[-1] #removes namespace to get either complex or simple type, another option here would be to use xpath('local-name()') or remove the first 34 characters from the tag, none of them really clean options
    typeelements = sp.getchildren()
    specialtypes[sname]["details"] = []
    print (specialtypes)
    print (specialtypes[sname])

    if specialtypes[sname]["type"] == "complexType":
        specialtypes[sname]["requireds"] = []
        
        for t in typeelements:
            print (t.get("name"))
            specialtypes[sname]["details"].append(t.get("name"))
            if (not "minOccurs" in t.attrib) or int(t.get("minOccurs"))>0:
                specialtypes[sname]["requireds"].append(t.get("name"))
                #print (specialtypes)
    '''    
    else:
        for t in typeelements:
            print (t.get("value"))
            if t.get("value") is not None:
                specialtypes[sname]["details"].append(t.get("value"))
                print specialtypes
   '''  
print (specialtypes)

print (elemdict)