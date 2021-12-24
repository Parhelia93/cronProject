from .models import PlcMessage
import snap7


def my_cron_job():
    IP = '10.145.112.47'
    RACK = 0
    SLOT = 2
    DB_NUM = 300
    START_ADDR = 0
    SIZE = 46

    plc = snap7.client.Client()
    plc.connect(IP, RACK, SLOT)

    data = plc.db_read(DB_NUM, START_ADDR, SIZE)
    newDataReady = snap7.util.get_bool(data, 0, 0)
    if newDataReady:
        numDriver = snap7.util.get_int(data, 4)
        controlVal = snap7.util.get_real(data, 6)
        comment = snap7.util.get_string(data, 18, 25)
        print(numDriver, controlVal, comment, newDataReady)
        PlcMessage.objects.create(numDriver=numDriver, controlValue=controlVal, comentStr=comment)
        snap7.util.set_bool(data, 0, 0, False)
        snap7.util.set_bool(data, 0, 1, True)
        snap7.util.set_int(data, 4, 0)
        snap7.util.set_real(data, 6, 0.0)
        plc.db_write(DB_NUM, START_ADDR, data)




