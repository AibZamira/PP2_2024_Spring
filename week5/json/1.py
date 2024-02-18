import json
print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")

with open("sample-data.json", "r") as js_file:
    j = json.load(js_file)
for it in j["imdata"]:
    print(f"{it["l1PhysIf"]["attributes"]["dn"]}                              {it["l1PhysIf"]["attributes"]["speed"]}   {it["l1PhysIf"]["attributes"]["mtu"]}")



    