# A collection of Vital related python commands I've created

import json
import os.path

def getPreset(filePath, returnType = {}):
	f = open(filePath, 'r')
	if type(returnType) == dict or returnType == 'dict' or returnType == 'dictionary':
		file = json.load(f)
	elif type(returnType) == str or returnType == 'str' or returnType == 'string':
		file = f.read()
		f.close()
	else:
		file = None
	return file

def writePreset(filePath, data, passExists = False, prettyFile = True, indent = 4):
	pathExists = os.path.exists(filePath)

	if pathExists == True and passExists == True:
		pass
	else:
		if prettyFile == True:
			data = json.dumps(data, indent = indent)
		else:
			data = json.dumps(data)
		f = open(filePath, 'w+')
		f.write(data)
		f.close()

def addNameTag(preset, setTo):
	if type(setTo) == str:
		preset['preset_name'] = setTo
	else:
		raise TypeError('Preset_name was set to something other than a String')
	return preset

def incrementPath(path, appendEnd = True, addUnderscore = True):
	i = 0
	newPath = path
	while os.path.exists(newPath):	
		root = os.path.split(path)[0]
		name = os.path.splitext(os.path.split(path)[1])[0]
		ext = os.path.splitext(os.path.split(path)[1])[1]

		if appendEnd:
			if addUnderscore:
				toAdd = '_' + str(i)
			else:
				toAdd = str(i)
			newPath = os.path.join(root,name+toAdd+ext)
		else:
			if addUnderscore:
				toAdd = str(i) + '_'
			else:
				toAdd = str(i)
			newPath = os.path.join(root,toAdd+name+ext)
		i+=1
	return newPath

def listPresets(dirPath, listNested = False, topDown = True, followLinks = True):
	if os.path.exists(dirPath):
		paths = []
		if listNested == True:
			for root, dirs, files in os.walk(dirPath, topdown = topDown, followlinks = followLinks):
				for i in files:
					if i.endswith('.vital'):
						paths.append(os.path.join(root,i))
		else:
			for files in os.listdir(dirPath):
				if files.endswith('.vital'):
					paths.append(os.path.join(dirPath,files))
		return paths
	else:
		raise FileNotFoundError("File path was not specified or was invalid")

def dirToDict(dirPath, only = (False, ''), ignores = (False, '')):
	d = {}
	for i in [os.path.join(dirPath, i) for i in os.listdir(dirPath) if os.path.isdir(os.path.join(dirPath, i))]:
		d[os.path.basename(i)] = dirToDict(i, only = only, ignores = ignores)
	if only[0] == True:
		d['/files'] = [i for i in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, i)) and os.path.splitext(i)[1] == only[1]]
	elif ignores[0] == True:
		d['/files'] = [i for i in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, i)) and os.path.splitext(i)[1] != ignores[1]]
	else:
		d['/files'] = [i for i in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, i))]
	return d

print(incrementPath("hi\\ok"))