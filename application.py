import sys
import qdarkstyle
from PyQt5.QtWidgets import QApplication
from ui import MainWindow
from opt import ConstrainedOpt
from model import sgan

if __name__ == "__main__":
    model = sgan.Model("params/sgan_model.ckpt")
    opt_engine = ConstrainedOpt(model)

    # initialize application
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet(pyside=False))
    window = MainWindow(opt_engine)
    window.setWindowTitle("pix2vox")
    window.show()
    window.viewerWidget.interactor.Initialize()
    sys.exit(app.exec_())
