import pandas as pd

def to_dataset(spreadsheet, columns=[], outfile='dataset.txt'):
    print(f'Creating dataset from {spreadsheet}')
    usecols = list(range(len(columns))) if len(columns) > 0 else None
    df = pd.read_excel(spreadsheet, usecols=usecols)
    df.columns = columns
    print(df)
    with open(outfile, 'w') as f:
        for ind in df.index:
            entry = f'{"{"}"{columns[0]}": "{df[columns[0]][ind]}", '
            for column in columns[1:-1]:
                cleaned_value = str(df[column][ind].encode('ascii', 'ignore').decode())
                cleaned_value = cleaned_value.replace('\n', '').replace('"', '')
                cleaned_value = cleaned_value.lower()
                entry += f'"{column}": "{cleaned_value}", '
            entry += f'{columns[-1]}: {df[columns[-1]][ind]}{"}"}\n'
            f.write(entry)
        f.close()

def main():
    spreadsheet = 'medical_app_vetting.xlsx'
    columns = ['pkg_name', 'description', 'label']
    to_dataset(spreadsheet, columns)

if __name__ == '__main__':
    main()
