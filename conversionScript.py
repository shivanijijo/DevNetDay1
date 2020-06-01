import json
import xmltodict
import yaml

f = open('sample.json','r')
inputData = f.read()
dictData = json.loads(inputData)

yamlData = yaml.safe_dump(dictData)
f = open('sample.yml','w')
f.write(yamlData)

xmlData = xmltodict.unparse(dictData)
f = open('sample.xml','w')
f.write(xmlData)


