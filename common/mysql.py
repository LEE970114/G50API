import pymysql
from common.logger import logger
from testcase.config import MyConf
def delete_test_user():
    config=MyConf("conf_test.ini")
    db=pymysql.connect(host=config.get("mysql","host"),
                   user=config.get("mysql","user"),
                   password=config.get("mysql","password"),
                   database=config.get("mysql","database"),
                   charset=config.get("mysql","charset"))
    cur = db.cursor()
    try:
        cur.execute("delete from member where phone=17720798629")
        logger.info("删除已注册手机号")
    except:
        logger.debug("删除失败")
    cur.execute("select * from member")
    db.commit()
    db.close()
    data = cur.fetchmany(10)




