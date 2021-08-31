import sys 

fly_mapping, c_tab_name = sys.argv[1], sys.argv[2]

map_dict = {}

fly_map = open(fly_mapping)
for line in fly_map:
    entry = line.strip("\n").split("\t")
    map_dict[entry[0]] = entry[1]  #creating [k:v] in dict

if len(sys.argv) == 3:
    ctab = open(c_tab_name)
    for line in ctab:
        entry = line.strip("\n").split("\t")
        if entry[8] in map_dict:
            entry[8] = map.dict[entry[8]]
            print(('\t').join(entry))
    
if len(sys.argv) == 4:   
    missing_text = sys.argv[3]
    ctab = open(c_tab_name)
    for line in ctab:
        entry = line.strip("\n").split("\t")
        if entry[8] in map_dict:
            entry[8] = map_dict[entry[8]]
        else:
            entry[8] = missing_text
        print(("\t").join(entry))




    
    






    

    
    



    



    

    

    
    


    


    



    
    











