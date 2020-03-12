import glob
import os
def Form_train_data(rbox_names,image_names):
    # print(rbox_names)
    # print(image_names)
    rbox_f = []
    img_f = []
    for link in rbox_names:
        rbox_f.append(os.path.basename(link))
    for link in image_names:
        img_f.append(os.path.basename(link))
    # print(rbox_f)
    # print(img_f)
    with open("input.txt", 'a') as output:
        for r in rbox_f:
            trim_rbox = r.replace("xml.rbox","jpg")
            idx =img_f.index(trim_rbox)
            if(idx >=0) :
                # print(img_f[idx] + " " +r)
                output.write(img_f[idx] + " " +r)
                output.write("\n")



rbox_names = glob.glob('/Users/divyachandana/Documents/NJIT/work/all-imgs/temp/*.rbox')
image_names = glob.glob('/Users/divyachandana/Documents/NJIT/work/all-imgs/temp/*.jpg')
Form_train_data(rbox_names,image_names)
