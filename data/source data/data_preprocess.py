

import os
import pandas as pd

def precoess(file_name):

	columns = ["Max TemperatureF","Mean TemperatureF", "Min TemperatureF", "Max Humidity"," Mean Humidity"," Min Humidity", " Mean Sea Level PressureIn", " Mean Wind SpeedMPH", " CloudCover", " Events"]

	month = file_name.split(".")[0].split("-")[-1]

	data = pd.read_csv(file_name)

	m, n = data.shape

	cdt = pd.Series([str(month)] * m)

	new_d = data[columns]

	new_d.insert(0, 'CDT', cdt)

	new_d.to_csv(file_name.split(".")[0] + '-out.csv', index=False)


def main():

	# read files list from folder "dataset"
	#path = "/Users/Songbingyu17/Desktop/dataset"
	#files = os.listdir(path)
#l = []

	for filename in os.listdir(r'/Users/Songbingyu17/Documents/584/project/weather/dataset')[1:]:
		# print(filename)
		if filename.startswith("20"):
			print("Process file %s" %filename)
			precoess(filename)

	# Done

if __name__ == "__main__":
	main()
	# precoess("dataset/2016-4.txt")
