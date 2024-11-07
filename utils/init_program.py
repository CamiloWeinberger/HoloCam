from PyQt6.QtWidgets import QMainWindow
from PyQt6.uic import loadUi
from PyQt6.QtCore import QTimer
import torch
from utils.modifier import *
from utils.display_functions import *
import cv2
from PIL import Image


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
z0_start = 0.000625     # start source-to-sample distance in meter
z0_step =  0.000001 
z0 = z0_start
#pp = None

class windows(QMainWindow):
    def __init__(self):
        super(windows, self).__init__()
        self.pp = None 
        self.frame = None
        self.image = None
        self.Nframes = 0
        self.record = 0
        self.f1 = None
        self.cap = None
        self.distance_det = 15
        self.rang = None
        #self.f1_i = None
        loadUi('utils/Microscope.ui',self)
        if self.pp is None:
            self.pp = define_base(int(self.im_resol.text())).to(device)
            self.f1 = FT2Dc(self.pp).to(device)
            self.yline_amp.setMaximum(self.pp.shape[0])
            self.rang = range(self.pp.shape[0])
            
        self.connectCam.clicked.connect(self.InitCam)
        self.start.clicked.connect(self.Start_prev)
        self.stop.clicked.connect(self.Stop_prev)
        self.startRec.clicked.connect(self.Start_rec)
        self.stopRec.clicked.connect(self.Stop_rec)
        self.horizontalSlider.valueChanged.connect(self.Run)
        self.wavelength.textChanged.connect(self.Run)
        self.im_resol.textChanged.connect(self.Gen_pp)
        self.savePhoto.clicked.connect(self.saveImage)
        self.ZoomIn.clicked.connect(self.zoom)
        self.ZoomOut.clicked.connect(self.zoomout)
        self.ZoomOrig.clicked.connect(self.zoomorig)


        self.timer = QTimer()
        self.timer.timeout.connect(self.Run)
    
    def InitCam(self):
        try:
            self.wavelength.setEnabled(False)
            self.holo_size.setEnabled(False)
            self.distance.setEnabled(False)
            self.im_resol.setEnabled(False)
            self.start.setEnabled(False)
            self.stop.setEnabled(False)
            self.startRec.setEnabled(False)
            self.horizontalSlider.setEnabled(False)
            self.savePhoto.setEnabled(False)
            self.timer.stop()
            self.cap = cv2.VideoCapture(int(self.cam_number.text()), cv2.CAP_DSHOW)
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2560)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1440)
            
            self.wavelength.setEnabled(True)
            self.holo_size.setEnabled(True)
            self.distance.setEnabled(True)
            self.im_resol.setEnabled(True)
            self.start.setEnabled(True)
            self.stop.setEnabled(True)
            self.startRec.setEnabled(True)
            self.horizontalSlider.setEnabled(True)
            self.savePhoto.setEnabled(True)
            self.line_amp.setEnabled(True)
        except:
            a = 1
        
    def Start_prev(self):
        self.timer.start(10)
        
    
    def DrawLine(self):
        self.timer.start(10)
        
    def Stop_prev(self):
        self.timer.stop()
                
    def Start_rec(self):
        self.record = 1
        self.stopRec.setEnabled(True)    
        self.startRec.setEnabled(False)
        
        self.frame = cv2.VideoWriter('./Videos/' + self.name_video.text() + '.mp4', cv2.VideoWriter_fourcc(*'MP4V'), float(self.fps.text()), (self.pp.shape[0]*3, self.pp.shape[1]))
        #self.amplitude = cv2.VideoWriter(f'amp.mp4', cv2.VideoWriter_fourcc(*'MP4V'), 25.0, self.pp.shape)
        #self.phase = cv2.VideoWriter(f'phase.mp4', cv2.VideoWriter_fourcc(*'MP4V'), 25.0, self.pp.shape)
    def Stop_rec(self):
        self.record = 0
        self.frame.release()
        #self.amplitude.release()
        #self.phase.release()
        self.stopRec.setEnabled(False)    
        self.startRec.setEnabled(True)
    def Gen_pp(self):
        try: 
            pp_size = int(self.im_resol.text())     
        except:
            pp_size = 2
        self.pp = define_base(pp_size).to(device)
        self.f1 = FT2Dc(self.pp).to(device)
        self.yline_amp.setMaximum(pp_size)
        self.rang = range(self.pp.shape[0])
    
    def saveImage(self):
        im = Image.fromarray(self.image)
        im.save('./Captures/' + self.name_video.text() + '_frame_' +  str(self.Nframes) + '.bmp')
        
    def zoom(self):
        out = self.rang[20:-20]
        self.rang = out
    def zoomout(self):
        out = self.rang[20:-20]
        self.rang = out
    def zoomorig(self):
        self.rang = range(self.pp.shape[0])
        
    
    def Run(self):
        if self.cap.isOpened(): 
            ret, frame = self.cap.read()
            crop = self.pp.shape[0]
            w, h,c = frame.shape
            #image = torch.from_numpy(plt.imread('test.bmp')[:,:,1]).float()#.to(device)
            if crop<w:
                image = torch.from_numpy(frame[int((w-crop)/2):int((crop-w)/2),int((h-crop)/2):int((crop-h)/2),1]).float()
                
            else:
                image = torch.from_numpy(frame[:,:,1]).float()
                if image.shape[1] > image.shape[0]:
                    image = torch.from_numpy(frame[:,int((h-w)/2):int((w-h)/2),1]).float()
                
                
            # Check miss variables
            try:
                lmbd =  float(self.wavelength.text())*1e-9
            except:      
                lmbd = 0
            try:
                z0_start = float(self.distance.text())*1e-6
            except:       
                z0_start = 0
            try:
                h_size =  float(self.holo_size.text())    
            except:
                h_size = 0
                
            z0 = z0_start+float(self.horizontalSlider.value())*z0_step + 1e-12
            self.pos_value.setText(str((z0*1e6)))
            s0 = z0*h_size/(self.distance_det)
            try:
                imag_amp, phase = modifier(image.to(device), lmbd, float(self.im_resol.text()),s0,z0,self.pp,self.f1)
                imag_amp = imag_amp.cpu()
                phase = phase.cpu()
                set_single_channel_image_from_numpy(self.raw_image, image,      None)
                set_single_channel_image_from_numpy(self.im_amp,    imag_amp[self.rang][:,self.rang],   self.yline_amp.value())
                set_single_channel_image_from_numpy(self.im_ph,     phase[self.rang][:,self.rang],      None)    
                plot_on_label(self.im_amp_line, imag_amp[self.yline_amp.value(),self.rang])
                self.image = np.uint8(torch.stack((ff,)*3, axis=0).permute(1,2,0).numpy())

                if self.record == 1:
                    self.frame.write(self.image)
                    self.Nframes += 1
                else:
                    self.frame = None
                    self.Nframes = 0  
                self.time.setText(str(self.Nframes))

            except:
                a = 1
                