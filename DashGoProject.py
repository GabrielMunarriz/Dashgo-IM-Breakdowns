import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from sklearn.impute import SimpleImputer

#---While Loop---
continueLoop = True

while continueLoop:
    
    #---Welcome Message---
    print("--Music Royalties Statement Analyzer--")
    print(" ") #Line Break
    print("Choose Distribution Service and Operation through corresponding number.")
    print(" ") #Line Break
    print("--Current Distribution Services--")
    print("'1' - DashGo.")
    print("'2' - IdentityMusic.")
    print(" ") #Line Break
    print("--Current Operations--")
    print("'1' - Show Breakdown.")
    print("'2' - Show Pie Chart.")
    print(" ") #Line Break
    
    #---User Input---
    distributionService = input("Choose Distribution Service: ")
    operation = input("Choose Operation: ")
    artistName = input("Specify Artist Name: ")
    month = input("Choose Month (MM): ")
    year = input("Choose Year (YY): ")

    #--DashGo--
    if distributionService == "1":

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
        
        if operation == "1":
        
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
            
        elif operation == "2":
            print ("no operation 2 yet.")

    #--IdentityMusic--
    elif distributionService == "2":
        
        print("No IdentityMusic Functionality yet")
    
    print(" ") #Line Break
    print(" ") #Line Break

    #Ask to continue analyzing files or not.
    continueLoop_Query = input("Would you like to break down another file (Y/N)?: ")
    print(" ") #Line Break
    
    if continueLoop_Query.upper() == "Y":
        continueLoop = True
    elif continueLoop_Query.upper() == "N":
        continueLoop = False