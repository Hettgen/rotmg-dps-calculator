import xml.etree.ElementTree as ET

filename = "exalt-extractor/output/xml/equip.xml"

tree = ET.parse(filename)
root = tree.getroot()

# DATA STRUCTURES
weapons = []
armor = []
abilities = []


# Functions
def getStats(obj):

    stats = {}

    foundvalues = obj.findall("ActivateOnEquip")
    
    for statChange in foundvalues:
        stats[statChange.get("stat")] = int(statChange.get("amount"))
    return stats

def getNum(obj, dataType):

    return dataType(obj) if obj is not None else None


# just get function with check added for readability in code. getOrFind is for if you're searching in a particular fields properties (get) or searching for the value of the field (find)
def getChecked(obj, dataType, name, getOrFind):

    if getOrFind is "find":
        if dataType is int:
            value = obj.findtext(name)
            return int(value) if value is not None else None
        if dataType is float:
            value = obj.findtext(name)
            return float(value) if value is not None else None
        if dataType is str:
            return obj.findtext(name)

    if obj is None:
        return None
    #This is for accessing values within the xml element
    
    
    if getOrFind is "get":
        value = obj.get(name) if obj.get(name) is not None else None
        if value is None:
            return None
        if dataType is int:
            return int(value)
        if dataType is str:
            return value
        if dataType is float:
            return float(value)

def getProjectileData(obj):

    projectile = obj.find("Projectile")
    # Check for Subattack
    subAttacksObj = obj.findall("Subattack")
    subAttacks = []
    if subAttacksObj is not None:
        for subAttack in subAttacks:
            subAttackID = getChecked(subAttack, int, "projectileId", "get")
            numProjectiles = getChecked(subAttack, int, "NumProjectiles", "find")
            rateOfFire = getChecked(subAttack, float, "RateOfFire", "find")
            posOffset = getChecked(subAttack, float, "PosOffset", "find")

    if projectile is None:
        return
    projName = projectile.findtext("ObjectId")
    minDmg = getNum(projectile.findtext("MinDamage"), float)
    maxDmg = getNum(projectile.findtext("MaxDamage"), float)
    avgDmg = (minDmg + maxDmg) / 2
    projCount = getNum(projectile.findtext("NumProjectiles"), int)

def addAbility(obj):

    name = getChecked(obj, str, "id", "get")
    stats = getStats(obj)
        
    slotType = obj.find("SlotType").text if obj.find("SlotType") is not None else None
    mpCost = int(obj.find("MpCost").text) if obj.find("MpCost") is not None else None
    
    # for shots / scaling
    onActivate = obj.find("Activate") if obj.find("Activate") is not None else None
    shots = getChecked(onActivate, int, "numShots", "get")
    scalingStat = getChecked(onActivate, str, "scalingStat", "get")
    statModScalingMin = getChecked(onActivate, int, "statModScalingMin", "get")
    statModDamage = getChecked(onActivate, float, "statModDamage", "get")
    statModNumShots = getChecked(onActivate, float, "statModNumShots", "get")

    ability = {
        "Name" : name,
        "Stats" : stats,
        "SlotType" : slotType,
        "mpCost" : mpCost,
        "Shots" : shots,
        "ScalingStat" : scalingStat,
        "statModScalingMin" : statModScalingMin,
        "statModDamage" : statModDamage,
        "statModNumShots" : statModNumShots
    }
    abilities.append(ability)
def addWeapon(obj):
    stats = getStats(obj)

    slotType = obj.find("SlotType").text if obj.find("SlotType") is not None else None

    #Shots / Dmg / Spread
    shots = getChecked(obj, int, "NumProjectiles", "find")
    shotMinDmg = getChecked(obj, )


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


        #getStats(obj.findall("ActivateOnEquip"), stats)
        

        #objAttributes = ""

        #objSlotType = obj.find('SlotType').text if obj.find('SlotType') is not None else None

        addAbility(obj)

for ability in abilities:
    print(ability)
    print("\n")
