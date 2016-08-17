# -*- coding: utf-8 -*-
import hyper
import base64
from multiprocessing import Process
import time

"""
구간으로 호출
"""
def loop_call_abort(domain,deploymentid,userid,passwd,start,end):
    for i in range(start, end):
        call_abort(domain,deploymentid,userid,passwd,i)
"""
단독 호출
"""
def call_abort(domain,deploymentid,userid,passwd,instanceid):
    c = hyper.HTTPConnection(domain)
    i_str = str(instanceid)
    url = '/business-central/rest/runtime/'+deploymentid+'/process/instance/'+i_str+'/abort'
    #print url
    c.request('POST',url,headers={'Authorization' : 'Basic %s' % base64.b64encode(userid+':'+passwd)})
    #resp = c.get_response()
    #print resp.read()
    #resp.close()
"""
멀티 프로세스를 띄우는 것
"""
def multi_process_call_abort(domain,deploymentid,userid,passwd,process_num,start,end):
    num = (start - end)
    num2 = num / process_num
    num3 = num % process_num
    start_time = time.time()
    for i in range(0, process_num):
        if(i==(process_num -1)):
            p = Process(target=loop_call_abort, args=(domain,deploymentid,userid,passwd,start+(num2 * i), start + (num2 * (i+1))+num3))
            p.start()
            p.join()
        else:
            p = Process(target=loop_call_abort, args=(domain,deploymentid,userid,passwd,start+(num2 * i), start + (num2 * (i+1))))
            p.start()
            p.join()
    end_time = time.time()
    print 'during time '+(end_time - start_time)+' sec'

if __name__ == '__main__':
    domain = raw_input("domain을 입력하세요 : ")
    deploymentid = raw_input("deploymentid를 입력하세요 : ")
    userid = raw_input("userid를 입력하세요 : ")
    passwd = raw_input("passwd를 입력하세요 : ")
    mode = input("mode를 입력하세요 :")
    if(mode == 1):
        instanceid = input("instanceid를 입력하세요 :")
        call_abort(domain, deploymentid, userid, passwd, instanceid)
    else:
        process_num = input("process 갯수를 입력하세요 :")
        start = input("시작 instanceid를 입력하세요 :")
        end = input("끝 instanceid를 입력하세요 :")
        multi_process_call_abort(domain, deploymentid, userid, passwd, process_num, start, end)
