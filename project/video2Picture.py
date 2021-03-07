import cv2

#file is video path, save_path is the JPG dir path
def video_2_pic(file, save_path):
    """
    逐帧取照片
    file:视频的位置
    save_path:保存路径
    """
    # 读取视频
    video = cv2.VideoCapture(file)
    # 获取视频帧率
    fps = video.get(cv2.CAP_PROP_FPS)
    # 获取画面大小
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    size = (width, height)
    frame_num = str(video.get(7))
    ret, frame = video.read()
    num = 1
    while True:
        ret, frame = video.read()
        if ret != True:
            break
        cv2.imwrite(save_path + str(num) + '.jpg', frame)
        num += 1
    video.release()
    return fps, size, frame_num

video_2_pic('./clip.mp4', './test/')
