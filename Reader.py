
def maxMalay():
	data = open("data.txt", "r")
	maxPop = 0
	year = 0
	for line in data:
		if "Total Malays" in line:
			x = line.split(",")
			pop = (x[2])
			if pop > maxPop:
				maxPop = pop
				year = x[0]
	print ("Highest population of Malays = " + maxPop + " in " + year)

def maxChinese():
	data = open("data.txt", "r")
	maxPop = 0
	year = 0
	for line in data:
		if "Total Chinese" in line:
			x = line.split(",")
			pop = (x[2])
			if pop > maxPop:
				maxPop = pop
				year = x[0]
	print ("Highest population of Chinese = " + maxPop + " in " + year)

def maxIndians():
	data = open("data.txt", "r")
	maxPop = 0
	year = 0
	for line in data:
		if "Total Indians" in line:
			x = line.split(",")
			pop = (x[2])
			if pop > maxPop:
				maxPop = pop
				year = x[0]
	print ("Highest population of Indians = " + maxPop + " in " + year)

def maxOtherEthnicGroups():
	data = open("data.txt", "r")
	maxPop = 0
	year = 0
	for line in data:
		if "Other Ethnic Groups (Total)" in line:
			x = line.split(",")
			pop = (x[2])
			if pop > maxPop:
				maxPop = pop
				year = x[0]
	print ("Highest population of other ethnic groups = " + maxPop + " in " + year)

def getCitizensInYear(year):
	data = open("data.txt", "r")
	for line in data:
		if str(year) in line:
			if "Total Citizen" in line:
				x = line.split(",")
				pop = (x[2])
				print pop

def maxCitizenAnnualGrowth():
	maxGrowthRate = 0
	maxGrowthYear = 0
	minGrowthRate = 0
	minGrowthYear = 0
	dic = {}
	count = 0
	data = open("data.txt", "r")
	for line in data:
		if "Total Citizen" in line:
			x = line.split(",")
			dic[x[0]] = x[2]
	sortedDic = (sorted(dic))	
	for key in dic:
		if int(sortedDic[count]) >= 1991 and int(sortedDic[count]) <= 2018:
			popNow = float(dic[sortedDic[count]])
			popLast = float(dic[sortedDic[count-1]])
			growthRate = ((popNow - popLast) / popLast)
			if growthRate > maxGrowthRate:
				maxGrowthRate = growthRate
				maxGrowthYear = sortedDic[count]
			elif growthRate < minGrowthRate:
				minGrowthRate = growthRate
				minGrowthYear = sortedDic[count]
		count = count + 1
	print (str(maxGrowthRate) + " in " + maxGrowthYear)
	print (str(minGrowthRate) + " in " + minGrowthYear)

maxCitizenAnnualGrowth()
