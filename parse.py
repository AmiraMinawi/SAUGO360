import csv
path = 'input.csv'  # from here you can change the csv file in the parser function


def parser(path):
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)

        user_map = {}

        for row in csv_reader:
            if row[1] == "" or row[2] == "" or row[0] == "":  # if there is an empty cell in the row
                break   # skip to the next row
            else:
                if row[1] not in user_map:
                    user_map.update({row[1]: {}})

                if row[2] not in user_map:
                    user_map.update({row[2]: {}})

                user_map.get(row[1]).update({row[2]: row[0]})
                user_map.get(row[2]).update({row[1]: row[0]})

        for key, value in user_map.items():
            print(key, ' : ', value)

        return user_map


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


user = parser(path)
write_log_summary(user)











