import re

filename = 'raw.githubusercontent.com_Secure-Platforms-Lab-W-M_IoTSpotter_main_data_dataset_training_set.txt'
#filename = 'dataset.txt'

def main():
    charset = ''
    with open(filename, 'r') as f:
        for entry in f.readlines():
            pkg_name = re.search(r'"pkg_name": "(\w+\.)*\w+"', entry).group(0)[len('"pkg_name": "'):-1]
            search = re.search(r'"description": "[^"]*"', entry).group(0)[len('"description": "'):-1]
            for char in search:
                if char not in charset:
                    if char == ';' or char == '\\':
                        print(search)
                    charset += char
        f.close()
    print(charset)

if __name__ == '__main__':
    main()