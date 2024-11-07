import numpy as np
import torch
#lmbd = 405*1e-9         # wavelength in meter
#h = 6e-03               # sidelength of hologram in meter
#z = 15e-03              # source-to-detector distance in meter

def define_base(N):
    u = v = torch.linspace(-N/2,N/2-1,N)
    U,V = torch.meshgrid(u,v)
    pp = U**2+V**2
    return pp

def modifier(X,lmbd, N, s0, z0,pp,f1):
    hologram = X[:,:int(N)]
    #prop = torch.exp(-1j*torch.pi*lmbd*z0*pp.cuda()/(s0**2))
    prop = torch.exp(-1j*torch.pi*lmbd*z0*pp/(s0**2))
    #t = IFT2Dc(FT2Dc(hologram)*prop.conj())
    t = f1*torch.fft.fft2(f1*hologram)*prop.conj()
    t = f1.conj()*torch.fft.ifft2(f1.conj()*t)

    amp = t.abs()
    phase = t.angle()
    amp = (amp-amp.min())/(amp.max()-amp.min())*255
    phase = (phase-phase.min())/(phase.max()-phase.min())*255
    return  amp, phase


def FT2Dc(input):
    Nx = input.shape[0]
    Ny = input.shape[1]
    [U,V] = torch.meshgrid(torch.linspace(1,Nx,Nx),torch.linspace(1,Ny,Ny))
    out = torch.exp(1j*torch.pi*(U+V))#.cuda()
    #out = f1*torch.fft.fft2(f1*input)
    return out

def IFT2Dc(input):
    Nx = input.shape[0]
    Ny = input.shape[1]
    [U,V] = torch.meshgrid(torch.linspace(1,Nx,Nx),torch.linspace(1,Ny,Ny))
    out = torch.exp(-1j*torch.pi*(U+V))#.cuda()
    #out = f1*torch.fft.ifft2(f1*input)
    return out