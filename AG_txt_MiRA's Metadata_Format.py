''' Program: American Gut text files converted to MiRA format. 
    Purpose: AG.txt or AG_full.txt files are converted into MiRA's Metadata file format
    Author: Jonathan Kindberg
    Last Revised: 03/18/2015
'''


#for lines in agFull_lines:
#        agFull_outfile.write(str(lines))
   

import re

#AG.txt file
#ag_infile = open('C:/Users/Jonathan/Desktop/Nihar/Projects/ag/AG.txt','r')
ag_outfile = open('C:/Users/Jonathan/Desktop/Nihar/Projects/ag/ag_output.txt','w')
#ag_lines = ag_infile.readlines()
#ag_infile.close()



#AG_full.txt file
# agFull_infile = open('C:/Users/Jonathan/Desktop/Nihar/Projects/agFull/AG_full.txt','r')
# agFull_outfile = open('C:/Users/Jonathan/Desktop/Nihar/Projects/agFull/agFull_output.txt','w') 
# agFull_lines = agFull_infile.readlines()
# agFull_infile.close()


def agDataFormat(ballz):

    with open(ballz,'r') as f:
        keepgoing = True
        header = f.next().strip()
        hsplit = re.split('\t',header)
        hlist = []
        for each in range(0,len(hsplit)):
            hlist.append(hsplit[each])
        while keepgoing:
            linelist = []
            lines = re.split('\t',f.next().strip())
            sampleid = lines[0]
            for each in range(0,len(lines)):
                linelist.append(lines[each])
            zipped = zip(hlist,linelist)
            for each in range(0,len(zipped)):
                if zipped[each][1] == '':
                    value = 'NA'
                else:
                    value = zipped[each][1]
                print sampleid,"Common",zipped[each][0],value
            try:
                lines = re.split('\t',f.next().strip())
            except:
                break
            
            

agDataFormat('C:/Users/Jonathan/Desktop/Nihar/Projects/ag/AG.txt')   

