import json as J
import dicttoxml
import yaml
with open('sample.json','r') as json_file:
    data_json=J.load(json_file)
#print(data_json)
with open('sample.yaml','w') as yaml_file:
    yaml.dump(data_json,yaml_file,default_flow_style=False)
xml=dicttoxml.dicttoxml(data_json)
with open('sample.xml','w') as xml_file:
    xml_file.write(xml.decode())

    
    
    

