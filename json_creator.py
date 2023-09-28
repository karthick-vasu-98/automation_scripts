
import os
import re
import json


def is_valid_json_key(key_name):
    try:
        json.loads('{"' + key_name + '": null}')
        return True
    except:
        return False


def validate_set_key_datatype(key_datatype):
    result = False
    d_type = None
    try:
        if key_datatype == 1:
            d_type = 'str'
        elif key_datatype == 2:
            d_type = 'int'
        elif key_datatype == 3:
            d_type = 'list'
        elif key_datatype == 4:
            d_type = 'dict'
        elif key_datatype == 5:
            d_type = 'boolean'

        if d_type:
            result = True
    except Exception as e:
        print('Exception :', e)
    return result, d_type


def get_json_obj_key():
    key_obj_list = list()
    num_of_keys = int(input('Enter the number of keys should present inside each json objects : '))
    key_data_type_help_text = '''Set the datatype of the json key. Enter 1 for String
                                        2 for Integer
                                        3 for List
                                        4 for Dict
                                        5 for Boolean'''
    try:
        for key in range(0, num_of_keys):
            key_obj = dict()
            j_key_obj = None
            key_name = str(input('Enter the key in a valid json key format : '))
            if not is_valid_json_key(key_name):
                raise Exception('Given key name is not in the valid json key naming format')
            if key == 0:
                print(f"{key_data_type_help_text}")
            key_data_type = int(input('Enter the datetype option : '))
            result, d_type = validate_set_key_datatype(key_data_type)
            if not result:
                raise Exception('Given key datatype is not valid')
            if d_type == 'dict':
                j_key_obj = get_json_obj_key()
            key_obj["key_name"] = key_name
            key_obj["key_type"] = d_type
            key_obj["j_key_obj"] = j_key_obj
            key_obj_list.append(key_obj)
    except Exception as e:
        print('Error :', e)
    return key_obj_list


def create_json(len_json, key_obj):
    json_obj = {}
    try:
        pass
        #NOTE: TODO
    except Exception as e:
        print('Error :', e)
    return json_obj


if __name__ == "__main__":
    current_directory = os.getcwd()
    len_json = int(input('Enter the number of json objects should present in the json : '))
    key_obj = get_json_obj_key()
    json_obj = create_json(len_json, key_obj)