import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import shutil


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            if filename not in ['desktop.ini']:
                #extracting the extension
                fname, file_extension = os.path.splitext(folder_to_track+"\\"+filename)
                file_extension = str(file_extension)
                src = folder_to_track + "\\" + filename
                try :
                    dest = extensions_folder[file_extension]+"\\"+filename
                    shutil.move(src, dest)
                except KeyError:
                    file_extension = 'noname'
                    dest = extensions_folder[file_extension]+"\\"+filename
                    shutil.move(src, dest)


extensions_folder = {
    #noname
    'noname' : "D:\\Saurabh\\Other\\Unknown",
    
    #Audio
    '.aif' : "D:\\Saurabh\\Media\\Audio",
    '.cda' : "D:\\Saurabh\\Media\\Audio",
    '.mp3' : "D:\\Saurabh\\Media\\Audio",
    '.mid' : "D:\\Saurabh\\Media\\Audio",
    '.midi' : "D:\\Saurabh\\Media\\Audio",
    '.mpa' : "D:\\Saurabh\\Media\\Audio",
    '.wav' : "D:\\Saurabh\\Media\\Audio",
    '.ogg' : "D:\\Saurabh\\Media\\Audio",
    '.wma' : "D:\\Saurabh\\Media\\Audio",
    '.wpl' : "D:\\Saurabh\\Media\\Audio",
    '.m3u' : "D:\\Saurabh\\Media\\Audio",

    #Text
    '.txt' : "D:\\Saurabh\\Text\\TextFiles",
    '.doc' : "D:\\Saurabh\\Text\\Word",
    '.docx' : "D:\\Saurabh\\Text\\Word",
    '.odt': "D:\\Saurabh\\Text\\TextFiles",
    '.pdf' : "D:\\Saurabh\\Text\\PDF",
    '.rtf' : "D:\\Saurabh\\Text\\TextFiles",
    '.tex': "D:\\Saurabh\\Text\\TextFiles",
    '.wks': "D:\\Saurabh\\Text\\TextFiles",
    '.wps': "D:\\Saurabh\\Text\\TextFiles",
    '.wpd' : "D:\\Saurabh\\Text\\TextFiles",

    #Video
    '.3g2' : "D:\\Saurabh\\Media\\Video",
    '.3gp' : "D:\\Saurabh\\Media\\Video",
    '.avi' : "D:\\Saurabh\\Media\\Video",
    '.flv' : "D:\\Saurabh\\Media\\Video",
    '.h264' : "D:\\Saurabh\\Media\\Video",
    '.m4v': "D:\\Saurabh\\Media\\Video",
    '.mkv': "D:\\Saurabh\\Media\\Video",
    '.mov': "D:\\Saurabh\\Media\\Video",
    '.mp4' : "D:\\Saurabh\\Media\\Video",
    '.mpg': "D:\\Saurabh\\Media\\Video",
    '.mpeg': "D:\\Saurabh\\Media\\Video",
    '.rm': "D:\\Saurabh\\Media\\Video",
    '.swf':"D:\\Saurabh\\Media\\Video",
    '.vob': "D:\\Saurabh\\Media\\Video",
    '.wmv': "D:\\Saurabh\\Media\\Video",

    #Images
    '.ai': "D:\\Saurabh\\Media\\Images",
    '.bmp': "D:\\Saurabh\\Media\\Images",
    '.gif': "D:\\Saurabh\\Media\\Images",
    '.ico': "D:\\Saurabh\\Media\\Images",
    '.jpg' : "D:\\Saurabh\\Media\\Images",
    '.jpeg': "D:\\Saurabh\\Media\\Images",
    '.png': "D:\\Saurabh\\Media\\Images",
    '.ps': "D:\\Saurabh\\Media\\Images",
    '.psd' : "D:\\Saurabh\\Media\\Images",
    '.svg' : "D:\\Saurabh\\Media\\Images",
    '.tif': "D:\\Saurabh\\Media\\Images",
    '.tiff': "D:\\Saurabh\\Media\\Images",
    '.CR2' : "D:\\Saurabh\\Media\\Images",

    #Internet
    '.asp' : "D:\\Saurabh\\Other\\Internet",
    '.aspx' :  "D:\\Saurabh\\Other\\Internet",
    '.cer':  "D:\\Saurabh\\Other\\Internet",
    '.cfm':  "D:\\Saurabh\\Other\\Internet",
    '.cgi':  "D:\\Saurabh\\Other\\Internet",
    '.pl' :  "D:\\Saurabh\\Other\\Internet",
    '.css' :  "D:\\Saurabh\\Other\\Internet",
    'htm' :  "D:\\Saurabh\\Other\\Internet",
    '.js' :  "D:\\Saurabh\\Other\\Internet",
    '.jsp' :  "D:\\Saurabh\\Other\\Internet",
    '.part' :  "D:\\Saurabh\\Other\\Internet",
    '.php' :  "D:\\Saurabh\\Other\\Internet", 
    '.rss' :  "D:\\Saurabh\\Other\\Internet",
    '.xhtml' :  "D:\\Saurabh\\Other\\Internet", 

    #Compressed
    '.7z' : "D:\\Saurabh\\Other\\Compressed",
    '.arj':  "D:\\Saurabh\\Other\\Compressed",
    '.deb' : "D:\\Saurabh\\Other\\Compressed",
    '.pkg' : "D:\\Saurabh\\Other\\Compressed",
    '.rar' : "D:\\Saurabh\\Other\\Compressed",
    '.rpm' : "D:\\Saurabh\\Other\\Compressed",
    '.tar.gz' : "D:\\Saurabh\\Other\\Compressed",
    '.gz': "D:\\Saurabh\\Other\\Compressed",
    '.z' : "D:\\Saurabh\\Other\\Compressed",
    '.zip' : "D:\\Saurabh\\Other\\Compressed",

    #Disc
    '.bin' : "D:\\Saurabh\\Other\\Disc",
    '.dmg' : "D:\\Saurabh\\Other\\Disc",
    '.iso' : "D:\\Saurabh\\Other\\Disc",
    '.toast' : "D:\\Saurabh\\Other\\Disc",
    '.vcd' : "D:\\Saurabh\\Other\\Disc",

    #Data
    '.csv': "D:\\Saurabh\\Programming\\Database", 
    '.dat': "D:\\Saurabh\\Programming\\Database",
    '.db': "D:\\Saurabh\\Programming\\Database",
    '.dbf': "D:\\Saurabh\\Programming\\Database",
    '.log' : "D:\\Saurabh\\Programming\\Database",
    '.mdb' : "D:\\Saurabh\\Programming\\Database",
    '.sav' : "D:\\Saurabh\\Programming\\Database",
    '.sql' : "D:\\Saurabh\\Programming\\Database",
    '.tar' : "D:\\Saurabh\\Programming\\Database",
    '.xml' : "D:\\Saurabh\\Programming\\Database",
    '.json' : "D:\\Saurabh\\Programming\\Database",

    #Executables
    '.apk': "D:\\Saurabh\\Other\\Executables",
    '.bat' : "D:\\Saurabh\\Other\\Executables",
    '.com' : "D:\\Saurabh\\Other\\Executables",
    '.exe': "D:\\Saurabh\\Other\\Executables",
    '.gadget': "D:\\Saurabh\\Other\\Executables",
    '.jar': "D:\\Saurabh\\Other\\Executables",
    '.wsf': "D:\\Saurabh\\Other\\Executables",

    #Presentations
    '.key' : "D:\\Saurabh\\Text\\Presentations",
    '.odp': "D:\\Saurabh\\Text\\Presentations",
    '.pps' : "D:\\Saurabh\\Text\\Presentations",
    '.ppt': "D:\\Saurabh\\Text\\Presentations",
    '.pptx': "D:\\Saurabh\\Text\\Presentations",

    #Programming
    '.c' : "D:\\Saurabh\\Programming\\C&C++",
    '.class' : "D:\\Saurabh\\Programming\\Java",
    '.dart' : "D:\\Saurabh\\Programming\\Dart",
    '.py' : "D:\\Saurabh\\Programming\\Python",
    '.sh': "D:\\Saurabh\\Programming\\Shell",
    '.swift' : "D:\\Saurabh\\Programming\\Swift",
    '.html': "D:\\Saurabh\\Programming\\C&C++",
    '.h' : "D:\\Saurabh\\Programming\\C&C++",

    #Spreadsheets
    '.ods': "D:\\Saurabh\\Text\\Excel",
    '.xlr' : "D:\\Saurabh\\Text\\Excel",
    '.xls': "D:\\Saurabh\\Text\\Excel",
    '.xlsx' : "D:\\Saurabh\\Text\\Excel",

    #System
    '.bak' : "D:\\Saurabh\\Other\\System",
    '.cab' : "D:\\Saurabh\\Other\\System",
    '.cfg': "D:\\Saurabh\\Other\\System",
    '.cpl': "D:\\Saurabh\\Other\\System",
    '.col': "D:\\Saurabh\\Other\\System",
    '.cur': "D:\\Saurabh\\Other\\System",
    '.dll':"D:\\Saurabh\\Other\\System",
    '.dmp':"D:\\Saurabh\\Other\\System",
    '.drv': "D:\\Saurabh\\Other\\System",
    '.icns': "D:\\Saurabh\\Other\\System",
    '.ico': "D:\\Saurabh\\Other\\System",
    '.ini': "D:\\Saurabh\\Other\\System",
    '.lnk': "D:\\Saurabh\\Other\\System",
    '.msi': "D:\\Saurabh\\Other\\System",
    '.sys': "D:\\Saurabh\\Other\\System",
    '.tmp': "D:\\Saurabh\\Other\\System",
}


folder_to_track = "C:\\Users\\a\\Downloads"
folder_destination_path = "D:\\Saurabh"

event_handler = MyHandler()
observer = Observer()

observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
    
except KeyboardInterrupt:
    observer.stop()
observer.join()
