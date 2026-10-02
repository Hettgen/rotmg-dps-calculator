## This is a test file, only to be run when looking at new fields and experimenting with their structure / what data will be relevant for the site. Does not run as part of normal operations, only used for development
import xml.etree.ElementTree as ET

filename = "exalt-extractor/output/xml/equip.xml"

tree = ET.parse(filename)
root = tree.getroot()

subAttackFields = {}

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
    subAttacks = obj.findall("Subattack")

    for subAttack in subAttacks:
        if subAttack is None:
            continue

        for element in subAttack:
            dataType = getType(element)
            field = element.tag
            if dataType == int and subAttackFields.get(field) == float:
                continue
                


            subAttackFields.update({element.tag : getType(element) })


for field, fieldType in subAttackFields.items():
    print(field, fieldType.__name__)