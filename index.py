from app.colordescriptor import ColorDescriptor
import argparse
import cv2
import glob

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", help = "path to dataset")
ap.add_argument("-i", "--index", help = "path where index file is created")
args = vars(ap.parse_args())

# creating the object of colordescriptor class
color_descriptor = ColorDescriptor((8, 12, 3))
# writing pixel values of specific region of intrest into csv file
output_file = open(args["index"], "w")

for path in glob.glob(args["dataset"]+ "/*.png"):
    # rfind extracts last occured index

    imageid = path[path.rfind("dataset") + 8:]
    print(imageid)
    image = cv2.imread(path)

    features = color_descriptor.describe(image)

    # since each features will be in floating point value we write it to csv file by converting to string

    features = [str(f) for f in features]
    output_file.write("%s,%s\n" % (imageid, ",".join(features)))

output_file.close()



