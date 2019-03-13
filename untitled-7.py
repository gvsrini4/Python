import csv, ConfigParser, re, datetime, time
from lxml import etree

elemdict = {}
parser = etree.XMLParser()
data = etree.parse(open("testschema.xsd"),parser)
root = data.getroot()
version = root.get("version")

rootelement = root[0]

elements = rootelement[0][0].getchildren()

for e in elements:
    ename = e.get("name")
    elemdict[ename] = [] 
    subelements = e[0][0].getchildren()
    for se in subelements:
        elemdict[ename].append(se.attrib)

specials = root.getchildren()[1:]

specialtypes = {}

for sp in specials:
    sname = sp.get("name") 
    specialtypes[sname] = {}
    specialtypes[sname]["type"] = sp.tag.split('}')[-1] #removes namespace to get either complex or simple type, another option here would be to use xpath('local-name()') or remove the first 34 characters from the tag, none of them really clean options
    typeelements = sp.getchildren()[0].getchildren()
    specialtypes[sname]["details"] = []
    if specialtypes[sname]["type"] == "complexType":
        specialtypes[sname]["requireds"] = []
        for t in typeelements:
            specialtypes[sname]["details"].append(t.get("name"))
            if (not "minOccurs" in t.attrib) or int(t.get("minOccurs"))>0:
                specialtypes[sname]["requireds"].append(t.get("name"))
    else:
        for t in typeelements:
            specialtypes[sname]["details"].append(t.get("value"))
            
            
print (specialtypes)