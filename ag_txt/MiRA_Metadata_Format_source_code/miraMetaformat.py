''' Program: American Gut text files converted to MiRA format. 
    Purpose: AG.txt or AG_full.txt files are converted into MiRA's Metadata file format
    Author: Jonathan Kindberg
    Last Revised: 03/18/2015
'''

import re

#AG.txt file
#AG_full.txt file

def miraMetaformat(file):
    outfilename = ''.join((re.split('\.',file)[0] + '_out.txt'))
    outfile = open(outfilename,'w')
    outfile.write("Sample Name\t Category\t Key\t Value\n")
#     outfile.close()
    with open(file) as f:

        keepgoing = True
        header = f.next().strip()
        hsplit = re.split('\t',header)
        hlist = []
    
        for each in range(0,len(hsplit)):
            if hsplit[each] == "#SampleID":
                continue
            else:
                hlist.append(hsplit[each])
        for myline in f:
       
            linelist = []
            lines = re.split('\t',myline.strip())
            sampleid = lines[0]
                
            for each in range(0,len(lines)):
                linelist.append(lines[each])
            linelist.pop(0)
            zipped = zip(hlist,linelist)
                
            for each in range(0,len(zipped)):
                if zipped[each][1] == '':
                    value = 'NA'
                else:
                    value = zipped[each][1]
                #print sampleid,"Common",zipped[each][0],value
                    print >> outfile, "%s\t%s\t%s\t%s\t"%  (sampleid,'Common',zipped[each][0],value)

    
              
#miraMetaformat('C:/Users/Jonathan/Desktop/Nihar/Projects/ag/AG.txt')
miraMetaformat('C:/Users/Jonathan/Desktop/Nihar/Projects/ag/AG_full.txt')    
