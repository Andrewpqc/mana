mana: my flask toolkit : help me generate my flask app.
===
## flask in my heart
我觉得，flask是一个非常自由的框架，它只有默默服务的核心，没有条条框框的约束。<br/>

## flask & free
flask 是自由的，但这种自由更多的体现在选择上(虽然这有时会有点困难)。<br/>
但是如果我们选中了一个合适的扩展后，一般就会在自己的项目中一直使用它。<br/>

## toolkit
每个flask开发者都有自己的一套工具 <br/>

## generate
不用每次重复的创建文件目录，集成、初始化扩展。<br/>

## So: mana
mana = my:toolkit + generate <br/>

## 使用mana 😄
### init your project

    $ mana init project_name

你已经创建了你的目录结构(如图)<br/>
![目录结构]() <br/>
并且在相关文件中预填了代码<br/>
[config.py预填代码]() <br/>
[__init__.py预填代码]() <br/>

### install your flask extensions
在 requirement.txt 中写入你希望安装的扩展的名称

    mana install --venv

这将创建一个名称为venv的虚拟环境并在该虚拟环境中安装扩展<br/>
如果你希望在全局环境中安装扩展，你可以关闭 --venv 选项

    mana install --no-venv

那么你的扩展就会被安装到全局中<br/>


### work with sql
对于sql数据库的处理, flask-sqlalchemy 是我最常用的扩展，使用mana可以帮助我快速集成、初始化扩展

    mana ext flask-sqlalchemy

接下来，你只需要专心于models.py的数据库设计与编码了<br/>


## 进度
2015-0910: have an idea<br/>
2015-0911: mana init & mana install<br/>
