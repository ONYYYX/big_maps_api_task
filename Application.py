from sys import argv, exit
from io import BytesIO
from requests import get
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from Interface import Ui_MainWindow as ApplicationMainWindow


class Application(QMainWindow, ApplicationMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.host = 'https://static-maps.yandex.ru/1.x/'
        self.size = 1050, 760
        self.type = 'map'
        self.coord = [49.620645, 54.216882]
        self.zoom = 3
        self.load_map()

    def load_map(self):
        map_params = {
            'll': ','.join(map(str, self.coord)),
            'l': self.type,
            'z': self.zoom,
            'size': ','.join(map(str, self.size))
        }
        self.map.setPixmap(QPixmap().loadFromData(bytes(BytesIO(get(self.host, params=map_params).content))))
        #  Либо так:
        #  self.map.setPixmap(QPixmap().loadFromData(get(self.host, params=map_params).content))
        #  Либо так:
        #  with open('temp.png', 'wb') as f:
        #       f.write(get(self.host, params=map_params).content)
        #       self.map.setPixmap(QPixmap('temp.png'))


if __name__ == '__main__':
    a = QApplication(argv)
    app = Application()
    app.show()
    exit(a.exec())
