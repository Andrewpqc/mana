# coding: utf-8

"""
    mana
    ~~~~

        my flask toolkit & help me generate my flask app!

        copyright: (c) 2015 by neo1218.
        :license: MIT, see LICENSE for more details.

        mana init project_name                 # init your project
        mana install --venv/--no-venv          # install your flask extensions
        mana sql database_name                 # makesure the database_name is same with your config
        mana project_name app db               # create manage.py
        mana update project_name               # update the project
"""

import click
import os
from templates import _config_base, _config_with_sql, _file_init, \
                     _file_init_with_sql, _sql_models_file, _manage_py


def make_tuple(name, count):
    """
	格式化元组工厂函数
	:param name:
	:param count:
	"""
    format_tuple = []
    for i in range(count):
        format_tuple.append(name)
    return tuple(format_tuple)


def fill_file(project_name, filename, pre_code):
    """
	文件中填入预填代码:
	预填代码从templates模版中获取
	:param project_name
	:param filename
	:param pre_code
	"""
	# :path 当前路径
	# open the file path::project_name::filename and is "w+"
	# write the pre_code into file
    path = os.popen('pwd').readlines()[0][0:-1]
    fo = open("%s/%s/%s" % (path, project_name, filename), "w+")
    fo.write(pre_code)
    fo.close

"""use click:)"""

@click.group()
def mana():
    """my flask toolkit
       help me generate my flask app"""
    pass


@mana.command()
@click.argument('project_name', default="my_project")
def init(project_name):
    """
	init your project
	:param project_name 你项目的名字
	:default 默认是 "my_project"
	"""
	# 在python中执行shell命令
    os.system("mkdir %s" % project_name)
    os.system("touch %s/README.md %s/config.py %s/requirement.txt" \
            % make_tuple(project_name, 3))
    os.system("mkdir %s/app/ %s/test/" \
            % make_tuple(project_name, 2))
    os.system("touch %s/app/__init__.py %s/app/models.py %s/app/views.py %s/app/forms.py" % \
            make_tuple(project_name, 4))
    os.system("mkdir %s/app/templates/ %s/app/static/" % \
            make_tuple(project_name, 2))
    os.system("cd ..")

    # happy coding
	# 调用 fill_file 函数
	# 初始化的时候调用模版预填代码
    fill_file(project_name, 'config.py', _config_base)
    fill_file(project_name, 'app/__init__.py', _file_init)

    click.echo("init ... done!")


@mana.command()
@click.option('--venv/--no-venv', default=False, help="")
def install(venv):
    """
	install your flask extensions
	安装flask扩展
	:venv 虚拟环境 默认是 False
	:--venv 创建虚拟环境，并在虚拟环境下安装扩展
	:--no-venv 在全局环境中安装扩展
	需要在 'requirement' 文件中预填扩展
	:example
		Flask==0.10
	"""
    if venv:
        click.echo("creating venv")
        os.system("virtualenv venv")
        os.system(". venv/bin/activate")

        click.echo("install extensions")
        os.system("pip install -r requirement.txt")
        click.echo("install ... done!")
    else:
        click.echo("install extensions")
		# use sudo
        os.system("sudo pip install -r requirement.txt")
        click.echo("install ... done!")


@mana.command()
@click.argument('project_name')
def sql(project_name):
    """
	integrate flask-sqlalchemy
	自动集成flask-sqlalchemy扩展
	:param project_name 项目的名称
	"""
    fill_file(project_name, 'config.py', _config_with_sql)
    fill_file(project_name, 'app/__init__.py', _file_init_with_sql)
    fill_file(project_name, 'app/models.py', _sql_models_file)
    click.echo("integrate flask-sqlalchemy ... done!")


@mana.command()
@click.argument('project_name')
def manage(project_name):
    """
	create manage.py help me:)
	创建 manage.py 文件
	调用 fill_file 函数
	"""
    fill_file(project_name, 'manage.py', _manage_py)
    click.echo("create ... done!")
