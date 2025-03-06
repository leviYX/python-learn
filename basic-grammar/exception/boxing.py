import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def printBox4(x,y,boxName):
    logging.info('x is %s,y is %s, boxName is %s',x,y,boxName)
    if x < 0:
        raise ValueError("第四象限，x不能小于零")
    if y > 0:
        raise ValueError("第四象限，y不能大于零")
    if boxName is None:
        raise ValueError("第四象限，必须传入boxName参数")
    print("第四象限：",x,y)

#assert 1 == 1,"断言失败"

for x,y,name in [(1,-2,"第四象限1"),(3,4,"第四象限2"),(5,6,"第四象限3"),(7,8,"第四象限4")]:
    try:
        printBox4(x,y,name)
    except ValueError as e:
        print(e)

