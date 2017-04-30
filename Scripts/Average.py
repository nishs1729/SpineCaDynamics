from numpy import *
import os

def getDirs(path, sstr='seed_'):
        dirs = [d for d in os.listdir(path) if os.path.isdir(path + '/' + d) and sstr in d]
        dirs.sort()
        return(dirs)
        
def avg_dat(inFile="name_of_input_file", outFile="name_of_output_file"):
        dataPath = '/data/test/offset_time_01'
        resultPath ='/data/test/result'
        dirs = getDirs(dataPath)
        print dirs
        seeds = len(dirs)
        print seeds
                
        avg = []
        for i in range(seeds):
            avg.append(genfromtxt(dataPath + dirs[i] + inFile, invalid_raise=False))#, use_col=(1,2,6)))
        avg = array(avg)
        
        m = (avg.mean(axis=0))
        #sd = std(avg, axis=0)
        
        avgData = m #column_stack([m])#, sd])
        
        of = resultPath + outFile
        print "Writing average to: " + of
        savetxt(of, avgData, fmt='%.7f')
        
avg_dat()
