#import the csv module
import csv

class PortfolioConcentration(object):
    
    #open a comma delimited file and return the output
    #I wrote this function so that it takes any column and returns the sum of market value by that column    
    def GetMeasureTotalBySlice(self, slice, measure):
        try:
            positionsFile = None
            # raw string
            fileName = r"./PortfolioAppraisalReport.csv"
            if not csv.Sniffer().has_header(fileName):
                raise Exception("headers expected in position file. FileName: " + fileName)
            positionsFile = open(fileName, 'rt')
            dictReader = csv.DictReader(positionsFile)
            #dictReader is list of dictionaries where the keys are the column headers and the values represent one row of values
            
            dictTag = {}
            #iterate over 
            for dictRow in dictReader:
                mv = dictRow[measure]
                strat = dictRow[slice]
                #need to cast to float
                if(dictTag.has_key(strat)):
                    dictTag[strat] += float(mv)
                else:
                    dictTag[strat] = float(mv)
            return dictTag
        except Exception, e:
            print e
            raise e
        finally:
            #print 'Finalizer called'
            if positionsFile != None :
                positionsFile.close()
    
   
    
    #This function should accept the dictionary and return that max and the min value in the dictionary
    def GetTopandBottomSlices(self, sliceData):
        for security, value in sliceData:
            if value = 
        #what do you think this method should return
        return "Complete the implementation"
            
        
try:
    #how do you want to query this portfolio
    slice = "StrategyDesc"
    measure = "BaseMarketValue"
    portfolioConcentration = PortfolioConcentration()
    tagData = portfolioConcentration.GetMeasureTotalBySlice(slice, measure)
    print tagData
    
except Exception, e:
    print e

print """
    Question 5:
    This firm's exposure to Value Equities is %d
    """, % tagData['Value Equities']
        