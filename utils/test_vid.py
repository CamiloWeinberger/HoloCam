import cv2
import numpy as np
result = cv2.VideoWriter(f'filename.mp4v', cv2.VideoWriter_fourcc(*'MP4V'), 25.0, (500, 500))
nn = 1
for i in range(1000):
    nn += 1
    print(str(nn))
    frame = np.uint8(np.random.rand(500,500,3)*255)
    result.write(frame)
    
result.release()