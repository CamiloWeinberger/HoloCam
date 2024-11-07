from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPixmap, QImage, QPainter, QPen
from PyQt6.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from io import BytesIO
import numpy as np


def plot_on_label(label: QLabel, y: np.array):
            # Create a Matplotlib figure and plot data
            fig = Figure()
            canvas = FigureCanvas(fig)
            #ax = fig.add_subplot(111)
            ax = fig.add_axes([0, 0, 1, 1])
            ax.axis('off')
            # Example data to plot
            x = range(y.shape[-1])
            ax.set_xlim([0,x[-1]])
            ax.plot(x, y)
            # Save the plot to a BytesIO buffer as a PNG image
            buf = BytesIO()
            canvas.print_png(buf)
            buf.seek(0)

            # Convert the PNG buffer data to a QPixmap
            pixmap = QPixmap()
            pixmap.loadFromData(buf.getvalue())
            pixmap = pixmap.scaled(label.size())#, Qt.AspectRatioMode.KeepAspectRatioByExpanding, Qt.TransformationMode.SmoothTransformation)

            # Set the QPixmap on the QLabel (self.im_line)
            label.setPixmap(pixmap)  # Ensure that self.im_line is the QLabel's name in your .ui file


def set_single_channel_image_from_numpy(label: QLabel, np_image: np.ndarray,line_amp):
    """
    Convert a single-channel (grayscale) numpy image array to a QImage and set it in the QLabel.
    
    Args:
        label (QLabel): The QLabel where the image will be displayed.
        np_image (np.ndarray): The numpy array containing the single-channel image data.
    """
    # Ensure the image is 2D (grayscale image)
    h, w = np_image.shape
    # Create QImage from numpy array (Format_Grayscale8)
    q_image = QImage(np.uint8(np_image).data, w, h, QImage.Format.Format_Grayscale8)
    
    # Convert QImage to QPixmap
    pixmap = QPixmap.fromImage(q_image)
    
    # Create a QPainter object to draw on the QPixmap
    if line_amp is not None:
        painter = QPainter(pixmap)
        pen = QPen(Qt.GlobalColor.red, 3)  # Set the color and thickness of the line
        painter.setPen(pen)
        painter.drawLine(0, line_amp, np_image.shape[0], line_amp)
        painter.end()
    
    # Scale the QPixmap to fit the QLabel while keeping the aspect ratio
    scaled_pixmap = pixmap.scaled(label.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
    # Set the QPixmap on the QLabel
    label.setPixmap(scaled_pixmap)
    
    # Optionally, center the QLabel content
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)