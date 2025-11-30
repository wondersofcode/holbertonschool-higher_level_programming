#!/usr/bin/env python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    try:
        # Kök element yaradılır
        root = ET.Element("data")

        # Dictionary daxilindəki hər açar üçün child element yaradılır
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)  # XML yalnız string saxlaya bilir

        # XML ağacını fayla yazırıq
        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)
        return True

    except Exception:
        return False


def deserialize_from_xml(filename):
    try:
        # XML faylını parse edirik
        tree = ET.parse(filename)
        root = tree.getroot()

        # Yenidən dictionary strukturu qurulur
        result = {}
        for element in root:
            result[element.tag] = element.text

        return result

    except FileNotFoundError:
        return None
