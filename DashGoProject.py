import pandas as pd
import numpy as np
#from sklearn.impute import SimpleImputer

#---User Input---
DistributionService = input("Choose Distribution Service (DashGo or IdentityMusic): ")
Month = input("Choose Month (MM): ")
Year = input("Choose Year (YY): ")

#---Create Filename String---
if DistributionService.upper() == "DG" or "DASHGO":
    DashGoCSV_filename = "landq-"
    DashGoCSV_filename = DashGoCSV_filename + Month + "-"
    DashGoCSV_filename = DashGoCSV_filename + Year + ".csv"
elif DistributionService.upper() == "IM" or "IDENTITYMUSIC":
    print("No IdentityMusic Functionality yet")

#---Create Breakdowns---
if DistributionService.upper() == "DG" or "DASHGO":
    
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
    
    print(" ")
    
    #---Revenue and Payable Summary---
    RAPB_Stats = RAPB.sum()
    #RAPB_Stats
    print("Summary")
    print(RAPB_Stats)