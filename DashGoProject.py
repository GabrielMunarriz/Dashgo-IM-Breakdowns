import pandas as pd
import numpy as np
#from sklearn.impute import SimpleImputer

#---Import DashGo CSV---
DGCSV_filename = input("Input DashGo Filename (Format: landq-MM-YY.csv): ")
DGCSV = pd.read_csv(DGCSV_filename)

#---Format DashGo CSV---
#Remove Columns
#DGCSV.drop(columns=['UPC','VideoId','ChannelId','ISRC','Label Track ID']) #I removed these columns because they aren't relevant for finding "Payable"
#Remove Rows
DGCSV.drop(DGCSV[DGCSV['Deal Share'] == "0.0%"].index, inplace=True) #I removed these rows because they're duplicates from tracks that I released via self-release. 
                                                            #When self-releasing, rows are duplicated because I am both the label and the artist and a row is created for each "side" of the release.
                                                            #a row X with 0.0% Deal Share is created on the label's side while an identical row X with 100% deal share is created on the artist's side
                                                            #It is this way because I made 100% of royalties go to the artist (Me) during self-releases.
                                          
#---Revenue and Payable Breakdown---
RAPB = DGCSV.groupby(['Track Title', 'Label Name','Distribution Rate','Deal Share'])[['Net Revenue','Payable']].sum()
RAPB = RAPB.sort_values(by = ['Payable'], ascending=[False])
RAPB_Stats = RAPB.sum()

#RAPB #Shows Breakdown
print("Breakdown")
print(RAPB)

print(" ")

#RAPB_Stats #Shows Sums
print("Summary")
print(RAPB_Stats)