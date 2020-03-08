import glob

def xmlcombine(filenames):
    # print(filenames)
    xml_data = ''
    for file in filenames:
        with open('qwert.xml','a') as parentfile:
            with open(file) as childfile:
                for eachline in childfile:
                    parentfile.write(eachline)

filenames = glob.glob('/Users/divyachandana/Documents/NJIT/work/all-imgs/temp/*.xml')
xmlcombine(filenames)