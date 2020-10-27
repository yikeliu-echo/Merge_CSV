import pandas as pd
import os

Folder_Path = r'C:\Users\Admin\Desktop\spotify indonesia playlist'  # Folder path to be spliced, be careful not to include Chinese
SaveFile_Path = r'C:\Users\Admin\Desktop'  # File path to be saved after splicing
SaveFile_Name = r'SpotifyIndonesiaPlaylist.csv'  # File name to be saved after merging


# Modify current working path
os.chdir(Folder_Path)
# Save all file names in this folder into a list
file_list = os.listdir()

# Read the first CSV file and include the header and add a new column to include the filename
df = pd.read_csv(Folder_Path + '\\' + file_list[0])  # 编码默认UTF-8，若乱码自行更改
df["Playlist Name"] = os.path.splitext(file_list[0])[0]
# Write the first CSV file into the merged file and save
df.to_csv(SaveFile_Path + '\\' + SaveFile_Name, encoding="utf_8_sig", index=False)

# Loop through each CSV file name in the list and append to the merged file
for i in range(1, len(file_list)):
    df = pd.read_csv(Folder_Path + '\\' + file_list[i])
    df["Playlist Name"] = os.path.splitext(file_list[i])[0]
    df.to_csv(SaveFile_Path + '\\' + SaveFile_Name, encoding="utf_8_sig", index=False, header=False, mode='a+')