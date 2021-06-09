#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: Avin

import os,time,re,json,io

alldata = {}
sys_mon = {}


#top => data
topData = {}
#time2sleep = 2.5
#while True:
#print(int(time.time()))
#print(os.popen('top -bin 1').read().split('\n')[2])
topHead = os.popen('top -bin 1').read()
row1 = topHead.split('\n')[0]
cpu_per = topHead.split('\n')[2]
mem = topHead.split('\n')[3]
swap = topHead.split('\n')[4]


running_time = row1.split("up ")[1].split(" days")[0]
load_aver1 = row1.split("load average:")[1].split(",")[0]
load_aver5 = row1.split("load average:")[1].split(",")[1]
load_aver15 = row1.split("load average:")[1].split(",")[2]

topData["load_aver"] = [load_aver1,load_aver5,load_aver15]
topData["running_time"] = running_time

for row in range(2,5):

	key = topHead.split("\n")[row].split(":")[0]
	value = topHead.split("\n")[row].split(":")[1]
	valueList = re.split('[,]',value)

	data = {}

	for id in range(0,len(valueList)):

		childKey = (valueList[id].strip()).split(" ")[1]
		childValue = (valueList[id].strip()).split(" ")[0]

		if row == 4 and id == 2:
			used = (valueList[id].strip()).split(".")[0]
			availMem = (valueList[id].strip()).split(".")[1]
			usedKey = used.split(" ")[1]
			usedVal = used.split(" ")[0]
			availMemVal = availMem.split("avail Mem")[0]
			data[usedKey] = usedVal
			data["avail Mem"] = availMemVal.strip()
		else:
			data[childKey] = childValue
	topData[key] = data

sys_mon['top'] = topData

#df -h => data
dfData = {}
for i in os.popen("df -h"):
	lineData = i.strip().split()
	data = {}
	data["Filesystem"] = lineData[0]
	data["Size"] = lineData[1]
	data["Used"] = lineData[2]
	data["Avail"] = lineData[3]
	data["Use%"] = lineData[4]
	data["Mounted on"] = lineData[5]
	dfData[lineData[0]] = data

sys_mon['df_h'] = dfData
today = time.strftime("%Y%m%d%H", time.localtime())


filename='sys_monitor.json'

file_obj = open(filename,'a+')

json_data = file_obj.readlines()
for line in json_data:
        old_data = json.loads(line.strip())
        for key in old_data:
                alldata[key] = old_data[key]
alldata[today] = sys_mon
alldata = eval(str(alldata).replace("}{",","))
fs = open(filename,'w')
fs.truncate()
fs.close()
json.dump(alldata,file_obj)
file_obj.close()

