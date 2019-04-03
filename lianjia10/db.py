import pymysql

class Lianjia10Info(object):
    def __init__(self,tableName):
        self.tableName = tableName
    # mysql数据库链接设置
    def add_lianjia10(self,title,detail_link,prize,time,location,content):
        db = pymysql.Connect(
            host = "localhost",
            port = 3306,
            user = "root",
            passwd = "root",
            db = "spider",
            charset = "utf8"

        )
        cursor = db.cursor()
        # 插入内容的sql语句
        sql = "insert into %s(title,detail_link,prize,time,location,content) value('%s','%s','%s','%s','%s','%s')"%(self.tableName,title,detail_link,prize,time,location,content)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()

    def get_count(self):
        db = pymysql.Connect(
            host = "localhost",
            port = 3306,
            user = "root",
            passwd = "root",
            db = "spider",
            charset = "utf8"

        )
        cursor = db.cursor()
        sql = "select count(1) from %s"%(self.tableName)
        cursor.execute(sql)
        total_count = cursor.fetchone()
        cursor.close()
        db.close()
        return total_count

    def outinfo(self,keyword,city,begin,total):
        result = {}
        config = {
            'host':"localhost",
            'port':3306,
            'user':"root",
            'passwd':"root",
            'db':'spider',
            'charset':'utf8',
            'cursorclass':pymysql.cursors.DictCursor
        }
        db = pymysql.Connect(**config)
        cursor = db.cursor()
        # 用于查询输出内容的sql语句
        sql = "select * from %s where (title like '%%%s%%' or content like '%%%s%%') and location like '%%%s%%' limit %s,%s"%(self.tableName,keyword,keyword,city,begin,total)
        print(sql)
        items = []
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            # 遍历返回的结果 并将所有内容一个个压入items字典中
            for row in result:
                item = {}
                item["title"] = row["title"]
                item["detail_link"] = row["detail_link"]
                item["prize"] = row["prize"]
                item["time"] = row["time"]
                item["location"] = row["location"]
                item["content"] = row["content"]
                items.append(item)

        except:
            pass
        finally:
            cursor.close()
            db.close()
        return items
    

    def create_table(self,tableName):
        db = pymysql.Connect(
            host = "localhost",
            port = 3306,
            user = "root",
            passwd = "root",
            db = "spider",
            charset = "utf8"

        )
        cursor = db.cursor()
        # mysql数据库中判断是否已经创建了表 若没有 则在此创建
        sql = """
        CREATE TABLE IF NOT EXISTS `""" +self.tableName+ """`  (
        `Id` int(11) NOT NULL AUTO_INCREMENT,
        `title` varchar(255) DEFAULT NULL,
        `detail_link` varchar(255) DEFAULT NULL,
        `prize` varchar(255) DEFAULT NULL,
        `time` varchar(255) DEFAULT NULL,
        `location` varchar(255) DEFAULT NULL,
        `content` text,
        PRIMARY KEY (`Id`)
        ) ENGINE=MyISAM DEFAULT CHARSET=utf8;
        """
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
                



lianjia10 = Lianjia10Info("lianjiainfo10")

lianjia10.create_table("lianjiainfo10")


