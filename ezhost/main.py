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
        nargs=2
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

    # if config file and host both not provide, throw a error
    if args.config is None and args.host is None:
        raise ValueError('缺少配置文件-C(--config)或客户机地址-H(--host)')

    # check user and passwd
    if args.host is not None:
        if (args.user and (args.passwd or args.keyfile)) is None:
            raise ValueError('缺少登录必要的信息')

    # if exist config file, read configuration from file
    if args.config is not None:
        # init configuration parser
        configure = configparser.ConfigParser()
        configure.read(args.config[0])
        config_sections = configure.sections()

        # check key exist
        if args.config[1] not in config_sections:
            raise KeyError('未找到与{0}对应的登录配置文件，存在的配置文件为{1}'
                           .format(args.config[1], config_sections))

        configure_obj = configure[args.config[1]]
    # init server
    ServerBase(args, configure_obj)
