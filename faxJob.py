#!c:\python36\python.exe
import re

class faxJob(object):

    #public static
    faxJobs=[]
    
    #object vars
    files=[]#fullpath filenames
    uid=""
    status="NEW"
    staffcode=""
    
    destName=""
    destOrg=""
    destFax=""
    cliName=""
    casenum=0    
    staffEmail=""
    comment=""
    
    dwCasenum=""
    dwName=""
    dwProvider=""
    dwCategory=""
    dwDocumentType=""

    def __init__(self, uid):
        self.uid=uid
        self.staffcode=re.search('(.+?)-',uid,0).group(1)