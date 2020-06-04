"""Program to concatenate all files to form final output

Usage:
    python get_minimax_log_summary.py <lower_date_range in mm:dd;yy> <upper_date_range in mm:dd;yy>
"""
import os
import re
from datetime import datetime
from parse_it import utils


class LogParsing(object):
    def __init__(self, input_dir = None):
        self.input_dir = input_dir
        self._file_name = ""

    @property
    def output_file(self):
        time_stamp = datetime.now().strftime('%m_%d_%Y__%H_%M')
        return f'{self._file_name}_{time_stamp}.csv'

    @output_file.setter
    def output_file(self,file_name):
        if file_name:
            self._file_name = file_name
        else:
            self._file_name = "parsed_file"

    def parse_ifwi_log(self, parse_file_name=""):
        """
        Test on IfWi logfiles and form the table below
                        part_location,status
                        1A1,Pass
                        1A1,Pass
        """
        self.output_file = parse_file_name
        write_file_path = os.path.join(self.input_dir, self.output_file)
        with open(write_file_path, 'w+') as outfile:
            outfile.write(','.join(['part_location', 'status']))
            outfile.write('\n')
        for item in os.listdir(self.input_dir):
            if "IfWi" in item:
                _file_path = os.path.join(self.input_dir, item)
                _search_pattern = '\\s\\d[A-Z]\\d\\s'
                compiled_pattern = re.compile(_search_pattern)
                with open(_file_path, 'r') as f:
                    for line in f:
                        if re.search(compiled_pattern, line):
                            _ll = line.split()  # form list
                            line_to_write = _ll[-2] + "," + _ll[-1]
                            utils.open_given_file_and_append(line_to_write, write_file_path)
        utils.open_file_and_print(write_file_path)

    def parse_minimax_results_log(self, parse_file_name=""):
        """ create(if not exists) and then open a file by given name and write in this format. It also generate list of parts which doesn't have visual id
                                part_location,cpu_visualid,status
                                1D4,D0YB552200589,Pass
                                1D4,D0YB552200589,Pass
                                1A5,None,Pass
        """
        self.output_file = parse_file_name
        write_file_path = os.path.join(self.input_dir, self.output_file)
        with open(write_file_path, 'a') as outfile:
            outfile.write(','.join(['part_location', 'cpu_visualid', 'status']))
            outfile.write(' \n')
        for item in os.listdir(self.input_dir):
            if "results" in item:
                file_path = os.path.join(self.input_dir, item)
                with open(file_path) as f:
                    f.readline()  # readout the first line
                    for line in f:
                        _ll = line.split()
                        if len(_ll) == 3:
                            _ll.insert(1, 'None')
                        line_to_write = _ll[2] + ',' + _ll[1] + ',' + _ll[3]
                        utils.open_given_file_and_append(line_to_write, write_file_path)
        utils.open_file_and_print(write_file_path)

if __name__ == '__main__':
    # arguments =docopt(__doc__)
    # print(arguments)
    minimax_parse = LogParsing()
    minimax_parse.input_dir = "C:\ddey_documents\GitHub_projects\parse_it\Test_folder"
    minimax_parse.parse_minimax_results_log(parse_file_name = "parse_minimax")
    minimax_parse.parse_ifwi_log(parse_file_name = "parse_ifwi")
