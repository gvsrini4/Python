from lxml import etree

INDICATORS = ["all", "sequence", "choice"]
TYPES = ["simpleType", "complexType"]

class schema:

    def __init__(self, schemafile):
        if schemafile is None:
            print "Error creating Schema: Invalid schema file used"
            return

        self.schema = self.create_schema(etree.parse(schemafile))

    def create_schema(self, schema_data):
        def getXSVal(element): #removes namespace
            return element.tag.split('}')[-1]

        def get_simple_type(element):
            return {
                "name": element.get("name"),
                "restriction": element.getchildren()[0].attrib,
                "elements": [ e.get("value") for e in element.getchildren()[0].getchildren() ]
        }

        def get_simple_content(element):
            return {
                "simpleContent": {
                    "extension": element.getchildren()[0].attrib,
                    "attributes": [ a.attrib for a in element.getchildren()[0].getchildren() ]
                }
            }

        def get_elements(element):


            if len(element.getchildren()) == 0:
                return element.attrib

            data = {}

            ename = element.get("name")
            tag = getXSVal(element)

            if ename is None:
                if tag == "simpleContent":
                    return get_simple_content(element)
                elif tag in INDICATORS:
                    data["indicator"] = tag
                elif tag in TYPES:
                    data["type"] = tag
                else:
                    data["option"] = tag

            else:
                if tag == "simpleType":
                    return get_simple_type(element)
                else: 
                    data.update(element.attrib)

            data["elements"] = []
            data["attributes"] = []
            children = element.getchildren()        

            for child in children:
                if child.get("name") is not None:
                    data[getXSVal(child)+"s"].append(get_elements(child))
                elif tag in INDICATORS and getXSVal(child) in INDICATORS:
                    data["elements"].append(get_elements(child))
                else:
                    data.update(get_elements(child))

            if len(data["elements"]) == 0:
                del data["elements"]
            if len(data["attributes"]) == 0:
                del data["attributes"]

            return data

        schema = {}
        root = schema_data.getroot()
        children = root.getchildren()
        for child in children:
            c_type = getXSVal(child)
            if child.get("name") is not None and not c_type in schema:
                schema[c_type] = []
            schema[c_type].append(get_elements(child))
        return schema

    def get_Types(self, t_name):
        types = []
        for t in self.schema[t_name]:
            types.append(t["name"])
        return types

    def get_simpleTypes(self):
        return self.get_Types("simpleType")

    def get_complexTypes(self):
        return self.get_Types("complexType")


if __name__ == '__main__':
    fschema = open("schema.txt")

    schema = schema(fschema)

    print schema.get_simpleTypes()
    print schema.get_complexTypes()

