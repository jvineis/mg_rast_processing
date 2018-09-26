#!/usr/bin/env python
import json
import sys
json1_file = open(sys.argv[1],'rU')
json1_str = json1_file.read()
dat = json.loads(json1_str)
## This script is perfect. You run it with the biom file produced using 
## matrix "http://api.metagenomics.anl.gov/matrix/organism?" like this

# python speciesbiometotxt.py infile.biom outfile.txt

# A funciton that will write a tab separated file of row for each function and column of counts for each sample
def pulldata(functions):
    outfile = open(sys.argv[2],'w')
    outfile.write("Damain"+'\t'+"Phylum"+'\t'+"Class"+'\t'+"Family"+'\t'+"Order"+'\t'+"Genus"+'\t'+"Species"+'\t')
    for i in functions['parameters']['mg_ids']:
        outfile.write(str(i))
        outfile.write('\t')
    outfile.write('\n')
    x = functions['data']['data']
    y = functions['data']['rows']
    fun_dict = {}
    c_dict = {}
    count = 0
 

## THIS SECTION IS FOR TESTING:
#    for line in y:
#        #print line['metadata']
#        if line['metadata'] == None:
#            print "what the fuck", line
#        else:
#            print line['metadata']
    # To collect the counts into a new dictionary
    for line in x:
        c_dict[count] = line
        count +=1
 
    # To collect the functions into a new dictionary
    count1 = 0
    for line in y:
        if line['metadata'] == None:
            fun_dict[count1] = ['Domain','Phylum','Class','Family','Order','Genus',line['id']]
        else:
            fun_dict[count1] = [line['metadata']['hierarchy']['domain'],line['metadata']['hierarchy']['phylum'],line['metadata']['hierarchy']['class'],line['metadata']['hierarchy']['family'],line['metadata']['hierarchy']['order'], line['metadata']['hierarchy']['genus'], line['id']]
         
        count1 +=1
                     
## FOR TESTING TAXA DICTIONARY
#    for key in fun_dict.keys():
#        print fun_dict[key]
## FOR TESTING COUNT DICTIONARY
    
    
    for key in fun_dict.keys():
        for line in fun_dict[key]:
            outfile.write(str(line))
            outfile.write('\t')
        for line in c_dict[key]:
            outfile.write(str(line))
            outfile.write('\t')

        outfile.write('\n')





pulldata(dat)
