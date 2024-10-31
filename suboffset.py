import sys

def timestamp_to_ms(timestr):
  # timestamp = HH:MM:SS.(MS*10)
  timestamptuple = timestr.split(":")
  pass

def ms_to_timestamp(ms):
  pass

def calc_timestamp_offset(timestr, offset):
  #returns the time with offset for the single subtitle
  pass

def main():
  #parses the insubfilename, offset in ms and outsubfilename
  #print(sys.argv) #debug
  assert len(sys.argv)==4 #invalid arguments
  insubfilename = sys.argv[1]
  offset = int(sys.argv[2])
  outsubfilename = sys.argv[3]
  #reads the insubfile, copy file until finds "[Events]", then read every line and if finds "Dialogue" converts the timestamp_start and timestamp_end, adds the offsets and finally write the timestamp in the output file and the remenaing line
  insubfile = open(insubfilename, "r")
  outsubfile = open(outsubfilename, "w")
  events_found = False
  while insubfile.readable() and not events_found:
    line = insubfile.readline()
    outsubfile.write(line+"\n")
    if line.find("[Events]")>-1:
      events_found = True
  if events_found:
    print("Subtitle file detected. Beginning process...")
    while insubfile.readable():
      line = insubfile.readline()
      if line.find("Dialogue")>-1:
        timetuple = line[len("Dialogue: "):].split(",")
        timestamp_start = timetuple[1]
        timestamp_end = timetuple[2]
        timestamp_start_offset = calc_timestamp_offset(timestamp_start, offset)
        timestamp_end_offset = calc_timestamp_offset(timestamp_end, offset)
        outsubfile.write("Dialogue: "+timetuple[0]+","+timestamp_start_offset+","+timestamp_end_offset)
        for i in len(timetuple)-3:
          outsubfile.write(","+timetuple[i+3])
        outsubfile.write("\n")
      else:
        outsubfile.write(line+"\n")
    print("process complete!")
  else
    print("Subtitle file not valid. Aborting process...")

if __name__ = "__main__":
  main()
