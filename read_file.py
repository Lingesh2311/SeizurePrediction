'''
Script to read and display information on the EDF files
'''
# Import built-in Packages
import os

# Import 3rd party package
import mne
import xlsxwriter

# Import authorship info
import init


# Read the files
def read_edf():
    path = os.getcwd() + '\\data\\'
    files = []
    print("Reading files...")
    for f in os.listdir(path):
        files.append(mne.io.read_raw_edf(path+f))
        print(f"Reading {f} now..")
    print('Reading successfully completed!')
    return files


# Display the information
def get_info(files):
    for index, item in enumerate(files):
        print(f"> Record Information of patient {index+1}:\n{item.info}")
        print("-"*40)
    print('Information generated!')
    return True

def get_channel_names(files):
    row = 0
    column = 0
    workbook = xlsxwriter.Workbook('Channelnames.xlsx')
    worksheet = workbook.add_worksheet("Names of Channels")    
    for _, item in enumerate(files):
        worksheet.write(row, column, len(item.info['chs']))
        l = 0
        while(l < len(item.info['chs'])):
            worksheet.write(row+l+1, column, item.info['ch_names'][l])
            l += 1
        column += 1
    workbook.close()
    print('Writing Channel Names Complete!')
    return True


if __name__ == "__main__":
    files = read_edf()
    get_info(files)
    get_channel_names(files)
