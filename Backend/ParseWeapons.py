import xml.etree.ElementTree as ET

filename = "exalt-extractor/output/xml/equip.xml"

tree = ET.parse(filename)
root = tree.getroot()

# DATA STRUCTURES
weapons = []
armor = []
abilities = []



# Get stats on equip. Returns dict
def getStats(obj):

    stats = {}

    foundvalues = obj.findall("ActivateOnEquip")
    
    for statChange in foundvalues:
        stats[statChange.get("stat")] = int(statChange.get("amount"))
    return stats
# Parse text in obj and returns data type (int, float, str)
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


# just get function with check added for readability in code. getOrFind is for if you're searching in a particular fields properties (get) or searching for the value of the field (find)
def getChecked(obj, dataType, name, getOrFind):

    if getOrFind == "find":
        value = obj.findtext(name)
        if value is None:
            return None
        if dataType is int:
            return int(value)
        if dataType is float:
            return float(value)
        if dataType is str:
            return value

    if obj is None:
        return None
    #This is for accessing values within the xml element
    
    
    if getOrFind == "get":
        value = obj.get(name) if obj.get(name) is not None else None
        if value is None:
            return None
        if dataType is int:
            return int(value)
        if dataType is str:
            return value
        if dataType is float:
            return float(value)


# This will be used to programatically parse through the properties in a particular object, and using getChecked() will get all values and return an obj
def parseSubFields(obj):
    if obj is None: return None

    fields = {}

        
    for element in obj:
        if element is None: continue

        dataType = getType(element)
        tag = element.tag

        if element.text is None:
            value = True
        else:
            value = getChecked(obj, dataType, tag, "find")

        fields.update({tag : value})

    return fields


def getProjectileData(obj):

    projectileObjs = obj.findall("Projectile")
    projectileList = []

    for projectileObj in projectileObjs:
        projId = getChecked(projectileObj, int, "id", "get")
        #projId None when no subattacks. Set to 0 for convenience
        if projId is None: projId = 0

        projectileList.append({
        "id" : projId} | parseSubFields(projectileObj))

    subAttacksObjs = obj.findall("Subattack")
    if subAttacksObjs is not None:
        for subAttackObj in subAttacksObjs:

            # subAttackId is "projectileId" in XML. Relates subattack to projectile (1:1). Kept json consistent with ROTMG nomenclature
            subAttackId= getChecked(subAttackObj, int, "projectileId", "get")
            projectileList.append({
            "projectileId" : subAttackId} | parseSubFields(subAttackObj))

    return projectileList

def parseAttributes(obj):
    
    attributes = obj.attrib

    



def addAbility(obj):
    stats = getStats(obj)

    # raw is all of the parsed XML. Only entering what is needed
    raw = parseSubFields(obj)
    activations = obj.findall("Activate")
    attributes = []
    for activate in activations:
        attributes.append([activate.text, activate.attrib])


    ability = {
        'id' : getChecked(obj, str, "id", "get"),
        'projectiles' : getProjectileData(obj),
        'activate' : attributes,
        'onEquip' : stats,
        'slotType' : raw.get("SlotType"),
        'tier' : raw.get("Tier"),
        'mpCost' : raw.get("MpCost"),
        'feedPower' : raw.get("feedPower"),
    }
    return ability


def addWeapon(obj):
    stats = getStats(obj)

    raw = parseSubFields(obj)

    weapon ={
        'id' : getChecked(obj, str, "id", "get"),
        'projectiles' : getProjectileData(obj),
        'onEquip' : stats,
        'tier' : raw.get('Tier') if raw.get('Tier') is not None else "UT",
        'slotType' : raw.get("SlotType"),
        'feedPower' : raw.get("FeedPower")
    }
    return weapon
    #Shots / Dmg / Spread



totalProjectileData = []

for obj in root.findall("Object"):

    classElement = obj.find('Class')
    objElement = classElement.text if classElement is not None else None

    classLabel = obj.find('Labels')
    objLabel = classLabel.text if classLabel is not None else None

    # Check for if not equipment.

    if objElement is None or objLabel is None:
        continue

    if "EQUIPMENT" not in objLabel:
        continue

    if "ABILITY" in objLabel:
        ability = addAbility(obj)
        print(ability)
        print("\n")

    if "WEAPON" in objLabel:
        continue
        # projectileData = getProjectileData(obj)
        # totalProjectileData.append(projectileData)


# for projectiles in totalProjectileData:
#     print(projectiles)