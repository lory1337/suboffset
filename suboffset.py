import sys

def timestamp_to_ms(timestr):
  pass

def ms_to_timestamp(ms):
  pass

def calctime(timestr, offset):
  #returns the time with offset for the single subtitle
  pass

#parses the insubfilename, offset in ms and outsubfilename
#print(sys.argv) #debug
assert len(sys.argv)==4 #invalid arguments
insubfilename = sys.argv[1]
offset = int(sys.argv[2])
outsubfilename = sys.argv[3]

#reads the insubfile, copy file until finds "[Events]", then read every line and if finds "Dialogue" converts the timestamp_start and timestamp_end, adds the offsets and finally write the timestamp in the output file and the remenaing line
