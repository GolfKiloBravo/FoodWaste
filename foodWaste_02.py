# -*- coding: utf-8 -*-
"""
FoodWaste data: treatment and storage routine version 0.1

@author: GKB
NORSUS, January 2021.
Hi Gaylord, i'm testing

"""
# import required modules
import pandas as pd
import os
import numpy as np
import sys
from IPython.display import clear_output
#%%

# function to handle excel files loading
def loadFile(filename, sheet = 'Sheet2'):
    ''' 
    Here are some examples for loading data using this function:

    servingPlaces = loadFile('Database serving places.xlsx')
    matsvin       = loadFile('Mapping tables.xlsx', 'Matsvinn i Matavfall')
    processID     = loadFile('Mapping tables.xlsx', 'Process')
    meadID        = loadFile('Mapping tables.xlsx', 'Meal')

    Check the loaded data

    meadID.head()

    '''
    
    try:
        loadedfile = pd.read_excel(filename, sheet_name=sheet)
        return loadedfile
    
    except:
        print("Something went wrong. Please check for spelling or existing filename!")


# function to handle file restructuration
def restructureFile(filename):
    '''
    An example for restructuring data using the above function:

    processedFile = restructureFile('sammen.xlsx')

    '''
    clear_output()
    try:
        rawFile          = pd.read_excel(filename)
        restructuredFile = rawFile[['Dato','Kjøkken','Frokost Lager Vekt kg','Frokost Tilberedning Vekt kg', 
                     'Frokost Tallerken Vekt kg', 'Frokost Buffet Vekt kg', 'Frokost Gjester', 'Lunsj Lager Vekt kg', 'Lunsj Tilberedning Vekt kg', 
                     'Lunsj Tallerken Vekt kg', 'Lunsj Buffet Vekt kg','Lunsj Gjester', 'Middag Lager Vekt kg', 'Middag Tilberedning Vekt kg', 
                     'Middag Tallerken Vekt kg','Middag Buffet Vekt kg', 'Middag Gjester']]
        
        print("The processed dataset has now {} columns in stead of {}.".format(len(list(restructuredFile.columns)), len(list(rawFile))))
        return restructuredFile
    
    except:
        print("Something went wrong. Please check for spelling or existing filename!")   


# function to handle quick exploration of a given excel file
def quick_fileExploration(filename):
    
    '''
    An example for using the quick-fileExploration function is given below:

    quick_fileExploration('sammen.xlsx')

    '''
    nameOftheCompany = filename.split('.')[0]
    
    try:
        rawFile             = pd.read_excel(filename)
        variablesNumber     = len(list(rawFile.columns))
        dataPoints          = len(rawFile)
        
        print("The variables in the dataset are: \n")
        print(list(rawFile.columns))
        print("\n\nIn total", nameOftheCompany, "has {} columns and {} rows.".format(variablesNumber, dataPoints))
    
    except:
        print("Something went wrong. Please check for spelling or existing filename!")


# data manipulation functions (three functions, each dealing with one specific case

# alternative number One: The kitchen is found and company name is identical with the one found in the serving place database
def pullAndFill(variable):
    
    kept1 = variable.split(" ")[0]                                    
    kept2 = variable.split(" ")[1]                                    
                                      
    Date.append(restructuredFile['Dato'][i])
    SectorKM_ID.append(infoServering['SectorKM_ID'][0])
    CompanyID.append(infoServering['CompanyID'][0])
    Criteria.append(np.nan)
    Food_TypeID.append(np.nan)
    Food_Type.append(np.nan)
    KitchenID.append(infoServering['KitchenID'][0])
    Matsvinn.append(np.nan)
    Meal.append(kept1)
    MealID.append(np.nan)        
    Process.append(kept2.replace('Tilberedning','Produksjon').replace('Gjester', ' '))
    ProcessID.append(np.nan)
    WasteType.append(infoServering['Matsvinn/avfall'][0])
                    
    weightValue = [w if 'Vekt' in c else np.nan for w in [restructuredFile[c][i]]]
    Weight.append(weightValue[0])
                    
    guestNumber = [n if 'Gjester' in c else np.nan for n in [restructuredFile[c][i]]]
    Guests.append(guestNumber[0])
    
# alternative number Two: Kitchen name not found in the serving places, but company name found in the same database
def collectAndProcess(variable):
    
    kept1 = variable.split(" ")[0]                                       
    kept2 = variable.split(" ")[1]                                      
                    
    Date.append(restructuredFile['Dato'][i])
    SectorKM_ID.append(infoServering['SectorKM_ID'][0])
    CompanyID.append(infoServering['CompanyID'][0])
    Criteria.append(np.nan)
    Food_TypeID.append(np.nan)
    Food_Type.append(np.nan)
    KitchenID.append(servingPlaces['KitchenID'][len(servingPlaces) - 1] + 1)
    Matsvinn.append(np.nan)
    Meal.append(kept1)
    MealID.append(np.nan)
    Process.append(kept2.replace('Tilberedning','Produksjon').replace('Gjester', ' '))
    ProcessID.append(np.nan)
    #WasteType.append(infoServering['Matsvinn/avfall'][0])    
                
    weightValue = [w if 'Vekt' in c else np.nan for w in [restructuredFile[c][i]]]
    Weight.append(weightValue[0])
                    
    guestNumber = [n if 'Gjester' in c else np.nan for n in [restructuredFile[c][i]]]
    Guests.append(guestNumber[0])
                          
    print("A new kitchen was found.")
    print("\nIts name is {}.".format(nameOfkitchen))
    print("\nPlease, provide the following information: ")
                       
    matsvinN        = input('Type in Matsvin status 0 (= registers matavfall) or 1 (=registers matsvinn): ')
    WasteType.append(matsvinN.replace('0','Matavfall').replace('1','Matsvinn'))
                
    freqWaste       = input("Please provide the appropriate registration frequency for waste i.e. d = Daily, w = Weekly or m = Monthly: ")
    RegFreq_waste   = []
    RegFreq_waste.append(freqWaste.replace('d','Daily').replace('m', 'Monthly').replace('w','Weekly'))
               
                
    freqGuest       = input("Please provide the appropriate registration frequency for Guest i.e. d = Daily, w = Weekly or m = Monthly: ")
    RegFreq_Guest   = []
    RegFreq_Guest.append(freqGuest.replace('d','Daily').replace('m', 'Monthly').replace('w','Weekly'))
                
    regMethod       = input("Please provide the appropriate registration method i.e. a = App, e = Excel, t = Tool, or w = Waste statistics: ")
    RegMethod       = []
    RegMethod.append(regMethod.replace('a','App').replace('e', 'Excel').replace('t','Tool').replace('w','Waste statistics'))
                
    detailN         = input("Please provide the appropriate level of detail i.e. i = Ingen fordeling, p = Per prossesledd, v = Per varegruppe or vp = Per varegruppe og prossesledd: ")
    Detail          = []
    Detail.append(detailN.replace('i','Ingen fordeling').replace('p', 'Per prossesledd').replace('v','Per varegruppe').replace('vp','Per varegruppe og prossesledd'))
                          
    servingPlaces.loc[len(servingPlaces)] = [KitchenID[-1]] + [infoServering['SectorKM'][0]] + [SectorKM_ID[-1]] + [np.nan] + [np.nan] + [nameOfCompany] + [CompanyID[-1]] + [WasteType[-1]] + [nameOfkitchen] + [RegFreq_waste[-1]] + [RegFreq_Guest[-1]] + [RegMethod[-1]] + [Detail[-1]]    
  
# alternative number Three: Kitchen and company are not found in the serving places. 
def collectAndCompile(variable):
    
    kept1 = variable.split(" ")[0]                                                                     
    kept2 = variable.split(" ")[1]                                                                     
                
    Date.append(restructuredFile['Dato'][i])
    #SectorKM_ID.append(np.nan)
    CompanyID.append(max(servingPlaces.CompanyID) + 1)
    Criteria.append(np.nan)
    Food_TypeID.append(np.nan)
    Food_Type.append(np.nan)
    KitchenID.append(servingPlaces['KitchenID'][len(servingPlaces) - 1] + 1)
    Matsvinn.append(np.nan)
    Meal.append(kept1) # replace total to "" 
    MealID.append(np.nan)
    Process.append(kept2.replace('Tilberedning','Produksjon').replace('Gjester', ' ')) #replace Total to ""? change tilberedning to production when you restructure the file
    ProcessID.append(np.nan)    
                
    weightValue = [w if 'Vekt' in c else np.nan for w in [restructuredFile[c][i]]]
    Weight.append(weightValue[0])
                    
    guestNumber = [n if 'Gjester' in c else np.nan for n in [restructuredFile[c][i]]]
    Guests.append(guestNumber[0])
    
    print("Kitchen name {} and company name {} were not found in serving places database".format(nameOfkitchen, nameOfCompany)) 
    print("\nPlease provide the following information for the new Kitchen:")
    print("1 = Kantine, 2 = Hotel, 3 = Restaurant, 4.1 = Barnehage, 4.2 = Sykehjem, 4.3 = Offentlige Kantiner, 4.4 = Skoler, 4.5 = SFO / AKS, 4.6 = Kommunekjøkken, 4.7 = Sykehus, 4.8 = Grunnskoler")
                
    sectorName      = input('Please provide the appropriate sector:')
    SectorKM        = []
    SectorKM.append(sectorName.replace('1', 'Kantine').replace('3', 'Restaurant').replace('2', 'Hotel').replace('4.2', 'Sykehjem').replace('4.6', 'Kommunekjøkken').replace('4.3', 'Offentlige Kantiner').replace('4.7', 'Sykehus').replace('4.1', 'Barnehage').replace('4.5', 'SFO / AKS').replace('4.4', 'Skoler').replace('4.8', 'Grunnskoler'))
    SectorKM_ID.append(sectorName)   
         
    matsvinN        = input('Key in Matsvin status 0 (= registers matavfall) or 1 (=registers matsvinn): ')
    #Matsvinn.append(matsvinN)
    WasteType.append(matsvinN.replace('0','Matavfall').replace('1','Matsvinn'))
                
    freqWaste       = input("Please provide the appropriate registration frequency for waste i.e. d = Daily, w = Weekly or m = Monthly: ")
    RegFreq_waste   = []
    RegFreq_waste.append(freqWaste.replace('d','Daily').replace('m', 'Monthly').replace('w','Weekly'))
               
                
    freqGuest       = input("Please provide the appropriate registration frequency for Guest i.e. d = Daily, w = Weekly or m = Monthly: ")
    RegFreq_Guest   = []
    RegFreq_Guest.append(freqGuest.replace('d','Daily').replace('m', 'Monthly').replace('w','Weekly'))
                
    regMethod       = input("Please provide the appropriate registration method i.e. a = App, e = Excel, t = Tool, or w = Waste statistics: ")
    RegMethod       = []
    RegMethod.append(regMethod.replace('a','App').replace('e', 'Excel').replace('t','Tool').replace('w','Waste statistics'))
                
    detailN         = input("Please provide the appropriate level of detail i.e. i = Ingen fordeling, p = Per prossesledd, v = Per varegruppe or vp = Per varegruppe og prossesledd: ")
    Detail          = []
    Detail.append(detailN.replace('i','Ingen fordeling').replace('p', 'Per prossesledd').replace('v','Per varegruppe').replace('vp','Per varegruppe og prossesledd'))
    #test pieter
    servingPlaces.loc[len(servingPlaces)] = [KitchenID[-1]] + [SectorKM[-1]] + [SectorKM_ID[-1]] + [np.nan] + [np.nan] + [nameOfCompany] + [CompanyID[-1]] + [WasteType[-1]] + [nameOfkitchen] + [RegFreq_waste[-1]] + [RegFreq_Guest[-1]] + [RegMethod[-1]] + [Detail[-1]]                       
    

# function dealing with cutting and moving all treated files from a source folder to a target folder
def cutAndMoveFiles(sourceFolder, targetFolder):
    '''
    An example for using this function is given below:

    cutAndMoveFiles(source_folder, target_folder)
 
    '''  
    
    try:
        for path, dir, files in os.walk(sourceFolder):
            if files:
                for file in files:
                    if not os.path.isfile(targetFolder + file):
                        os.rename(path + '\\' + file, targetFolder + file)
        print('All required files were successfully moved and deleted')
    
    except Exception as e:
        print(e)

# function to create the factor Table to use incalculating Matsvinn
def createMatsvinnFactorsTable(data_frame):
    
    '''
    An example for using this function is given below:

    Table = createMatsvinnFactorsTable(data_frame)

    ''' 
    data_frame = data_frame.drop(['Offentlig (detail)'], axis='columns') 
    data_frame = data_frame.melt(id_vars=['Gruppe'], value_vars=list(data_frame.columns)[1:])
    data_frame = data_frame.rename(columns={"Gruppe":"SectorID","variable":"Process","value":"Factors"})
    data_frame = data_frame.set_index(["SectorID","Process"])
    
    return data_frame

# function to calculate and fix Matsvinn
def fixMatsvinn(data_frame,Table):
    
    '''
    An example for using this function is given below:

    data_frame = fixMatsvinn(data_frame)

    '''  
    for i in range(0, len(data_frame)):
        
        if data_frame['WasteType'][i].lower() == 'matsvinn':
            data_frame['Matsvinn (kg)'][i] = data_frame['Weight (kg)'][i]
        
        elif data_frame['WasteType'][i].lower() == 'matavfall':
            data_frame['Matsvinn (kg)'][i] = data_frame['Weight (kg)'][i] * Table.loc[data_frame['SectorKM_ID'][i],data_frame['Process'][i]]
        
        else:
            data_frame['Matsvinn (kg)'][i] = data_frame['Weight (kg)'][i] * Table.loc[data_frame['SectorKM_ID'][i], 'Total']
        
    return data_frame

# function to fix the "Criteria 2"
def fixCriteriaTwo(df):
    
    '''
    An example for using this function is given below:

    data_frame = fixCriteriaTwo(data_frame)

    '''  
    
    df['UniqueCode']   = list(zip(df.Date, df.KitchenID))
    df1                = df.groupby(['Date','KitchenID'])[['Matsvinn (kg)','Guests']].apply(sum).reset_index()
    df1['Code']        = list(zip(df1.Date, df1.KitchenID))
    df1['CriteriaTwo'] = np.where((df1['Matsvinn (kg)'] > 0) & (df1['Guests'] > 0), 1, 0)
    
    replacement_map    = {a : b for a, b in zip(list(df1.Code), list(df1.CriteriaTwo) )}
    
    df['criteria 2']   = df['UniqueCode'].map(replacement_map)
    df.drop(['UniqueCode'], axis = 1, inplace = True) 
    
    return df

# The main function
def main():
    # this function runs the program and uses all helper functions to accomplish the intended tasks.
    '''
    To use this function, simply call it as follow:
    
    main()
    
    All helper functions must run before calling the main function.
    '''
    
    Date        = []
    SectorKM_ID = []
    CompanyID   = []
    KitchenID   = []
    Meal        = []
    Process     = []
    Food_TypeID = []
    Food_Type   = []
    Weight      = []
    Guests      = []
    WasteType   = []
    MealID      = []
    Matsvinn    = []
    ProcessID   = []
    Criteria    = []
    
    servingPlaces = loadFile('Database serving places.xlsx')
    matsvin       = loadFile('Mapping tables.xlsx', 'Matsvinn i Matavfall')
    processID     = loadFile('Mapping tables.xlsx', 'Process')
    mealID        = loadFile('Mapping tables.xlsx', 'Meal')
    
    servingPlaces['KitchenName'] = servingPlaces['KitchenName'].astype(str)     
    servingPlaces['Company']     = servingPlaces['Company'].astype(str)
    
    target_folder = r'C:\Users\pgcal\Documents\Python Scripts\Exported' + '\\'             # enter the correct target forlder's path 
    source_folder = r'C:\Users\pgcal\Documents\Python Scripts\WUOW' + '\\'                 # enter the correct source folder's path
    
    for path, dir, files in os.walk(source_folder):
        if files:
            for file in files:
                # get company name
                nameOfCompany = file.split('.')[0]
                # import file and restrcuture it # unique for each possibility to deliver data (dependent on folder name)
                restructuredFile            = restructureFile(path+file)
                restructuredFile['Kjøkken'] = restructuredFile['Kjøkken'].astype(str)
                #variable = list(restructuredFile.columns[2:])
            
                
                
                for i, row in restructuredFile.iterrows():
                    for c in restructuredFile.columns[2:]:
                        check = restructuredFile[c][i]
                        if check > 0:
                            nameOfkitchen = restructuredFile['Kjøkken'][i]
                            
                            if nameOfkitchen in servingPlaces['KitchenName'].values:
                                infoServering = servingPlaces[servingPlaces['KitchenName'].isin([nameOfkitchen])].reset_index()
                                
                                if infoServering['Company'].iloc[0].lower() == nameOfCompany.lower():
                                    pullAndFill(c)
                                    
                                else:
                                    print('Kitchenname found in the serving place database')
                                    print('The program has stopped completely due to Company name in the file not matching the one found in the serving place database')
                                    print('The company name found in the serving places is: ', infoServering['Company'].iloc[0])
                                    print('The company name found in the file is: ', nameOfCompany)
                                    print('Please, consider manual tunning to fix the issue! This may be caused by the followings:')
                                    print(' 1. Filename is written wrong')
                                    print(' 2. Kitchen name (', nameOfkitchen,') is already used by another company (', infoServering['Company'].iloc[0],') consider changing the kithenname')
                    
                                    sys.exit('Company name issue needs to be fixed!')
                        
                            elif nameOfCompany in servingPlaces['Company'].values:
                                infoServering = servingPlaces[servingPlaces['Company'].isin([nameOfCompany])].reset_index()
                                collectAndProcess(c)
                            
                            else:
                                collectAndCompile(c)
 #%%                               
        cutAndMoveFiles(source_folder, target_folder)      
    
    # collect all data into a dataframe
    collection  = pd.DataFrame(
    {
     
     'Date'         :Date,
     'SectorKM_ID'  :SectorKM_ID,
     'CompanyID'    :CompanyID,
     'KitchenID'    :KitchenID,
     'Meal'         :Meal,
     'Process'      :Process,
     'Food_TypeID'  :Food_TypeID,
     'Food_Type'    :Food_Type,
     'Weight (kg)'  :Weight,
     'Guests'       :Guests,
     'WasteType'    :WasteType,
     'Matsvinn (kg)':Matsvinn,
     'ProcessID'    :ProcessID,
     'MealID'       :MealID,
     'criteria 2'   :Criteria
     
     })  
    
    # update non collected information
    
    # fill in processID
    capitalizer             = lambda x: x.upper()
    collection['Process']   = collection['Process'].apply(capitalizer)
    replacement_map         = {a : b for a, b in zip(list(processID.current.apply(capitalizer)), list(processID.ID) )}
    collection['ProcessID'] = collection['Process'].map(replacement_map)
    
    # fill in mealID
    collection['Meal']      = collection['Meal'].apply(capitalizer)
    replacement_map         = {a : b for a, b in zip(list(mealID.Current.apply(capitalizer)), list(mealID.ID) )}
    collection['MealID']    = collection['Meal'].map(replacement_map)
    
    # fill in Matsvinn
    # first create the matsvinn Table
    Table = createMatsvinnFactorsTable(matsvin)
    # use the Table to populate the Matsvinn variable 
    collection = fixMatsvinn(collection, Table)
    
    # fill in criteria 2
    collection = fixCriteriaTwo(collection)
    
    
    # here we can add a function to export everything to sql. But I want you first to test the program for debugging.
    # the project is over here for WUOW as the main data framework. e-smiley will be easy to integrate 
    # into this program (just one or two-stage function). We can also get the functions to methods i.e. into a class for OOP.
    
    


































































































































































