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