import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('config_file.xml')
root = tree.getroot()

# Create a dictionary for the server information
server_info = {}
for child in root.findall('server'):
    for subchild in child:
        server_info[subchild.tag] = subchild.text

# Create a list of dictionaries for the system information
net_systems = []
for child in root.findall('network/system'):
    system_dict = {}
    for subchild in child:
        if subchild.tag == 'whitelist':
            system_dict[subchild.tag] = [ip.text for ip in subchild]
        else:
            system_dict[subchild.tag] = subchild.text
    net_systems.append(system_dict)

# Print the resulting dictionaries
print(f"Server dictionary:\n{server_info}")
print(f"\nSystems on the network:\n{net_systems}")