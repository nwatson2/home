import csv
from datetime import date
#get date
today = date.today()
string_date = str(today)
string_date = ''.join([i for i in string_date]) \
    .replace('-', '_')

#file names
draft_out_name = 'draft%s.csv'%(string_date)
ktc_in_name = '2023KTC_in.csv'
ktc_out_name = '2023KTC_out.csv'
players_23_file = '2023_players.csv'
players_24_file = '2024_players.csv'

#initialize
players_23 = []
players_24 = []
rank_23 = 0
rank_24 = 0
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

# reformat csv file
with open(ktc_in_name, 'r') as ktc_in_file:
    ktc_reader = csv.reader(ktc_in_file)
    with open(ktc_out_name, 'w') as ktc_out_file:
        ktc_writer = csv.writer(ktc_out_file)

        header = ['ovr rank','player', 'position', 'ktc_val', 'year', 'year rank']
        wanted = [0,2,4,8]
        ktc_writer.writerow(header)

        line_count = 0
        curr_csv_line = []
        for line in ktc_reader:
            if(line_count == 10):
                line_count = 0
                curr_csv_line.append(str(curr_year))
                if(curr_year == 23):
                    curr_csv_line.append(str(rank_23))
                else:
                    curr_csv_line.append(str(rank_24))
                ktc_writer.writerow(curr_csv_line)
                curr_csv_line.clear()
            if(line_count in wanted):
                string_line = ','.join(map(str,line))
                if(line_count == 2):
                    i=0
                    while(i<5):
                        temp_line = string_line[:-i]
                        if (temp_line in players_23):
                            curr_csv_line.append(temp_line)
                            curr_year = 23
                            rank_23 += 1
                            i=5
                        elif (temp_line in players_24):
                            curr_csv_line.append(temp_line)
                            i=5
                            curr_year = 24
                            rank_24 += 1
                        else:
                            i += 1
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

#get rid of extra \n's
text = open(ktc_out_name, 'r')
text = ''.join([i for i in text]) \
    .replace('\n\n', '\n')
draft_out = open(draft_out_name,'w')
draft_out.writelines(text)
draft_out.close() 
