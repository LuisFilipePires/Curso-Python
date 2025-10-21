


print("Standard output stream by default")

#we can rederect the output
#  python3  d.py  > text.txt
#  cat text.txt      $Standard output stream by default


import sys

print("Standard error", file=sys.stderr)   #2  second output

# python3 errout.py 2> o.txt   #  the error outputo goes to o.txt  (2)

sys.stderr.write("error message\n")  #no newline 


import logging
logging.warning("Warning message")

'''
cat o.txt
Standard error
error message
WARNING:root:Warning message
'''
