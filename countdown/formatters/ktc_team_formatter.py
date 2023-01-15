import csv
import pandas as pd

ktc_in_name = 'team_in.csv'
ktc_out_name = 'team_out.csv'

# reformat txt file
with open(ktc_in_name, 'r') as ktc_in_file:
    ktc_reader = csv.reader(ktc_in_file)
    with open(ktc_out_name, 'w') as ktc_out_file:
        ktc_writer = csv.writer(ktc_out_file)

        header = ['ovr rank','player', 'position', 'ktc_val']
        ktc_writer.writerow(header)
# change to a list of wanted indexes and then do "in"
        line_count = 0
        max_lines = 8
        curr_csv_line = []
        wanted = [0,2,4,6]
        for line in ktc_reader:
            if(line_count == max_lines):
                line_count = 0
                ktc_writer.writerow(curr_csv_line)
                curr_csv_line.clear()
            if(line_count in wanted):
                string_line = ','.join(map(str,line))
                curr_csv_line.append(string_line)
            line_count += 1