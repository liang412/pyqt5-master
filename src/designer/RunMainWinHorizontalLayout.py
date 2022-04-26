import sys
import MainWinHorizontalLayout
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)  # 传入参数，固定写法
    mainWindow = QMainWindow()  # 创建主窗口
    ui = MainWinHorizontalLayout.Ui_MainWindow()
    # 向主窗口上添加控件
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())  # 进入主循环