import json
from datetime import datetime

def initialisatie():
    global check_list
    global log_list
    check_list = bes_lezen("ServersChecks.json")
    log_list = bes_lezen("ServersLogs.json")

'''Bestand lezen'''
def bes_lezen(naam):
    try:
        with open(naam,"r") as bes:
            data = json.load(bes)
        return data
    except FileNotFoundError:
        with open(naam,"w") as bes:
            json.dump([],bes)
        return []

'''Bestand schrijven'''
def bes_schrijven(naam, data):
    with open(naam,"w") as bes:
        json.dump(data,bes)

'''data list schrijven naar html bestand'''
def data_naar_html():
    with open("index.html","r") as input_bes:
        index_string = input_bes.read()
    pos = index_string.find("output")+8
    start = index_string[0:pos]
    end = index_string[pos:-1]
    login = ""
    copy_list = log_list[:]
    copy_list.sort(key = lambda date: datetime.strptime(date[0], '%Y-%m-%d %X'), reverse=True)
    for event in copy_list:
        if event[5][0] == None:
            succes = 0
            rapport = f"offline"
        else:
            succes = int(100 - float(event[5][0]))
            rapport = f"Min: {event[5][1]}ms , Avg: {event[5][2]}ms ,  Max: {event[5][3]}ms"
        if succes == 100:
            boodschap = f"<strong class='ok'>{event[3]}</strong>"
        else:
            boodschap = f"<strong class='not_ok'>{event[3]}</strong>"
        event_boodschap = f"{boodschap} <span>{event[4]}</span> {succes}% OK | {rapport} <time datetime='{event[1]} {event[2]}'>{event[1]} {event[2]}</time>"

        login += "<li>" + event_boodschap + "</li>"
    with open("login.html","w") as output_bes:
        output_bes.write(start + login + end)