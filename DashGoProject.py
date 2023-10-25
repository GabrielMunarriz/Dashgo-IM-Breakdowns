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
        DashGoCSV_DF = pd.read_csv(DashGoCSV_filename)

        #---Formatting DashGo CSV---
        
        # Formatting -- General
        
        # Remove Duplicate Rows from Self Releases
        DashGoCSV_DF.drop(DashGoCSV_DF[DashGoCSV_DF['Deal Share'] == "0.0%"].index, inplace=True) #I removed these rows because they're duplicates from tracks that I released via self-release. 
                                                                                                  #When self-releasing, rows are duplicated because I am both the label and the artist and a row is created for each "side" of the release.
                                                                                                  #a row X with 0.0% Deal Share is created on the label's side while an identical row X with 100% deal share is created on the artist's side
                                                                                                  #It is this way because I made 100% of royalties go to the artist (Me) for self-releases.
        
        
        # Formatting -- Revenue and Payable Breakdown
        
        # Detailed Breakdown
        RAPB = DashGoCSV_DF.groupby(['Track Title', 'Label Name','Distribution Rate','Deal Share'], as_index=False)[['Net Revenue','Payable']].sum() #Formatting
        RAPB = RAPB.sort_values(by = ['Payable'], ascending=[False]) #Sort
        
        # Summarized Breakdown
        RAPB_Stats = RAPB.sum(numeric_only=True)
        
        if operation == "1":
        
            #---Printing Revenue and Payable Detailed Breakdown---
            #RAPB
            print("Breakdown")
            print(RAPB)
            print(" ") #Line Break

            #---Printing Revenue and Payable Summarized Breakdown---
            
            #RAPB_Stats
            print("Summary")
            print(RAPB_Stats)
            print(" ") #Line Break
            
        elif operation == "2":
            #print ("no operation 2 yet.")
            
            print("")
            RAPB_Payable = RAPB['Payable']
            RAPB_Payable_Labels = RAPB['Track Title']
            
            plt.pie(RAPB_Payable, labels = RAPB_Payable_Labels)
            plt.show()
            

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