import csv

# https://www.youtube.com/watch?v=bkpLhQd6YQM
# There are 2 methods in the video, this uses 2nd method with Dictionaries-


html_output = ''
names = []

with open('files.csv', 'r') as data_file:
    csv_data = csv.DictReader(data_file)


    # print(csv_data) this gives : <csv.DictReader object at 0x0000021A03DC59E8> which is an iterable object

    # Need to print the list: One continuous line of data,
    # print(list(csv_data))

    # to do it line by line we need to iterate over it
    for line in csv_data:
         print(line)
    # If We don't want first line of bad data, use the next command, this jumps over the line, if you want to do it for 2 lines then 2 lines of next(csv_data)
    #      next(csv_data)
#
#     for line in csv_data:
#         if line['FirstName'] == 'No Reward':
#             break
#         names.append(f"{line['FirstName']} {line['LastName']}")
#
# html_output += f'<p>There are currently {len(names)} public contributors. Thank You!</p>'
#
# html_output += '\n<ul>'
#
# for name in names:
#     html_output += f'\n\t<li>{name}</li>'
#
# html_output += '\n</ul>'
#
# print(html_output)