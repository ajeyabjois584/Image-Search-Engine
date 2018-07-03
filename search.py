from app.colordescriptor import ColorDescriptor
from app.searcher import Searcher
import cv2
import argparse
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required=True, help = "path to index file where image features are stored")
ap.add_argument("-q", "--query", required=True, help = "path to query image" )
ap.add_argument("-r", "--result-path", required=True, help="path to result images")
args = vars(ap.parse_args())

color_descriptor = ColorDescriptor((8, 12, 3))

# read the query image from specified path
query_image = cv2.imread(args["query"])

# extract color features from query image
features = color_descriptor.describe(query_image)

# obtain the searcher object to perform search
searcher = Searcher(args["index"])
results = searcher.search(features)
# results = np.asarray(results)
# print(type(results))

# now display the query image
cv2.imshow("query image",query_image)



# print(type(query_image))
# plt.imshow(query_image)
# plt.show()
result_list = []


for score,resultID in results:
    result = cv2.imread(args["result_path"] + "/" + resultID)
    result_list.append(result)


    # plt.imshow(result)
    # plt.show()
    # cv2.imshow("Result", result)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

for result_image in result_list:
    plt.axis("off")
    plt.imshow(cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB))
    plt.show()

# print(len(result_list))
# plt.imshow(result_list[0])
# plt.imshow(result_list[1])
# plt.imshow(result_list[2])
# plt.imshow(result_list[3])
# plt.imshow(result_list[4])
# plt.imshow(result_list[5])
# plt.imshow(result_list[6])
# plt.imshow(result_list[7])
#
# plt.show()




