import sys
import csv
import re
import os

if len(sys.argv) != 3:
    print("Usage:python3 zoomrec.py c:/path/to/file.csv outfile.csv \r\nDownload report csv from https://<ZOOMDOMAIN>/recording/management \r\n")
    print("Warning: Zoom has an export limit of 5000 entrys. If high volume, please narrow down export.",file=sys.stderr)
    exit()

User_info = dict()

with open(sys.argv[1],mode="r",encoding="utf-8") as csvfile:

    '''
    Imports the Recording CSV file
    Finds unique users
    Parses the recording size (Processing Recordings and 0 bytes are ignored)
    Reduce each recording to bytes for accuracy
    Add each recording size to each user
    '''

    csv_reader = csv.reader(csvfile, delimiter=",")
    for line in csv_reader:
        if line[0] not in User_info:
            User_info[line[0]] = int(0)
        size = re.sub("\([0-9]{1,} Files\)|,","",line[4]).split(" ")
        if len(size) != 2:
            continue
        elif size[1] == "GB":
            size[0] = float(size[0])*1073741824 #GB to B
        elif size[1] == "MB":
            size[0] = float(size[0])*1048576 #MB to B
        elif size[1] == "KB":
            size[0] = float(size[0])*1024 #KB to B
        else:
            continue
        User_info[line[0]] = User_info.get(line[0]) + int(size[0])


with open (sys.argv[2],'w') as csvcreate:
    ''' Creates UserRecordingExport.csv file with results '''
    csvcreate.write("email,Size in GB\n")
    for key in User_info.keys():
        try:

            csvcreate.write(f"{key},{round(User_info.get(key)/1073741824,2)}\n")
        except:
            pass
os.system(sys.argv[2])

        
        

