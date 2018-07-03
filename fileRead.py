import sys

filename = "poi_emails.py"

with open(filename) as f:
  while True:
    c = f.read(1)
    if not c:
      print "End of file"
      break
    if c == '\n':
        sys.stdout.write('\n!$!')
    else:
        sys.stdout.write(c)