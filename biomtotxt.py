#!/usr/bin/env python
import json
import sys
json1_file = open(sys.argv[1],'rU')
json1_str = json1_file.read()
dat = json.loads(json1_str)

#print dat.keys()
print dat[u'parameters'][u'mg_ids']

# A funciton that will write a tab separated file of row for each function and column of counts for each sample
def pulldata(functions):
    outfile = open(sys.argv[2],'w')
    outfile.write("Level1"+'\t'+"Level2"+'\t'+"Level3"+'\t'+"Level4"+'\t')
    for i in functions['parameters']['mg_ids']:
        outfile.write(str(i))
        outfile.write('\t')
    outfile.write('\n')
    x = functions['data']['data']
    y = functions['data']['rows']
    fun_dict = {}
    c_dict = {}
    count = 0

    # To collect the counts into a new dictionary
    for line in x:
        c_dict[count] = line
        count +=1
    # To collect the functions into a new dictionary
    count1 = 0    
    for line in y:
        fun_dict[count1] = line[u'metadata'][u'hierarchy']
        count1 +=1 
 #   for key in c_dict.keys():
 #       print c_dict[key]
    level4_list = []
    for key in fun_dict.keys():
        list_to_write = []
        if fun_dict[key]['level4'] not in level4_list:
        
            list_to_write.append(fun_dict[key]['level1'])
            if "level2" in fun_dict[key].keys():
                list_to_write.append(fun_dict[key]['level2'])
            else:
                list_to_write.append("unknown")#"unknown"+str(key))
            if "level3" in fun_dict[key].keys():
                list_to_write.append(fun_dict[key]['level3'])
            else:
                list_to_write.append("unknown")#"unknown"+str(key))
            list_to_write.append(fun_dict[key]['level4'])
            for i in c_dict[key]:
                list_to_write.append(i)
  #      print key, list_to_write                 
            for i in list_to_write:
                outfile.write(str(i))
                outfile.write('\t')
            outfile.write('\n')
        level4_list.append(fun_dict[key]['level4'])

    


pulldata(dat)
