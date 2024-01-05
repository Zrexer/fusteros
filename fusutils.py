import os 
import sys 

class Symbols(object):
    
    def under() -> str:
        return "└"
    
    def base() -> str:
        return "├"
    
    def connector() -> str:
        return "|"
    
    def upper() -> str:
        return "┌"
    
class PathWorker(object):
    
    def DirectoryRunner() -> str:
        return os.getcwd()
    
    def argv() -> list:
        return sys.argv
    
class String(object):
    
    def __init__(self, string):
        self.string = str(string) if not type(string) is str else string 
        
    def splitter(self) -> list:
        return self.string.split()
    
    def specialSplitter(self, special):
        return self.string.split(special)
    
    def startsWith(self, starter) -> bool:
        return self.string.startswith(starter)
    
    def endsWith(self, ender) -> bool:
        return self.string.endswith(ender)
    
    def last(self) -> str:
        return self.string.split()[-1]
    
    def indexString(self, number) -> str:
        return self.string[number]
    
    def indexOf(self, indexer) -> int:
        return self.string.split().index(indexer)

    def responeString(self, targetToRespone) -> bool:
        if self.string.startswith(targetToRespone):
            return self.string.replace(targetToRespone, "")
        else:
            return False
        
    def replacer(self, base, toChange):
        return self.string.replace(base, toChange)
    
    def changeType(self):
        return str(self.string)
    
class Dictionary(object):
    def __init__(self, __dict):
        self.dict = __dict
        
    def getElement(self, element):
        return self.dict[element]
    
    def setElement(self, element, data):
        self.dict[element] = data
        return self.dict
    
    def allElements(self):
        return self.dict.keys()

    def allDatas(self):
        return self.dict.values()
    
    def clear(self, element):
        del self.dict[element]
        return self.dict
        
    def changeType(self):
        return dict(self.dict)
    
class List(object):
    def __init__(self, __list):
        self.list = __list
        
    def add(self, data):
        self.list.append(data)
        return self.list
    
    def clear(self):
        self.list.clear()
        return self.list
    
    def indexOf(self, indexor) -> int:
        return self.list.index(indexor)
    
    def pop(self, popper):
        return self.list.pop(popper)
    
    def changeType(self):
        return list(self.list)

