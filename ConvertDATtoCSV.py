#Latest version
import subprocess
import re
import os
import sys
import time
import concurrent.futures
import shutil

start_time = time.time()
machine_no=str(1) #Select machine number
file_location = "C:/DAT_file/" + machine_no + "/" #DAT file path
os.chdir(file_location) #Directory path of DAT file location

csv_folder_name = "Machine name" + machine_no
csv_file_location = os.path.abspath(os.curdir) + "/" + csv_folder_name + "/" #Path for saving CSV file

'''Check if CSV folder is existing'''
try:
    os.mkdir(csv_folder_name)
except:
    sys.exit("There's already CSV folder created")

DATlist = os.listdir(file_location) #Create list from file in path (file location)
target_file = []

''' Check DAT file name format -> 2021 11 08 0000 (Float)'''
for line in DATlist:
    regex = re.findall(r"[0-9]{4} [0-9]{2} [0-9]{2} [0-9]{4} \(Float\)", line)
    if len(regex) == 1:
        target_file.append(regex[0])

''' Convert DAT file to CSV file by using FTViewFileViewer.exe program and multi-thread processing'''
def convert_dat_to_csv(file):
    file_name = file
    print('converting... ', file)
    viewer_location = 'C:\FTViewFileViewer.exe'
    dat_location = file_location + file_name + '.dat'
    csv_location = csv_file_location + file_name + '.csv'
    subprocess.run([viewer_location,'/sd', dat_location, csv_location], shell=True)
/
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(convert_dat_to_csv, target_file)

print('Finished in %s seconds' % (round(time.time() - start_time, 3)))
''' Credit : https://github.com/alpacapetter '''

''' Rename file name '''
folder = csv_file_location
for file_name in os.listdir(folder):
    source = folder + file_name
    file_name_date = file_name[0:10]
    destination = folder + 'Machine name' + machine_no + '_' + file_name_date + '.csv'
    os.rename(source, destination)
print('All Files Renamed')
print('New Names are')
res = os.listdir(folder)
print(res)

'''Clear DAT file and CSV folder that's already converted'''
old_path = csv_file_location
dest_path = r'Detination path'
new_path = dest_path + '/' + csv_folder_name
new_path2 = 'C:/Done' + '/' + csv_folder_name

filelist = []
filelist2 = []

files = os.listdir (old_path)
for file_name in files:
    filelist.append(file_name)
    fullpath = old_path + file_name
    shutil.move(os.path.join(old_path,  file_name), os.path.join(new_path, file_name))

file2 = os.listdir(file_location)
for file_name in file2:
    filelist2.append(file_name)
    fullpath = r'C:/Done/Machine name' + machine_no
    shutil.move(os.path.join(file_location,  file_name), os.path.join(new_path2, file_name))

last_path = 'C:/Done/Machine name'+machine_no+'/Machine name#'+machine_no
os.rmdir(last_path) #Deleted folder


print('---------------Completed-----------------')