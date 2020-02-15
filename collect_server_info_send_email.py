#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime

import yagmail
import psutil


user = 'xxxxx@163.com'
password = 'xxxx'
GIGA_BYTE_FORMAT = "{:.2f}G"


class Recipients(object):
    # def __init__(self, name, email):
    #     self.__dict__.update({k: v for k, v in locals().items() if k != 'self'})

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_first_name(self):
        return self.name.split()[0]

    def get_email_address(self):
        return self.email


def get_cpu_info():
    # cpu related
    cpu_count = psutil.cpu_count()
    cpu_percent = psutil.cpu_percent(interval=2)
    return locals()


def get_memory_info():
    # mem related
    """
    In [2]: psutil.virtual_memory()
    Out[2]: svmem(total=2107867136, available=1665032192, percent=21.0, used=227254272, free=598233088, active=782516224, inactive=541843456, buffers=60231680, cached=1222148096, shared=42590208)
    """
    virtual_mem = psutil.virtual_memory()
    mem_total = GIGA_BYTE_FORMAT.format(virtual_mem.total / 1024 / 1024 / 1024.0)
    mem_percent = virtual_mem.percent
    mem_free = GIGA_BYTE_FORMAT.format((virtual_mem.free ) / 1024 / 1024 / 1024.0)
    return dict(mem_total=mem_total, mem_percent=mem_percent,
            mem_free=mem_free)


def get_disk_info():
    # disk related
    """
    In [69]: psutil.disk_usage('/')
    Out[69]: sdiskusage(total=21100904448, used=2773405696, free=17430515712, percent=13.7)
    """
    disk_usage = psutil.disk_usage('/')
    disk_total = GIGA_BYTE_FORMAT.format(disk_usage.total / 1024 / 1024 / 1024.0)
    disk_percent = disk_usage.percent
    disk_free = GIGA_BYTE_FORMAT.format(disk_usage.free / 1024 / 1024 / 1024.0)
    return dict(disk_total=disk_total, disk_percent=disk_percent,
            disk_free=disk_free)


def get_boot_info():
    # boot related
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    boot_time = boot_time.strftime('%D %T')
    return locals()


def get_all_monitor_info():
    data = {}
    data.update(get_boot_info())
    data.update(get_cpu_info())
    data.update(get_memory_info())
    data.update(get_disk_info())
    return data


def generate_email_content(*args, **kwargs):

    body = """
Dear {name}:

    下面是{now}收集到的系统信息：

开机时间：{boot_time}

cpu个数: {cpu_count}
cpu使用率：{cpu_percent}

内存总量：{mem_total}
内存使用率：{mem_percent}
可用内存：{mem_free}

系统盘总量：{disk_total}
系统盘使用率：{disk_percent}
可用系统盘空间：{disk_free}

    """.format(**kwargs)
    return body


def main():
    recipients = [Recipients('xiao ming', 'xxxx@163.com'),
     Recipients('xiao hong', 'xxxx@qq.com')]

    data = get_all_monitor_info()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with yagmail.SMTP(user=user,
                      password=password,
                      host='smtp.163.com',
                      port='25') as yag:
        for rec in recipients:
            body = generate_email_content(name=rec.get_first_name(), now=now, **data)
            yag.send(rec.get_email_address(), "I now can send an attachment", body)


if __name__ == '__main__':
    main()
