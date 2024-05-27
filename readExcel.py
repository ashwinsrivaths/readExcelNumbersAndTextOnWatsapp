import pandas as pd
from textMessage import *
import math


def loadCommandFromFile(fileName):
    
    
    
    
    
    
    excelFile = pd.read_excel(fileName, sheet_name="Sheet1")
    
    
    
    

    print(excelFile)

    
    # cmdParentName = dfGeneral["name"][0]
    
    for index, row in excelFile.iterrows():
        if(math.isnan(row["Whatsapp Contact Number"]) == False):
            sendWatsappMessage(row['Name'], int(row['Whatsapp Contact Number']))
            
            # print("///////////////")
            # print(row['Name'])
            # print(int(row['Whatsapp Contact Number']))
            # print("///////////////")
    
    
    
    
#     """
#     Sl no	Name	Whatsapp Contact Number	Mail -ID	Course Taken in ISM	B.E %	
#     Year of passed out	Qualification	Branch	10%	12%	Diploma %	current location	
#     collage Name	relocate?	join immediate?


#     Returns:
#         _type_: _description_
#     """
    
#     # for rowIndex in range [1 , dfDataTypes.shape[0]]:
        
#     #     row = dfDataTypes.loc[rowIndex]
        
#     #     typeName = row["type name"]
#     #     engType = row["eng type"]
#     #     rawType = row["raw type"]
#     #     encoding = row["encoding"]
#     #     engUnit = row["eng unit"]
#     #     calibration = row["calibration"]
#     #     description = row["description"]

#     #     if(abstractFlag == "A"):
#     #         pass
#     #     else:
#     #         if(pd.isnull(commandName) and pd.isnull(argumentName)):
#     #             pass
#     #         elif(pd.isnull(argumentName) and (not pd.isnull(commandName))):
#     #             currentCommand = commandName
#     #             self.dataDict["commands"][commandName] = {"arguments": [], "description": row["description"], "rangeLow": row["range low"], "rangeHigh": row["range high"]}
#     #         elif((not pd.isnull(argumentName)) and pd.isnull(commandName)):
#     #             self.dataDict["commands"][currentCommand]["arguments"].append(argumentName)
#     #         else:
#     #             pass
    
    
    
#     commandNameList = []
#     index = 0
#     for cmd in dfCommands["command name"]:
#         index += 1
#         if(not pd.isnull(cmd)):
#             if(pd.isnull(dfCommands["flags"][index])):
#                 commandNameList.append(cmd)
    
    
    
#     return commandNameList
    
    
#     # returnStr = ""
#     # for cmd in commandNameList:
#     #     returnStr += "\n"
#     #     returnStr += cmd
        
#     # return returnStr
    
    
    
    
#     currentCommand = ''
#     for rowIndex in range [1 , dfCommands.shape[0]]:
        
#         row = dfCommands.loc[rowIndex]
        
#         abstractFlag = row["flags"]
#         commandName = row["command name"]
#         argumentName = row["argument name"]
#         # description = row["description"]
#         # rangeLow = row["range low"]
#         # rangeHigh = row["range high"]

#         if(abstractFlag == "A"):
#             pass
#         else:
#             if(pd.isnull(commandName) and pd.isnull(argumentName)):
#                 pass
#             elif(pd.isnull(argumentName) and (not pd.isnull(commandName))):
#                 currentCommand = commandName
#                 self.dataDict["commands"][commandName] = {"arguments": [], "description": row["description"], "rangeLow": row["range low"], "rangeHigh": row["range high"]}
#             elif((not pd.isnull(argumentName)) and pd.isnull(commandName)):
#                 self.dataDict["commands"][currentCommand]["arguments"].append(argumentName)
#             else:
#                 pass

        

        
# def loadCommandDetails(clickedItem, self):
#     commandDetailsText=""
    
#     # dfGeneral = self.dataDict["dfGeneral"]
#     # dfDataTypes = self.dataDict["dfDataTypes"]
#     dfCommands = self.dataDict["dfCommands"]
    
#     # cmd = dfCommands.loc[dfCommands["command name"] == clickedItem]
#     row_index = dfCommands.index[dfCommands["command name"] == clickedItem].tolist()[0]
#     cmdRow = dfCommands.loc[row_index]
    
    
    
#     cmdColumns = dfCommands.columns
#     index = 0
#     for param in cmdRow:
#         if(not pd.isnull(param)):
#             commandDetailsText = commandDetailsText + cmdColumns[index] + " - " + param + "\n"
#         index += 1
    
#     index = 0
#     row_index += 1
#     commandDetailsText += "\nArguments :- \n"
#     while(row_index < dfCommands.shape[0]):
#         index += 1
#         cmdRow = dfCommands.loc[row_index]
#         if(pd.isnull(cmdRow["command name"])):
#             if(not pd.isnull(cmdRow["argument name"])):
#                 commandDetailsText += "(" + str(index) + ") Argument Name = " + cmdRow["argument name"] + ",  Data Type = " + cmdRow["data type"]
                
#                 if(not pd.isnull(cmdRow["default value"])):
#                     commandDetailsText +=  ",  Default Value = " + str(cmdRow["default value"])
#                 if(not pd.isnull(cmdRow["range low"])):
#                     commandDetailsText += ",  rangeLow = " + str(cmdRow["range low"])
#                 if(not pd.isnull(cmdRow["range high"])):
#                     commandDetailsText += ",  rangeHigh = " + str(cmdRow["range high"])
#                 if(not pd.isnull(cmdRow["description"])):
#                     commandDetailsText += ",  description = " + cmdRow["description"]
                    
#                 commandDetailsText += "\n"

                
#             row_index += 1
#         else:
#             break
    
#     return commandDetailsText
    