import sys
import os
import fnmatch

commands_dict_file = open("xrdcp_dict.txt", "r")
arg = sys.argv[1]
print "I got the arguments:", arg

for line in commands_dict_file:
  parse = line.split(":::")
  if parse[0] == arg:
    print parse[1].strip()
    os.system(parse[1].strip())
