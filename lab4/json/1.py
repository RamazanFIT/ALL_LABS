import json

f = open('data1.json')

dict = json.load(f)

print('''Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------''')

dict_2 = dict["imdata"]

for x in dict_2:
    q1 = x["l1PhysIf"]["attributes"]["dn"]
    q2 = x["l1PhysIf"]["attributes"]["speed"]
    q3 = x["l1PhysIf"]["attributes"]["mtu"]
    q4 = x["l1PhysIf"]["attributes"]["descr"]
    print("{0:^50} {1:^20} {2:^7} {3:^7}".format(q1, q4 ,q2, q3))









