import sys

def timestamp_to_ms(timestr):
  '''
    Converts string formatted as a timestamp to int in ms.
  '''
  # timestamp = HH:MM:SS.(MS*10)
  timestamptuple = timestr.split(":")
  hours = int(timestamptuple[0])
  minutes = int(timestamptuple[1])
  secondstuple = timestamptuple[2].split(".") #SS.(MS*10)
  seconds = int(secondstuple[0])
  milliseconds = int(secondstuple[1])*10
  total_milliseconds = milliseconds+seconds*1000+minutes*60*1000+hours*60*60*1000
  return total_milliseconds

def ms_to_timestamp(ms):
  '''
    Converts ms(int) to string formatted as a timestamp.
  '''
  temp_milliseconds = ms
  hours = temp_milliseconds // (1000*60*60)
  temp_milliseconds -= hours * 1000*60*60
  minutes = temp_milliseconds // (1000*60)
  temp_milliseconds -= minutes * 1000*60
  seconds = temp_milliseconds // 1000
  temp_milliseconds -= seconds * 1000
  milliseconds = temp_milliseconds
  timestampstr = str(hours)+":"+str(minutes).zfill(2)+":"+str(seconds).zfill(2)+"."+str(round(milliseconds/10)).zfill(2)
  return timestampstr

def calc_timestamp_offset(timestr, offset):
  '''
    Calculates and returns a string formatted as timestamp with given offset in ms(int) and original timestamp string.
  '''
  #returns the time with offset for the single subtitle
  timestamp_offset = ms_to_timestamp(timestamp_to_ms(timestr)+offset)
  return timestamp_offset

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
  line = "x"
  while insubfile.readable() and not events_found and line != '':
    line = insubfile.readline()
    outsubfile.write(line+"\n")
    if line.find("[Events]")>-1:
      events_found = True
  if events_found:
    print("Subtitle file detected. Beginning process...")
    while insubfile.readable() and line != '':
      line = insubfile.readline()
      if line.find("Dialogue")>-1:
        timetuple = line[len("Dialogue: "):].split(",")
        timestamp_start = timetuple[1]
        timestamp_end = timetuple[2]
        timestamp_start_offset = calc_timestamp_offset(timestamp_start, offset)
        timestamp_end_offset = calc_timestamp_offset(timestamp_end, offset)
        outsubfile.write("Dialogue: "+timetuple[0]+","+timestamp_start_offset+","+timestamp_end_offset)
        for i in range(3,len(timetuple)):
          outsubfile.write(","+timetuple[i])
        #outsubfile.write("\n")
      else:
        outsubfile.write(line+"\n")
    print("process complete!")
  else:
    print("Subtitle file not valid. Aborting process...")

if __name__ == "__main__":
  main()
