
import sys, os, datetime, hashlib
import httplib, urllib, json

class Utils(object):
    def reflectInfo(self,object, spacing=10, collapse=1):
        """Print methods and doc strings.
        
        Takes module, class, list, dictionary, or string."""
        methodList = [e for e in dir(object) if callable(getattr(object, e))]
        processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
        print "\n".join(["%s %s" %
                         (method.ljust(spacing),
                          processFunc(str(getattr(object, method).__doc__)))
                         for method in methodList])
        
    def interrogate(self,item):
        """Print useful information about item."""
        if hasattr(item, '__name__'):
            print "NAME:    ", item.__name__
        if hasattr(item, '__class__'):
            print "CLASS:   ", item.__class__.__name__
        print "ID:      ", id(item)
        print "TYPE:    ", type(item)
        print "VALUE:   ", repr(item)
        print "CALLABLE:",
        if callable(item):
            print "Yes"
        else:
            print "No"
            
        if hasattr(item, '__doc__'):
            doc = getattr(item, '__doc__')
            
            if hasattr(doc,'strip'):
                doc = doc.strip()   # Remove leading/trailing whitespace.
                firstline = doc.split('\n')[0]
                print "DOC:     ", firstline

        
    def ConvertDictToString(self,d):
        #from pprint import pprint 
        #pprint(d)
        return ''.join(["'%s':%s\r\n" % item for item in d.iteritems()])

    prettyPrint = lambda self, dom: '\n'.join([line for line in dom.toprettyxml(indent=' '*2).split('\n') if line.strip()])

    def Ping(self,n):
        return n /3
     
    def md5encode(self,plain):
        m = hashlib.md5()
        m.update(plain)
        return m.hexdigest()
    
    def getToken(self):
        import uuid
        g = uuid.uuid1()
        return Utils().pack(str(g))
    
    
    def getRandom(self):
        import random
        return random.random()   
        
    def timestampJSON(self):
        return datetime.datetime.now().ctime()
        #return datetime.datetime.now().isoformat()
        
    def Timestamp(self):
        return datetime.datetime.now().ctime()
    
    def fileTimestamp(self):
        return datetime.datetime.now().strftime("%Y%m%d.%H%M%S")
    
    
        
    def printList(self,list):
        for item in list:
            print item
    
    def getListFromFile(self, path):
        """get list from text file"""
        readData = None
        logger.debug("loading list from " + path)
        
        ret = []
        try:        
            with open(path,'r') as f:
                for line in f.readlines():
                    ret.append( unicode(line.strip() ) )
        except:
            logger.error("error opening file at  >> " + path)
            raise
             
        return ret
    
    
    def pack(self,what):
        import urllib
        s = what.encode('base64','strict')
        return urllib.quote(s)
    
    def unpack(self,what):
        import urllib
        s = urllib.unquote(what)
        return s.decode('base64','strict')
    
    def tail(self,filepath, nol=10):
        f = open(filepath, 'rU')    # U is to open it with Universal newline support 
        allLines = f.readlines()
        f.close()
        ret = "\r\n".join(allLines[-nol:])
        return ret
    
    def removeFile(self,filePath):
        os.remove(filePath)
        
    def saveFile(self,path,filename,what):
        filepath = "{0}/{1}".format( path,filename)
        FILE = open(filepath,"w")
        FILE.write(what)
        FILE.close()
 