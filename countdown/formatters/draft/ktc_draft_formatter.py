import csv

ktc_in_name = '2023KTC_in.csv'
ktc_out_name = '2023KTC_out.csv'
players_23_file = '2023_players.csv'
players_24_file = '2024_players.csv'

players_23 = []
players_24 = []

with open(players_23_file, 'r') as file23:
    read23 = csv.reader(file23)
    for line in read23:
        string_line = ','.join(map(str,line))
        players_23.append(string_line)

with open(players_24_file, 'r') as file24:
    read24 = csv.reader(file24)
    for line in read24:
        string_line = ','.join(map(str,line))
        players_24.append(string_line)

print(players_24)

# reformat txt file
with open(ktc_in_name, 'r') as ktc_in_file:
    ktc_reader = csv.reader(ktc_in_file)
    with open(ktc_out_name, 'w') as ktc_out_file:
        ktc_writer = csv.writer(ktc_out_file)

        header = ['ovr rank','player', 'position', 'ktc_val', 'year']
        wanted = [0,2,4,8]
        ktc_writer.writerow(header)

        line_count = 0
        curr_csv_line = []
        for line in ktc_reader:
            if(line_count == 10):
                line_count = 0
                curr_csv_line.append(str(curr_year))
                ktc_writer.writerow(curr_csv_line)
                curr_csv_line.clear()
            # if(line_count == 2 or line_count == 4 or line_count == 10):
            if(line_count in wanted):
                string_line = ','.join(map(str,line))
                # print(string_line)
                if(line_count == 2):
                    string_line = string_line[:-3]
                    curr_csv_line.append(string_line)
                    if(string_line in players_23):
                        curr_year = 23
                    else:
                        curr_year = 24
                elif(string_line[0] == 'R' and line_count == 4):
                    curr_csv_line.append('RB')
                elif(string_line[0] == 'W' and line_count == 4):
                    curr_csv_line.append('WR')
                elif(string_line[0] == 'Q' and line_count == 4):
                    curr_csv_line.append('QB')
                elif(string_line[0] == 'T' and line_count == 4):
                    curr_csv_line.append('TE')
                else:
                    curr_csv_line.append(string_line)
            line_count += 1

text = open(ktc_out_name, 'r')
text = ''.join([i for i in text]) \
    .replace('\n\n', '\n')
x = open("ktc_draft.csv",'w')
x.writelines(text)
x.close() 
