#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko
import socket


def ssh_exec_command(ip, port, username, password, cmd):
    try:
        paramiko.util.log_to_file('./logs/ssh.log')
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip, port=port, username=username, password=password, timeout=6, allow_agent=False,
                    look_for_keys=False)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        return stdout.read()
    except paramiko.ssh_exception.AuthenticationException:
        return "用户名与密码验证失败！"
    except socket.timeout:
        return "连接失败！"
    finally:
        ssh.close()
