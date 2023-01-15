import csv
import pandas as pd

ktc_in_name = '2023KTC_in.csv'
ktc_out_name = '2023KTC_out.csv'

# reformat txt file
with open(ktc_in_name, 'r') as ktc_in_file:
    ktc_reader = csv.reader(ktc_in_file)
    with open(ktc_out_name, 'w') as ktc_out_file:
        ktc_writer = csv.writer(ktc_out_file)

        header = ['ovr rank','player', 'position', 'ktc_val']
        wanted = [0,2,4,10]
        ktc_writer.writerow(header)

        line_count = 0
        curr_csv_line = []
        for line in ktc_reader:
            if(line_count == 12):
                line_count = 0
                ktc_writer.writerow(curr_csv_line)
                curr_csv_line.clear()
            # if(line_count == 2 or line_count == 4 or line_count == 10):
            if(line_count in wanted):
                string_line = ','.join(map(str,line))
                if(string_line[0] == 'R' and line_count == 4):
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