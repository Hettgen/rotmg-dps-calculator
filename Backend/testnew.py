# from pathlib import Path
# import xml.etree.ElementTree as ET
# from collections import defaultdict

# xml_dir = Path("exalt-extractor/output/xml")

# items = defaultdict(list)

# for path in xml_dir.glob("*.xml"):
#     try:
#         root = ET.parse(path).getroot()
#     except ET.ParseError as e:
#         print(f"Failed to parse: {path.name}")
#         print(f"Error: {e}")
#         continue

#     for obj in root.iter("Object"):
#         name = obj.get("id", "")

#         if "orb" in name.lower() or "mystic" in name.lower():
#             items[name].append({
#                 "file": path.name,
#                 "type": obj.get("type"),
#                 "xml": ET.tostring(obj, encoding="unicode")
#             })

# for name, versions in items.items():
#     print(f"\n{name}: {len(versions)} occurrence(s)")
#     for version in versions:
#         print(version["file"], version["type"])
#         print(version["xml"][:1000])




# from pathlib import Path

# xml_dir = Path("exalt-extractor/output/xml")

# matches = 0

# for path in xml_dir.rglob("*.xml"):
#     content = path.read_text(encoding="utf-8", errors="replace")

#     for line_number, line in enumerate(content.splitlines(), start=1):
#         if "hex" in line.lower():
#             print(f"{path.name} | Line {line_number}: {line.strip()}")
#             matches += 1

# print(f"\nTotal matches: {matches}")

from pathlib import Path
import xml.etree.ElementTree as ET

path = Path("exalt-extractor/output/xml/equip.xml")
root = ET.parse(path).getroot()

for obj in root.findall("Object"):
    name = obj.get("id", "")

    if "orb" not in name.lower():
        continue

    print(f"\n{'=' * 50}")
    print(f"ITEM: {name}")
    print(f"TYPE: {obj.get('type')}")

    for element in obj:
        if (
            "activate" in element.tag.lower()
            or "effect" in element.tag.lower()
            or "condition" in element.tag.lower()
        ):
            print(ET.tostring(element, encoding="unicode").strip())