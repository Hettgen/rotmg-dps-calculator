## This is a test file, only to be run when looking at new fields and experimenting with their structure / what data will be relevant for the site. Does not run as part of normal operations, only used for development
import xml.etree.ElementTree as ET

filename = "exalt-extractor/output/xml/equip.xml"

tree = ET.parse(filename)
root = tree.getroot()

testObjFields = {}

def getType(obj):

    objText = obj.text
    if objText is None:
        return None

    try:
        val = int(objText)
    except(ValueError, TypeError):
        try:
            val = float(objText)
        except(ValueError, TypeError):
            val = objText
    return type(val)


for obj in root.findall("Object"):
    testObj = obj.findall("Projectile")

    for testField in testObj:
        if testField is None:
            continue

        for element in testField:
            dataType = getType(element)
            field = element.tag
            if dataType == int and testObjFields.get(field) == float:
                continue
                

            elementType = getType(element)
            testObjFields.update({element.tag : elementType})

x = 0
for field, fieldType in testObjFields.items():
    print(fieldType.__name__ if fieldType is not None else type(True).__name__)
#    print(field)


# , fieldType.__name__ if fieldType is not None else True