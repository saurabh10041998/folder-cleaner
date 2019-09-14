import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Watcher:
    directory_to_watch = "C:\Users\a\Downloads"
    def __init__(self):
        self.observer = Observer()
    
    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.directory_to_watch, recursive=True)

        self.observer.start()

        try:
            while True:
                time.sleep(10)
        except:
            self.observer.stop()
            print "Error"
        
        self.observer.join()
        