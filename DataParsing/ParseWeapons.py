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
        value = obj.findtext(name)
        if value is None:
            return None
        if dataType is int:
            return int(value)
        if dataType is float:
            return float(value)
        if dataType is str:
            value

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
            subAttackID = getChecked(subAttack, int, "projectileId", "get") #relates to Projectile ID (ID in xml in Projectile field)
            numProjectiles = getChecked(subAttack, int, "NumProjectiles", "find")
            rateOfFire = getChecked(subAttack, float, "RateOfFire", "find")
            arcGap = getChecked(subAttack, float, "ArcGap", "find")
            defaultAngle = getChecked(subAttack, float, "DefaultAngle", "find")
            posOffset = getChecked(subAttack, float, "PosOffset", "find")
            #for equipment with a burst
            burstCount = getChecked(subAttack, int, "BurstCount", "find")
            burstDelay = getChecked(subAttack, float, "BurstDelay", "find")
            burstMinDelay = getChecked(subAttack, float, "BurstMinDelay", "find")

        subAttack = {
            "subAttackID" : subAttackID,
            "numProjectiles" : numProjectiles,
            "rateOfFire" : rateOfFire,
            "arcGap" : arcGap,
            "defaultAngle" : defaultAngle,
            "posOffset" : posOffset,
            "burstCount" : burstCount,
            "burstDelay" : burstDelay,
            "burstMinDelay" : burstMinDelay
        }

        subAttacks.append(subAttack)

    ObjectId = getChecked(projectile, str,"ObjectId", "find")
    Speed = getChecked(projectile, float,"Speed", "find")
    MinDamage = getChecked(projectile, int,"MinDamage", "find")
    MaxDamage = getChecked(projectile, int,"MaxDamage", "find")
    LifetimeMS = getChecked(projectile, float,"LifetimeMS", "find")
    MultiHit = getChecked(projectile, bool,"MultiHit", "find")
    Amplitude = getChecked(projectile, float,"Amplitude", "find")
    Frequency = getChecked(projectile, float,"Frequency", "find")
    Size = getChecked(projectile, int,"Size", "find")
    ArmorPiercing = getChecked(projectile, bool,"ArmorPiercing", "find")
    PassesCover = getChecked(projectile, bool,"PassesCover", "find")
    Parametric = getChecked(projectile, bool,"Parametric", "find")
    FaceDir = getChecked(projectile, bool,"FaceDir", "find")
    ConditionEffect = getChecked(projectile, str,"ConditionEffect", "find")
    ParticleTrail = getChecked(projectile, str,"ParticleTrail", "find")
    Acceleration = getChecked(projectile, float,"Acceleration", "find")
    AccelerationDelay = getChecked(projectile, float,"AccelerationDelay", "find")
    SpeedClamp = getChecked(projectile, int,"SpeedClamp", "find")
    ProtectFromSink = getChecked(projectile, bool,"ProtectFromSink", "find")
    DamageMultiplier = getChecked(projectile, bool,"DamageMultiplier", "find")
    CollisionMult = getChecked(projectile, float,"CollisionMult", "find")
    Wavy = getChecked(projectile, bool,"Wavy", "find")
    Boomerang = getChecked(projectile, bool,"Boomerang", "find")
    CircleTurnDelay = getChecked(projectile, int,"CircleTurnDelay", "find")
    CircleTurnAngle = getChecked(projectile, int,"CircleTurnAngle", "find")
    Magnitude = getChecked(projectile, float,"Magnitude", "find")
    Damage = getChecked(projectile, int,"Damage", "find")
    TurnRate = getChecked(projectile, int,"TurnRate", "find")
    TurnRateDelay = getChecked(projectile, int,"TurnRateDelay", "find")
    TurnStopTime = getChecked(projectile, int,"TurnStopTime", "find")
    TurnAcceleration = getChecked(projectile, float,"TurnAcceleration", "find")
    TurnAccelerationDelay = getChecked(projectile, int,"TurnAccelerationDelay", "find")
    TurnClamp = getChecked(projectile, int,"TurnClamp", "find")


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
