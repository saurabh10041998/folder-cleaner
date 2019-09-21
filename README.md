# Folder cleaner / self organiser

## objective
-  move the files from specific folder say x to appropriate folder to keep x clog free.

### todo
- [x] track the downloads folder for filechange
- [x] move the folder to the desired destination
- [ ] rename the duplicate folder properly
- [x] create the file subsystems for these folder
- [x] run the app the background
- [x] works for different types of files

#### Came up to reading part
- got nice blog documentation.. check out
<a href = "https://www.michaelcho.me/article/using-pythons-watchdog-to-monitor-changes-to-a-directory">
    Simple watchdog documentation code..
</a>

## usage
    To start the script running in background
-   <code> pythonw autocleaner.py </code>
    <p> To stop the running script </p>
-   <code> tskill pythonw <code>
    <p> To check the it running or not</p>
-   <code> taskset </code>