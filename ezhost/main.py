# -*- coding: utf-8 -*-
#!/usr/bin/python
"""
This module contains `main` method plus related subroutines.
`main` is executed as the command line ``ezhost`` program and takes care of
parsing options and commands

The other callables defined in this module are internal only. Anything useful
to individuals leveraging Fabric as a library, should be kept elsewhere.
"""
import argparse
import configparser
from ezhost.ServerBase import ServerBase


def main():
    """
        Check args
    """

    configure_obj = None
    try:
        parser = argparse.ArgumentParser(description='自动化安装')
        parser.add_argument(
            '-s', '--server',
            help='服务器代替名',
        )

        # force to install packages without ask question
        parser.add_argument(
            '-f', '--force',
            dest='force',
            action='store_true',
            help='不询问是否安装',
        )
        parser.add_argument(
            '-nf', '--not-force',
            dest='force',
            action='store_false',
            help='询问是否安装',
        )
        parser.set_defaults(force=False)

        # login to remote mysql, default is false
        parser.add_argument(
            '-my', '--mysql',
            dest='login_mysql',
            action='store_true',
            help='登录到Mysql数据库',
        )
        parser.set_defaults(login_mysql=False)

        # login to server
        parser.add_argument(
            '-login', '--login',
            dest='login_server',
            action='store_true',
            help='登录到远程服务器',
        )
        parser.set_defaults(login_server=False)

        parser.add_argument(
            '-p', '--project',
            help='项目名称，默认是demo',
            default='demo'
        )

        parser.add_argument(
            '-gp', '--git-pull',
            help='Github项目的保存目录',
        )

        parser.add_argument(
            '-C', '--config',
            help='配置文件路径',
        )

        parser.add_argument(
            '-H', '--host',
            help='客户机地址',
        )

        parser.add_argument(
            '-U', '--user',
            help='客户机用户名',
        )

        parser.add_argument(
            '-P', '--passwd',
            help='客户机登录密码',
        )

        parser.add_argument(
            '-K', '--keyfile',
            help='客户机SSH KEY的路径',
        )

        args = parser.parse_args()
    except Exception as e:
        parser.print_help()

    # if config file and host both not provide, throw a error
    try:
        if args.config is None and args.host is None:
            raise ValueError('缺少配置文件-C(--config) 或 客户机地址-H(--host)')
    except Exception as e:
        print(e)
        return

    # check user and passwd
    try:
        if args.host is not None:
            if (args.user and (args.passwd or args.keyfile)) is None:
                raise ValueError('缺少登录必要的信息')
    except Exception as e:
        print(e)
        return

    # if exist config file, read configuration from file
    try:
        if args.config is not None:
            # init configuration parser
            configure = configparser.ConfigParser()
            configure.read(args.config)

            # check key exist
            if 'ezhost' in configure:
                configure_obj = configure['ezhost']
            else:
                raise KeyError('不能找到登录配置文件')
    except Exception as e:
        print(e)
        return

    # init server
    ServerBase(args, configure_obj)
