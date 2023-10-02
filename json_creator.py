import os
import json
import string
import random


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


def generate_string_data():
    length = random.randint(1, 20)
    characters = string.ascii_letters + string.digits
    string_data = ''.join(random.choice(characters) for _ in range(length))
    return string_data


def generate_int_data():
    int_data = random.randint(1, 20)
    return int_data


def generate_list_data():
    type_list = ['int', 'str']
    list_data = list()
    length = random.randint(1, 50)
    list_type = random.choice(type_list)
    for _ in range(length):
        if list_type == 'str':
            list_data.append(generate_string_data())
        else:
            list_data.append(generate_int_data())
    return list_data


def generate_dict_data(dict_obj=None):
    dict_data = generate_json_obj(dict_obj)
    return dict_data


def generate_bool_data():
    bool_data = random.choice([True, False])
    return bool_data


def generate_json_obj(key_obj):
    data = dict()
    try:
        for key in key_obj:
            generated_data = None
            if key['key_type'] == 'str':
                generated_data = generate_string_data()
            if key['key_type'] == 'int':
                generated_data = generate_int_data()
            if key['key_type'] == 'list':
                generated_data = generate_list_data()
            if key['key_type'] == 'dict':
                generated_data = generate_dict_data(dict_obj=key['j_key_obj'])
            if key['key_type'] == 'boolean':
                generated_data = generate_bool_data()
            data[key['key_name']] = generated_data
    except Exception as e:
        print('Error :', e)
    return data


def create_json(len_json, key_obj):
    json_obj = list()
    try:
        for i in range(0, len_json):
            json_obj.append(generate_json_obj(key_obj))
    except Exception as e:
        print('Error :', e)
    return json_obj


def create_unique_file_path(path='.'):
    counter = 0
    while True:
        file_name = f"data_{counter}.json"
        file_path = os.path.join(path, file_name)
        if not os.path.exists(file_path):
            return file_path
        counter += 1


def create_json_file(json_obj, path):
    result = False
    msg = 'Error occured while writing file'
    try:
        file_path = create_unique_file_path(path=path)
        with open(file_path, 'w') as json_file:
            json.dump(json_obj, json_file)
            result = True
            msg = f'File created at {file_path}'
    except Exception as e:
        print('Error :', e)
    return result, msg


if __name__ == "__main__":
    current_directory = os.getcwd()
    len_json = int(input('Enter the number of json objects should present in the json : '))
    key_obj = get_json_obj_key()
    json_obj = create_json(len_json, key_obj)
    result, msg = create_json_file(json_obj, current_directory)
    print(msg)