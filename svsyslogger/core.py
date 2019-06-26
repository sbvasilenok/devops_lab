#!/usr/bin/env python
from datetime import datetime
import time
import os
import configparser
import psutil
import json


class JsonLogger:

    snapnumber = 0

    def __init__(self, filename):
        self.filename = filename

    def logtofile(self):

        filename = self.filename
        JsonLogger.snapnumber += 1

        data = {
            'SNAPSHOT': JsonLogger.snapnumber,
            'TIME': datetime.now().strftime('%d-%m-%Y %H:%M:%S'),
            'CPU': str(psutil.cpu_percent(interval=1)),
            'MEMORY': str(psutil.virtual_memory()),
            'SWAP': str(psutil.swap_memory()),
            'IO': str(psutil.disk_io_counters(perdisk=False)),
            'NETWORK': str(psutil.net_io_counters(pernic=True))
        }

        with open(filename, 'a+', encoding='utf-8') as logfile:
            try:
                json.dump(data, logfile, ensure_ascii=False, indent=1)
            except NameError:
                print('write error')


class PlainLogger:

    snapnumber = 0

    def __init__(self, filename):
        self.filename = filename

    def logtofile(self):

        filename = self.filename
        PlainLogger.snapnumber += 1

        data = [
            'SNAPSHOT ',
            str(PlainLogger.snapnumber),
            datetime.now().strftime(': %d-%m-%Y %H:%M:%S :'),
            ' CPU: ', str(psutil.cpu_percent(interval=1)),
            ' MEMORY: ', str(psutil.virtual_memory()),
            ' SWAP: ', str(psutil.swap_memory()),
            ' IO: ', str(psutil.disk_io_counters(perdisk=False)),
            ' NETWORK: ', str(psutil.net_io_counters(pernic=True)), '\n'
        ]

        with open(filename, 'a+', encoding='utf-8') as logfile:
            try:
                logfile.writelines(data)
            except NameError:
                print('write error')


def main():

    cfgfilename = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.conf')

    if not os.path.isfile(cfgfilename):
        interval = 300
        logtype = 'plain'
        print('config.conf not exist, defaults loaded')
    else:
        try:
            config = configparser.ConfigParser()
            config.read(cfgfilename)
        except NameError:
            interval = 300
            logtype = 'plain'
            print('config.conf read error, defaults loaded')
        else:
            try:
                interval = int(config['common']['interval'])
            except KeyError:
                interval = 300
            try:
                logtype = config['common']['output']
            except KeyError:
                logtype = 'plain'
            try:
                logpath = config['common']['logpath']
            except KeyError:
                logpath = os.path.abspath(os.path.dirname(__file__))
            else:
                if not os.path.exists(logpath):
                    try:
                        os.makedirs(logpath)
                    except OSError:
                        logpath = os.path.abspath(os.path.dirname(__file__))
                print('path to config:', cfgfilename)

    if logtype == 'json':
        logfilename = os.path.join(logpath, 'log.json')
        logger = JsonLogger(logfilename)
    else:
        logfilename = os.path.join(logpath, 'log.txt')
        logger = PlainLogger(logfilename)

    print('path to logfile:', logfilename)

    while True:
        logger.logtofile()
        time.sleep(interval)


if __name__ == '__main__':
    main()
