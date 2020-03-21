from aip import AipImageClassify
from hyperlpr import *
import cv2
#更改视频路径Line9和图片储存路径Line13 [最后加"\\"] 和Line35和Line51  适当更改帧数Line17
class car:
    def __init__(self):
        print("Begin Hello world")
    def videoCut():
        videopath="D:\\Desktop\\cai_Maters.mp4"  #视频路径
        videoCapture = cv2.VideoCapture(videopath)
        # 通过摄像头的方式
        # videoCapture=cv2.VideoCapture(1)
        savePath = "D:\\savePath\\"  # 图片存储位置
        # 遍历帧数保存
        success, frame = videoCapture.read()
        i = 0
        timeF = 24
        j = 0
        while success:
            i = i + 1
            if (i % timeF == 0):
                j = j + 1
                address = savePath + str(j) + '.jpg'
                cv2.imwrite(address, frame)
            success, frame = videoCapture.read()
        print("视频关键帧截取完毕")

    def get_carInfo():
        # 百度智云API账号
        APP_ID = '18695294'
        API_KEY = 'zlKcuDiNEvci9QGuQZG1Lrjc'
        SECRET_KEY = 'rFQQBxWA1pFiiEKOL2qMef3vKxdOwTxx'

        img_prefix = ['png', 'jpg', 'jpeg']
        savePath="D:\\savePath"     #图片存储位置
        carClient=AipImageClassify(APP_ID,API_KEY,SECRET_KEY)

        #遍历指定文件夹下的指定图片文件
        carIamges = os.listdir(savePath)
        for carIamge in carIamges:
            index=carIamge.find('.')
            prefix=carIamge[index+1:]
            if prefix in img_prefix:
                filePath=savePath+"\\"+carIamge
                #读取图片数据
                with open(filePath,'rb') as fp:
                    carSize=carClient.carDetect(fp.read(),options={"top_numm": 1})["result"][0]["name"] #车型数据
                    carLicense =HyperLPR_plate_recognition(cv2.imread(filePath))#车牌数据
                    print(carSize,"     ",carLicense)
    def clearAll():
        savePath = "D:\\savePath"  # 图片存储位置
        for i in os.listdir(savePath):
            path_file = os.path.join(savePath, i)
            if os.path.isfile(path_file):
                os.remove(path_file)
            else:
                for f in os.listdir(path_file):
                    path_file2 = os.path.join(path_file, f)
                    if os.path.isfile(path_file2):
                        os.remove(path_file2)
        print("文件夹已清空")
if __name__=="__main__":
    car.videoCut()
    car.get_carInfo()
    car.clearAll()

