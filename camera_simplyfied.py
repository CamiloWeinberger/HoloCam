import cv2
from modifier import *
import matplotlib.pyplot as plt
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2560)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1440)
N = 700#int(np.min(cap.read()[1].shape[:2]))             # number of pixels
lmbd = 405*1e-9         # wavelength in meter
h = 6e-03               # sidelength of hologram in meter
z = 15e-03              # source-to-detector distance in meter
z0_start = 0.000535     # start source-to-sample distance in meter
z0_end = 0.000742       # end source-to-sample distance in meter
z0_step = 0.00001     # step of the source-to-sample distance in meter
z0 = z0_start
#image = torch.from_numpy(plt.imread('test.bmp')[:,:,1]).float().cuda()
pp = define_base(N)

while 1:
    #z0 += z0_step
    s0 = z0*h/z
    #print(z0)
    ret, frame = cap.read()
    crop = pp.shape[0]
    w, h,c = frame.shape
    frame = torch.from_numpy(frame[int((w-crop)/2):int((crop-w)/2),int((h-crop)/2):int((crop-h)/2),1]).float()
    imag,phase = modifier(frame,lmbd, N, s0, z0,pp)
    #imag,phase = modifier(image,lmbd, N, s0, z0)
    #cv2.imshow('rawdata', frame)
    #cv2.imshow('Amplitude PSF', imag.numpy())
    #cv2.imshow('Phasemap', phase.numpy())
    cv2.imshow('amp and phase', np.concatenate((imag.numpy()/255,phase.numpy()/250),axis = 1))
    if z0 >= z0_end:
        z0 = z0_start
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#cap.release()