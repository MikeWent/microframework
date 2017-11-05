#!/usr/bin/env python3

import time
import threading
import json

class PereodicTask:
    """Repeat procedure/function in background (thread) with interval
    
    Args:
        task (obj): procedure/function to repeat
        interval (int): interval in seconds (default 1)
    """
    def __init__(self, task, interval=1):
        self.interval = interval
        self.task = task
        
        self.thread = threading.Thread(target=self._procedure, args=())
        self.thread.daemon = True
        self.thread.start()

    def _procedure(self):
        while True:
            self.task()
            time.sleep(self.interval)
    
    def stop(self):
        """Stop execution and delete thread"""
        del self
    

class JSONDB:
    """Load JSON file and use it as database (key: value)
    
    Args:
        filename (str): filename of DB, example: names.json
        rw (bool): defines if DB writable or read-only
    """
    def __init__(self, filename, rw=True):
        self.filename = filename
        self.rw = rw
        self.load()
    
    def load(self):
        """Parse JSON and load to memory"""
        with open(self.filename, 'r') as f:
            self.json_array = json.loads(f.read())

    def save(self):
        """Save modified DB to file"""
        if not self.rw:
            return False
        
        with open(self.filename, 'w') as f:
            json.dump(self.json_array, f, sort_keys=True, indent=4)
            return True

    def get(self, option):
        """Get value from loaded config"""
        return self.json_array[option]
    
    def set(self, option, new_value):
        """Change key value. Need commit() to save to disk"""
        self.json_array[option] = new_value
