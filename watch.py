#! /usr/bin/env python

# Watch - program to execute commands after a set interval
# Author: Vaidik Kapoor  <kapoor.vaidik@gmail.com>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys, shlex, subprocess, time

'''
Gets command-line arguments
'''
def get_arg(arg, size=1):
  argc = len(sys.argv)

  i = 0
  for i in range(0, argc):
    if sys.argv[i] == arg:
      if size == 0:
        return True

      try:
        arg_val = []
        j = 0
        for j in range(1, size+1):
          arg_val.append(sys.argv[i+j])

        if len(arg_val) > 0:
          return arg_val
      except IndexError:
        print "Error: %s option needs %s value(s) as argument(s)." % (arg, size)
        exit()

  return None

if __name__ == '__main__':
  argl = 1

  help = get_arg('--help', 0)
  if help == True:
    print '''
    Usage: ./watch [options] <cmd>
    \n
    Options:
      --interval <n>		Interval in seconds. Defaults to 2 seconds. Accepts only integers.
      --shell			Prompts user to enter the command instead of passing the command as an argument.
      --help			Print this help information.
    '''
    exit()

  interval = get_arg('--interval')
  try:
    if interval != None:
      interval = int(interval[0])
      argl = argl + 2
    else:
      '''
      Default value of interval is 2 seconds.
      '''
      interval = 2
  except ValueError:
    print "--interval option expects time (integer) in seconds"
    exit()

  shell = get_arg('--shell', 0)
  if shell == True:
    print "Enter command:"
    command = raw_input()
    argl = argl + 1
  else:
    try:
      command = sys.argv[argl]
    except IndexError:
      print "Error: You did not provide a command to execute."
      exit()

  while True:
    try:
      args = shlex.split(command)
      process = subprocess.Popen(args)
      time.sleep(interval)
    except OSError:
      print "Error: The command could not be executed. Check the command you supplied."
      exit()

