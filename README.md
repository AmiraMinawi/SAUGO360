# SAUGO360(CommunicationParser)
## Prerequisites
1. You should have python 3 installed

2. import csv.  
CSV is a Python library for dealing with csv files.

```bash
pip install python-csv
```
The CSV file used (input.csv) is in the project directory.  
The information in the file should be in the following order: timestamp, src-user, dst-user.  

## How to Run
You can run the python script parse.py in PyCharm.  
If you want to change the file, you can specify the path to your input file in the path variable in the code.

## Functions
### parser(path) Function
The parser(path) function parses the contents of a CSV file containing logs of communication between users.


```python
def parser(path):
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)

        user_map = {}

        for row in csv_reader:
            if row[1] not in user_map:
                user_map.update({row[1]: {}})

            if row[2] not in user_map:
                user_map.update({row[2]: {}})

            user_map.get(row[1]).update({row[2]: row[0]})
            user_map.get(row[2]).update({row[1]: row[0]})

        for key, value in user_map.items():
            print(key, ' : ', value)

        return user_map
```

### write_log_summary(user) Function
The write_log_summary(user) function returns a log summary file showing the peers and latest connection timestamps for each user.

```python
def write_log_summary(user_map):
    f = open("output.log", "w+")

    first_run = True
    new_line = False

    for key in user_map:
        if new_line:
            f.write("\n")

        f.write(key + ": ")

        if first_run:
            key_flag = key
            first_run = False
            first_write = True

        for peers in user_map.get(key):
            if key_flag == key:
                if not first_write:
                        f.write(", ")
            else:
                key_flag = key

            f.write("(" + peers + ", " + user_map.get(key).get(peers) + ")")

            first_write = False
            new_line = True
```

## Input Example
| timestamp | src-user | dst-user  |
|-----------|----------|-----------|
| 1232131   | u123     | u22       |
| 1232132   | u123     | u23       |
| 1232133   | u123     | u23       |

## Expected Output (assuming the data in the input are valid)
```
u123: (u22, 1232131), (u23, 1232133)
u22: (u123, 1232131)
u23: (u123, 1232133)
```
