import xml.etree.ElementTree as ET

filename = "exalt-extractor/output/xml/equip.xml"

tree = ET.parse(filename)
root = tree.getroot()

# Functions
def getStats(foundvalues, stats):
    
    for statChange in foundvalues:
        stats[statChange.get("stat")] = int(statChange.get("amount"))
    return stats

def addAbility()
    getStats(obj.findall("ActivateOnEquip"), stats)
        
    
    classSlotType = obj.find('SlotType')
    objSlotType = classSlotType.text if classSlotType is not None else None

    abilities.append()

# Structure for output items in json

weapons = []
armor = []
abilities = []


for obj in root.findall("Object"):

    stats = {
    "ATK" : 0,
    "DEF" : 0,
    "SPD" : 0,
    "DEX" : 0,
    "VIT" : 0,
    "WIS" : 0,
    "HP" : 0,
    "MP" : 0
}

    obj.attrib.get

    classElement = obj.find('Class')
    objElement = classElement.text if classElement is not None else None

    classLabel = obj.find('Label')
    objLabel = classLabel.text if classLabel is not None else None

    if "ABILITY" in objLabel:

        getStats(obj.findall("ActivateOnEquip"), stats)
        

        objAttributes = ""
    
        classSlotType = obj.find('SlotType')
        objSlotType = classSlotType.text if classSlotType is not None else None

        abilities.append()

    elif "WEAPON" in objLabel:
        
    elif "ARMOR" in objLabel:

    elif "RING" in objLabel:
        


    print(objElement)

