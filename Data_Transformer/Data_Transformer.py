import json

from ruamel.yaml import YAML

#Specify safe mode, as default round trip has a vunerability with unregistered tags.
yaml = YAML(typ='safe') 
yaml.default_flow_style = False #Make the output more readable.

#Convert a yaml file to json format.
def YAML_to_JSON(in_file):

    #Split in_file name at the '.' to get the prefix from a temporary list.
    temp_list = in_file.split('.')
    out_file = temp_list[0]

    #Append .json extension to the out file name to preserve the original name.
    out_file += ".json"

    #Open and load the input file into a dictionary.
    with open(in_file, "r", encoding = "utf-8") as input_pointer:
        data = yaml.load(input_pointer)

    #Create/open output file and dump data from the dictionnary loaded from yaml file.
    with open(out_file, "w", encoding = "utf-8") as output_pointer:
        json.dump(data, output_pointer, indent=4, ensure_ascii=False)

#Convert a json file to yaml format.
def JSON_to_YAML(in_file):
    #Split in_file name at the '.' to get the prefix from a temporary list>
    temp_list = in_file.split('.')
    out_file = temp_list[0]

    #Append .json extension to the out file name to preserve the original name.
    out_file += ".yaml"

    #Open in_file and load data into a dictionary
    with open(in_file, "r", encoding = "utf-8") as input_pointer:
        data = json.load(input_pointer)

    #Create/open output file and dump data from the dictionnary loaded from json file.
    with open(out_file, "w", encoding = "utf-8") as output_pointer:
        yaml.dump(data, output_pointer)

#simple driver for the sake of demonstration.
def main():
    YAML_to_JSON("yamltojson.yaml")
    JSON_to_YAML("jsontoyaml.json")

if __name__ == "__main__":
    main()


    