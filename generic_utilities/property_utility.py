path = r'C:\Users\Ramya\PycharmProjects\POM-M15-Oct9-7AM\external_files\property_file.txt'

def property_data():
    with open(path) as file:
        d = {}
        for line in file:
            if '=' in line:
                key, value = line.strip().split('=')
                d[key] = value
        return d

res = property_data()
print(res)

























