import glob
import re
def xmlToRbox(filenames):
    substrs = ["<cx>","<cy>","<w>","<h>","<angle>"]
    replace_list = ["<cx>","</cx>","<cy>","</cy>","<w>","</w>","<h>","</h>","<angle>","</angle>"]
    for file in filenames:
        finalname = file+'.rbox'
        with open(finalname,'a') as parentfile:
            with open(file) as childfile:
                final_write_data = []
                for eachline in childfile:
                    if any(x in eachline for x in substrs):
                        if "<angle>" in eachline:
                            final_write_data.append("1")
                            eachline = re.sub(r'|'.join(map(re.escape, replace_list)), '', eachline)
                            final_write_data.append(eachline.strip())
                            # final_write_data.append("\n")
                        else :
                            eachline = re.sub(r'|'.join(map(re.escape, replace_list)), '', eachline)
                            final_write_data.append(eachline.strip())
                        # print(eachline)
                        # parentfile.write(eachline)
                if len(final_write_data)>0:
                    # print("\t".join(final_write_data))
                    parentfile.write("\t".join(final_write_data))


filenames = glob.glob('/Users/divyachandana/Documents/NJIT/work/all-imgs/temp/*.xml')
xmlToRbox(filenames)
