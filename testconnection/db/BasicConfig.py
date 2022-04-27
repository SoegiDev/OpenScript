from ast import arg


class BasicConfig():
    name = None
    config = None
    Version = None
    VersionCode = None
    ApplicationName = None
    PowerBy = None
    CreatedBy  = None
    CreatedYear = None
    License = None
    Github = None
    ApiVersion = None
    ServerVersion = None
    ApiUrl = None
    EndPoint = None
    def __init__(self, **kwargs):
        pass
    def parsing(self,parse):
        kwargs = {"version":parse['version'],"versioncode":parse['versioncode'],"applicationname":parse['applicationname'],"powered_by":parse['powered_by'],"created_by":parse['created_by'],"created_year":parse['created_year'],"license":parse['license'],"github":parse['github'],"version_api":parse['version_api'],"version_server":parse['version_server'],"url_api":parse['url_api'],"endpoint":parse['endpoint']}
        self.Version = kwargs['version']
        self.VersionCode = kwargs['versioncode']
        self.ApplicationName = kwargs['applicationname']
        self.powerBy = kwargs['powered_by']
        self.CreatedBy = kwargs['created_by']
        self.CreatedYear = kwargs['created_year']
        self.License = kwargs['license']
        self.Github = kwargs['github']
        self.ApiVersion = kwargs['version_api']
        self.ServerVersion = kwargs['version_server']
        self.ApiUrl = kwargs['url_api']
        self.EndPoint = kwargs['endpoint'] 
   
    def result(self):
        return {
        "version": self.Version,
        "versioncode":self.VersionCode,
        "applicationname": self.ApplicationName,
        "powered_by": self.powerBy,
        "created_by": self.CreatedBy,
        "created_year":self.CreatedYear,
        "license":self.License,
        "github":self.Github,
        "version_api":self.ApiVersion,
        "version_server":self.ServerVersion,
        "url_api":self.ApiUrl,
        "endpoint":self.EndPoint
        }
    def getConfig(self):
        self.name = 'name'
        self.config='config'
        return "{},{}".format(self.name, self.config)
    def getApiVersion(self):
        return self.ApiVersion
        
        