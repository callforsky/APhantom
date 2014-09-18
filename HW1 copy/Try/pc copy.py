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
        #Sort the values in the dictionary from smallest to largest
        a = sorted(sliceData.values())
        max, min = a[-1], a[0] #write down the max and min values
        for key in sliceData: # iterate over key values and match the max and mins
            if max == sliceData[key]:
                Max = key
            if min == sliceData[key]:
                Min = key
        #return a list
        return [[Max, max], [Min, min]
        ]
            
        
try:
    #how do you want to query this portfolio
    slice = "StrategyDesc"
    measure = "BaseMarketValue"
    portfolioConcentration = PortfolioConcentration()
    tagData = portfolioConcentration.GetMeasureTotalBySlice(slice, measure)
    #print tagData

    slice = "SecurityDesc"
    measure = "BaseMarketValue"
    portfolioConcentration = PortfolioConcentration()
    tagData2 = portfolioConcentration.GetMeasureTotalBySlice(slice, measure)
    # The codes above creates the tagData2, which is an unordered dictionary
    SecurityInfo = portfolioConcentration.GetTopandBottomSlices(tagData2)
    # The codes above pick up the max and min values from tagData2, and find its
    # corresponding values
    #print SecurityInfo
    #print type(SecurityInfo)
    #print SecurityInfo[1]

    slice = "StrategyDesc"
    measure = "YTDTotalPnL"
    tagData3 = portfolioConcentration.GetMeasureTotalBySlice(slice, measure)
    StrategyInfo = portfolioConcentration.GetTopandBottomSlices(tagData3)
    #print StrategyInfo[0]

    slice = "SecurityTypeDesc"
    measure = "YTDTotalPnL"
    tagData4 = portfolioConcentration.GetMeasureTotalBySlice(slice, measure)
    AssetInfo = portfolioConcentration.GetTopandBottomSlices(tagData4)
    
except Exception, e:
    print e



print """
    Question 5:
    This firm's exposure to Value Equities is 
    """, tagData['Value Equities']

print """
    Question 7:
    The firm's biggest short position is
    """, SecurityInfo[1]

print """
    Question 8: 
    Strategy that is a top performer is
    """, StrategyInfo[0],  " Strategy that is a bottom performer is ", StrategyInfo[1]

print """
    Question 9:
    AssetType is a top performer is
    """, AssetInfo[0], " Asset that is a bottom performer is ", AssetInfo[1]
#a = sorted(tagData.values())
#print a