import pandas as pd
import numpy as np
#from sklearn.impute import SimpleImputer

#---While Loop---
continueLoop = True

while continueLoop:
    
    #---User Input---
    distributionService = input("Choose Distribution Service (DashGo or IdentityMusic): ")
    artistName = input("Specify Artist Name: ")
    month = input("Choose Month (MM): ")
    year = input("Choose Year (YY): ")


    if distributionService.upper() == "DG" or "DASHGO":

        #---Create Filename String---
        #Format: artistname-MM-YY.csv (e.g. landq-09-23.csv)
        DashGoCSV_filename = artistName + "-"
        DashGoCSV_filename = DashGoCSV_filename + month + "-"
        DashGoCSV_filename = DashGoCSV_filename + year + ".csv"

        #---Read Filename---
        DashGoCSV = pd.read_csv(DashGoCSV_filename)

        #---Formatting DashGo CSV (Generalized)---
        #Remove Duplicate Rows from Self Releases
        DashGoCSV.drop(DashGoCSV[DashGoCSV['Deal Share'] == "0.0%"].index, inplace=True) #I removed these rows because they're duplicates from tracks that I released via self-release. 
                                                                                         #When self-releasing, rows are duplicated because I am both the label and the artist and a row is created for each "side" of the release.
                                                                                         #a row X with 0.0% Deal Share is created on the label's side while an identical row X with 100% deal share is created on the artist's side
                                                                                         #It is this way because I made 100% of royalties go to the artist (Me) for self-releases.

        #---Revenue and Payable Breakdown---
        RAPB = DashGoCSV.groupby(['Track Title', 'Label Name','Distribution Rate','Deal Share'])[['Net Revenue','Payable']].sum() #Formatting
        RAPB = RAPB.sort_values(by = ['Payable'], ascending=[False]) #Sort
        #RAPB
        print("Breakdown")
        print(RAPB)

        print(" ") #Line Break

        #---Revenue and Payable Summary---
        RAPB_Stats = RAPB.sum()
        #RAPB_Stats
        print("Summary")
        print(RAPB_Stats)

    elif distributionService.upper() == "IM" or "IDENTITYMUSIC":
        print("No IdentityMusic Functionality yet")
    
    print(" ") #Line Break
    print(" ") #Line Break

    #Ask to continue analyzing files or not.
    continueLoop_Query = input("Would you like to break down another file (Y/N)?: ")
    
    if continueLoop_Query.upper() == "Y":
        continueLoop = True
    elif continueLoop_Query.upper() == "N":
        continueLoop = False