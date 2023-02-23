import os
import json

dir_list = os.listdir(".\Json")

print(dir_list)

for file in dir_list:

    with open(f'.\Json\{file}', 'r', encoding= "utf-8") as f:
        data = json.load(f)

    # alle Einträge löschen, bei denen der Schlüssel den String "002_HMI_Errors" enthält
    for key in list(data.keys()):
        if "\n" in data[key]: 
            data[key] = data[key].replace("\n", "\\n")
        
        if '"' in data[key]:
            data[key] = data[key].replace('"', '\\"')

        if "[" in data[key]:
            if "[" == str(data[key])[0]:
                del data[key]   

        elif '002_HMI_Errors' in key:
            del data[key]
        
        elif 'alarm_msg' in key:
            del data[key]

        elif 'LowLimit' in key:
            del data[key]

        elif 'HighLimit' in key:
            del data[key]

        elif '002_HMIComm.003_General.FaultCount' in key:
            del data[key]

        elif 'SpoolReport' in key:
            del data[key]

        elif 'FB_' in key:
            del data[key]

        elif 'dummy' in key:
            del data[key]

        elif 'ModulStatus' in key:
            del data[key]

        elif 'Rc_' in key:
            del data[key]


    if file == "de-DE.json":



        data_de = data

    
    # geänderte Daten zurückschreiben
    with open(f'new\\{file}', 'w',  encoding= "utf8") as f:
        f.write("{ \n",  )
        for key, value in data.items():
            f.write(f'"{key}": "{value}",\n',  )
        f.write("} \n",  )

