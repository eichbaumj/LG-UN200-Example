import xact
import re
import struct
import datetime

__contact__ = "Mickey Mouse"
__version__ = "1"
__description__ = "Parse messages from inbox.dat files"

def main(images):
    for image in images:
        for file in image.files:
            matchname = re.match(r'inbox(.*)', file.name)
            if matchname:
                if matchname.group() == 'inbox.dat':
                    pass
                else:
                    messagelength=struct.unpack('>B', file.read(205,1))[0]
                    message=file.read(206,messagelength).decode('UTF-8')
                    time = struct.unpack('<L',file.read(12,4))[0]
                    phone = file.read(515,10).decode('UTF-8')
                    time=datetime.datetime.utcfromtimestamp(time+315964800)
                    print("Message:",message)
                    print("From:",phone)
                    print("Date/time:",time)
                    text = image.add_sms()
                    text.message = message
                    text.nr_from = phone
                    text.datetime = time
                
        
