import cv2

print(cv2.__version__)
vidcap = cv2.VideoCapture('test.mp4')
success,image = vidcap.read()
count = 0
success = True
fps = int(vidcap.get(cv2.CAP_PROP_FPS))

while vidcap.isOpened():
    ret, frame = vidcap.read()

    if ret:
        new_width = 210
        new_height = 120
        dsize = (new_width, new_height)
        output = cv2.resize(frame, dsize, interpolation = cv2.INTER_AREA)
        cv2.imwrite('frame{:d}.jpg'.format(int(count/fps)), output)
        count += fps # i.e. at 30 fps, this advances one second
        vidcap.set(1, count)
    else:
        vidcap.release()
        break