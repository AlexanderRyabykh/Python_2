import yaml


def save_to_yaml(to_list, number, some_dict):
    output = {'to_list': to_list, 'number': number, 'some_dict': some_dict}
    with open('new_file.yaml', 'w') as f:
        yaml.dump(output, f, default_flow_style=False)


save_to_yaml([1, 2, 3], 25, {'a': 'abba', 'b': 'papa'})


with open('new_file.yaml') as f:
    print(f.read())