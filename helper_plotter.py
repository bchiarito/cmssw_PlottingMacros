import sys
import os

fi = open(sys.argv[1])

print "Unchanging full options:"
unchanging = fi.readline().strip()
print unchanging

print "\nChanging options:"
changing_options = fi.readline().split()
print changing_options

print "\nCommands:"
commands = []
for line in fi:
  choices = line.split()
  if len(choices) != len(changing_options):
    continue

  command = "python plotting/plotter.py "
  command += unchanging+" "
  for i in range(len(changing_options)):
    command += changing_options[i] + " " + choices[i]+ " "
  print command
  commands.append(command)

print "\nRun commands? [y]"
response = raw_input()
if response == "y":
  for command in commands:
    os.system(command)
