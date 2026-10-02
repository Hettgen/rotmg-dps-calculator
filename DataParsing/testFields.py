## This is a test file, only to be run when looking at new fields and experimenting with their structure / what data will be relevant for the site. Does not run as part of normal operations, only used for development
import xml.etree.ElementTree as ET

filename = "exalt-extractor/output/xml/equip.xml"

tree = ET.parse(filename)
root = tree.getroot()

subAttackFields = {}


for obj in root.findall("Object"):

    subAttacks = obj.findall("Subattack")

    if subAttacks is None:
        continue

    for subAttack in subAttacks:
        if subAttack is None:
            continue

        for element in subAttack:
            print()