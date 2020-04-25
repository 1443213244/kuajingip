from dateutil.relativedelta import relativedelta
import cymysql
import json
import datetime
def get_dbconfig():
    with open('./usermysql.json', 'r') as f:
        config = f.read()
        dbconfig = json.loads(config)
        return dbconfig
def Set_date(month):
    enddate = datetime.datetime.now()+relativedelta(months=month)
    end_date = enddate.strftime("%Y-%m-%d %H:%M:%S")
    return end_date

def active():
    config =  get_dbconfig()
    conn = cymysql.connect(host=config['host'], user=config['user'], passwd=config['password'], db=config['db'])
    cur = conn.cursor()
    cur.execute('select d, active, pid from user')
    for r in cur.fetchall():
        if r[1] == 0 and r[0] >= 100000000:
                cur.execute('select billingcycle from tblhosting where id='+r[2])
                for t in cur.fetchall():
                    if t[0] == 'Monthly':
                       end_date = Set_date(1)
                       reg_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                       cur.execute('update user SET reg_date=\''+reg_date+'\', end_date=\''+end_date+'\', active=1 where pid='+r[2])
                       conn.commit()
                    elif t[0] == 'Quarterly':
                       end_date = Set_date(3)
                       reg_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                       cur.execute('update user SET reg_date=\''+reg_date+'\', end_date=\''+end_date+'\', active=1 where pid='+r[2])
                       conn.commit()
                    elif t[0] == 'Semi-Annually':
                        end_date = Set_date(6)
                        reg_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        cur.execute('update user SET reg_date=\''+reg_date+'\', end_date=\''+end_date+'\', active=1 where pid='+r[2])
                        conn.commit()
                    elif t[0] == 'Annually':
                        end_date = Set_date(12)
                        reg_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        cur.execute('update user SET reg_date=\''+reg_date+'\', end_date=\''+end_date+'\', active=1 where pid='+r[2])
                        conn.commit()
                    elif t[0] == 'Biennially':
                        end_date = Set_date(24)
                        reg_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        cur.execute('update user SET reg_date=\''+reg_date+'\', end_date=\''+end_date+'\', active=1 where pid='+r[2])
                        conn.commit()
                    elif t[0] == 'Triennially':
                        end_date = Set_date(36)
                        reg_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        cur.execute('update user SET reg_date=\''+reg_date+'\', end_date=\''+end_date+'\', active=1 where pid='+r[2])
                        conn.commit()
                    else:
                        print('one time')


active()
