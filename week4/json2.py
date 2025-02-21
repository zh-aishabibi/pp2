import json

with open(r"C:\Users\Адина\Documents\GitHub\pp2\week4\json1.json", encoding="utf-8") as file:  # Assuming it's a .json file
    data = json.load(file)

# Print the header for the table
print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<7}")
print("-" * 80)

# Parse and print the data from the JSON
for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    description = attributes.get("descr", "")
    speed = attributes.get("speed", "inherit")
    mtu = attributes.get("mtu", "")

    # Print each entry in the desired format
    print(f"{dn:<50} {description:<20} {speed:<7} {mtu:<7}")
