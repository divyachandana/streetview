from GPano import *
import GPano
import csv,itertools

def downloadImg(lon,lat,n):
    gpano = GPano.GPano()
    degrees = [60,90,120,240,270,300]
    saved_path = "/Users/divyachandana/Documents/NJIT/work/StreetView/street-images/"
    data = gpano.getPanoJsonfrmLonat(lon, lat)
    # print(data)
    car_pano = data.get("Location")
    car_lat = car_pano.get("lat")
    car_lon = car_pano.get("lng")
    # print(car_lon)
    angle = gpano.getDegreeOfTwoLonlat(lat,lon,float(car_lat),float(car_lon))
    # print(angle)
    # ---------------------------------------------------------------------------
    projection = data.get("Projection")
    pano_yaw_deg = float(projection.get("pano_yaw_deg"))
    # degrees.append(angle)

    find_min = [abs(pano_yaw_deg + deg - angle) for deg in degrees ]
    index = find_min.index(min(find_min))
    # print(data)
    yaw = degrees[index]+pano_yaw_deg
    # if yaw > 360:
    #     yaw = yaw - 360
    # if yaw < 0:
    #     yaw = yaw + 360
    # print(yaw)
    # getDegreeOfTwoLonlat
    image, jpg_name = gpano.getImagefrmAngle(float(car_lon),float(car_lat), saved_path,yaw=yaw,prefix=n)
    url = gpano.getGSV_url_frm_lonlat(float(car_lon),float(car_lat), heading=yaw)
    # print("Google street view URL:", url)
    # print(image)
    # print(jpg_name)
    # ---------------------------------------------------------------------------

#Tree long lat positions as input


# downloadImg(-75.14474465,39.98868215)

def readCSV(n):
    with open("PPR_StreetTrees.csv") as csv_file:

        # csv_reader = csv.reader(csv_file, delimiter=',')
        for row in itertools.islice(csv.DictReader(csv_file), 901,n):
            # print(row['X'], row['Y'])
            downloadImg(row["\ufeffX"],row['Y'],n)
            # each_row = frozenset(row)
            # data.append(each_row)
            # for item in each_row:
            #     itemSet.add(frozenset([item]))
readCSV(1900)

# python3 TreeImages.py