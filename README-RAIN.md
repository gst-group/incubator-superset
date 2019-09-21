## 开发笔记

### 在Mac上安装`mysqlclient`
- 安装`mysql-connector-c`
```shell script
brew install mysql-connector-c
```
- 修改配置`/usr/local/Cellar/mysql-connector-c/6.1.11/bin/mysql_config`
```shell script
在114行, 将
    libs="$libs -l "
改为
    libs="$libs -lmysqlclient -lssl -lcrypto"
```
- 在`virtualenv`下指定环境变量并安装
```shell script
export LDFLAGS="-L/usr/local/opt/openssl/lib"
export CPPFLAGS="-I/usr/local/opt/openssl/include"

pip install mysqlclient
```

### 前端开发模式
```shell script
cd superset/assets
npm ci

npm run dev-server
```

### 后端开发模式
```shell script
pip install -r requirements.txt
pip install -r requirements-dev.txt

pip install -e .
FLASK_ENV=development superset run -p 8088 --with-threads --reload --debugger
```

### 初始化Superset MateData DB
```shell script
# Create an admin user in your metadata database
superset fab create-admin

# Initialize the database
superset db upgrade 

# Create default roles and permissions
superset init
```

### 多表关联查询解决方案
优先在数据库中建立`view`，再按`table`添加进`superset`
```shell script
create view `test-view` as select a.*, b.* from a join b on ...
```

### 默认角色说明
```shell script
1、Admin
管理员有所有的权利，其中包括授予或撤销其他用户和改变其他人的切片和仪表板的权利。

2、 Alpha
alpha可以访问所有数据源，但不能授予或撤消其他用户的访问权限，并且他们也只能修改自己的数据。alpha用户可以添加和修改数据源。

3、 Gamma
Gamma访问有限。 他们只能使用他们通过另一个补充角色访问的数据源中的数据。 他们只能访问查看从他们有权访问的数据源制作的切片和仪表板。 目前，Gamma用户无法更改或添加数据源。 我们假设他们大多是内容消费者，虽然他们可以创建切片和仪表板。
还要注意，当Gamma用户查看仪表板和切片列表视图时，他们只会看到他们有权访问的对象。

4、sql_lab
sql_lab角色用于授予需要访问sql lab的用户，而管理员用户可以访问所有的数据库，默认情况下，Alpha和Gamma用户需要一个数据库的访问权限。

5、Public
允许登录用户访问一些Superset的一些功能。
在superset的config.py文件中public_role_like_gamma属性设置为true，您授予的公共角色权限设置为与Gamma的作用相同。如果要启用匿名用户查看仪表板，可以这样做。但是仍然需要对特定数据集进行显式授权，这意味着您需要编辑Public角色并将Public的数据源手动添加到角色
```