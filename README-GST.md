## 开发

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

### 前端开发
```shell script
cd superset/assets
npm ci

npm run dev-server
```

### 后端开发
```shell script
pip install -r requirements.txt
pip install -r requirements-dev.txt

pip install -e .
FLASK_ENV=development superset run -p 8088 --with-threads --reload --debugger
```

### 初始化元数据库
```shell script
# Create an admin user in your metadata database
superset fab create-admin

# Initialize the database
superset db upgrade 

# Create default roles and permissions
superset init
```

### 编译中文翻译模块
```shell script
pybabel compile -d superset/translations -l zh
```

### 多表关联查询解决方案
优先在数据库中建立`view`，再按`table`添加进`superset`
```shell script
create view `test-view` as select a.*, b.* from a join b on ...
```

### 部署&运行
```shell script
# 1.构建
./pypi_push.sh

# 2.传输
scp ./dist/apache-superset-1.0.0.tar.gz root@101.132.163.207:/root/superset

# 3.安装
pip3 install apache-superset-1.0.0.tar.gz

# 4.后台运行
SUPERSET_CONFIG_PATH=gst_config.py nohup superset run -h 0.0.0.0 -p 9000 --with-threads > superset.log &
```