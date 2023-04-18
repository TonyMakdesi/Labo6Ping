import platform
from datetime import datetime
import subprocess
import dataChecks

def add(type,para):
    dataChecks.check_list.append([type,para])
    dataChecks.bes_schrijven("ServersChecks.json",dataChecks.check_list)

def detelte(index):
    del dataChecks.check_list[int(index)]
    dataChecks.bes_schrijven("ServersChecks.json",dataChecks.check_list)

def frame():
    return dataChecks.check_list

def execute():
    for check in dataChecks.check_list:
        if check[0] == "ping":
            res = ping(check[1][0],check[1][1])
            time = datetime.now()
            time_clean = time.strftime("%Y-%m-%d %X")
            time_1 = time.strftime("%d-%m-%Y")
            time_2 = time.strftime("%X")
            check_res = [str(time_clean), str(time_1), str(time_2), "ping", check[1][0], res]
            dataChecks.log_list.append(check_res)
    dataChecks.bes_schrijven("ServersLogs.json",dataChecks.log_list)
    dataChecks.data_naar_html()

def ping(host_name,frams):
    try:
        para = "-n" if platform.system().lower()=='windows' else '-c'
        resp = subprocess.check_output(
            ['ping',para,str(frams),host_name],
            stderr=subprocess.STDOUT,
            universal_newlines=True
        )
    except subprocess.CalledProcessError:
        resp = [None]
        return resp
    else:
        if platform.system().lower()=='windows':
            packets = resp[resp.find("Lost = ")+10:resp.find("loss")-2]
            min = resp[resp.find("Minmum = ")+10:resp.find("ms, Maximum")]
            ave = resp[resp.find("Average = ")+10:resp.rfind("ms")]
            max = resp[resp.find("Maximum = ")+10:resp.find("ms,Average")]
            dev = '-'
            my_list = []
            my_list.append(packets)
            my_list.append(min)
            my_list.append(ave)
            my_list.append(max)
            my_list.append(dev)
            return my_list
        else:
            packets = resp[resp.find("received")+18:resp.find("packet loss")-2]
            round_trip = resp[resp.find("dev")+9:resp.rfind("ms")-1]
            return_string = packets + "/" +round_trip
            return return_string.split("/")