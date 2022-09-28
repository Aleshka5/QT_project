import sys
import pickle
import logic
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Calculation_point(QThread):
    def __init__(self,variables,parent = None):
        super().__init__()
        self.values = variables
    def run(self):
        logic.start_calculate_2(self.values)

class PageWindow(QtWidgets.QMainWindow):
    page1_col1_labels = ['Напряжение нагрузки', 'Сопротивление нагрузки', 'Ток нагрузки',
                         'Сопротивление генератора', 'Коэффициент усиления', 'E максимально допустимое',
                         'Максимальное отклонение темпиратуры', 'Нижняя граничная частота',
                         'Ёмкость эмиттерного перехода', 'Ёмкость коллекторного перехода']
    page1_col2_labels = ['Ёмкость нагрузки', 'Частота единичного усиления', 'Дельта U нелинейное',
                         'Дельта U тепловое', 'Тепловой ток коллектора', 'Температурный коэффициент',
                         'Коэффициент усиления по току', 'Напряжение база-эмиттер',
                         'Входное сопротивление транзистора (h11)']
    page2_col1_labels = ['Ток коллектора', 'Ток базы', 'Ток эмиттера',
                         'Допустимый тепловой ток', 'Напряжение питания', 'Напряжение коллектор-эмиттер',
                         'Напряжение по переменному току', 'Сопротивление по постоянному току',
                         'Сопротивление по переменному току', 'Сопротивление коллектора', 'Первый расчёт Rб']
    page2_col2_labels = ['Коэффициент перераспределения тока коллектора', 'Тепловой разброс тока',
                         'Разброс тока из-за усиления',
                         'Суммарный разброс по току', 'Напряжение смещения',
                         'Тепловой запас напряжения', 'Нпряжение Uп', 'Сопротивление эмиттера',
                         'Сопротивление R1', 'Сопротивление R2', 'Результирующее Rб']
    page3_col1_labels = ['Входное сопротивление','Сопротивление эммитера Rэ1','Ёмкость конеденсатора Сp1','Ёмкость конеденсатора Сp2',
                         'Временная постоянная tau_in','Временная постоянная tau_out','Временная постоянная tau_v']
    page3_col2_labels = ['Сопротивление эммитера Rэ2','Сопротивление R ТРэ','Ёмкость конеденсатора Сэ','Ёмкость конеденсатора C_in',
                         'Временная постоянная tau н','Временная постоянная tau_T','Верхняя частота пропускания f_v','Рассчитанный коэффициент усиления']
    dict_results = {'Ток коллектора': 0,'Ток базы': 0, 'Ток эмиттера': 0, 'Допустимый тепловой ток': 0,
                    'Напряжение питания': 0, 'Напряжение коллектор-эмиттер': 0,
                    'Напряжение по переменному току': 0, 'Сопротивление по постоянному току': 0,
                    'Сопротивление по переменному току': 0, 'Сопротивление коллектора': 0,
                    'Первый расчёт Rб': 0, 'Коэффициент перераспределения тока коллектора': 0,
                    'Тепловой разброс тока': 0, 'Разброс тока из-за усиления': 0,
                    'Суммарный разброс по току': 0, 'Напряжение смещения': 0,
                    'Тепловой запас напряжения': 0, 'Нпряжение Uп': 0,
                    'Сопротивление эмиттера': 0, 'Сопротивление R1': 0, 'Сопротивление R2': 0,
                    'Результирующее Rб': 0,'Входное сопротивление':0,'Сопротивление эммитера Rэ1':0,
                    'Ёмкость конеденсатора Сp1':0,'Ёмкость конеденсатора Сp2':0,'Временная постоянная tau_in':0,
                    'Временная постоянная tau_out':0,'Временная постоянная tau_v':0,'Сопротивление эммитера Rэ2':0,
                    'Сопротивление R ТРэ':0,'Ёмкость конеденсатора Сэ':0,'Ёмкость конеденсатора C_in':0,
                    'Временная постоянная tau н':0,'Временная постоянная tau_T':0,'Верхняя частота пропускания f_v':0,'Рассчитанный коэффициент усиления':0}
    dict_variables = {'Напряжение нагрузки': 0, 'Сопротивление нагрузки': 0,
                      'Ток нагрузки': 0, 'Сопротивление генератора': 0,
                      'Коэффициент усиления': 0, 'E максимально допустимое': 0,
                      'Максимальное отклонение темпиратуры': 0,
                      'Нижняя граничная частота': 0, 'Ёмкость эмиттерного перехода': 0,
                      'Ёмкость коллекторного перехода': 0, 'Ёмкость нагрузки': 0,
                      'Частота единичного усиления': 0, 'Дельта U нелинейное': 0,
                      'Дельта U тепловое': 0, 'Тепловой ток коллектора': 0,
                      'Температурный коэффициент': 0, 'Коэффициент усиления по току': 0,
                      'Напряжение база-эмиттер': 0,
                      'Входное сопротивление транзистора (h11)': 0, 'Ток коллектора': 0,
                      'Ток базы': 0, 'Ток эммитера': 0, 'Допустимый тепловой ток': 0,
                      'Напряжение питания': 0, 'Напряжение коллектор-эмиттер': 0,
                      'Напряжение по переменному току': 0, 'Сопротивление по постоянному току': 0,
                      'Сопротивление по переменному току': 0, 'Сопротивление коллектора': 0,
                      'Первый расчёт Rб': 0, 'Коэффициент перераспределения тока коллектора': 0,
                      'Тепловой разброс тока': 0, 'Разброс тока из-за усиления': 0,
                      'Суммарный разброс по току': 0, 'Напряжение смещения': 0,
                      'Рассчитанный тепловой запас напряжения': 0, 'Нпряжение Uп': 0,
                      'Сопротивление эмиттера': 0, 'Сопротивление R1': 0, 'Сопротивление R2': 0,
                      'Результирующее Rб': 0,'Входное сопротивление':0,'Сопротивление эммитера Rэ1':0,
                      'Ёмкость конеденсатора Сp1':0,'Ёмкость конеденсатора Сp2':0,'Временная постоянная tau_in':0,
                      'Временная постоянная tau_out':0,'Временная постоянная tau_v':0,'Сопротивление эммитера Rэ2':0,
                      'Сопротивление R ТРэ':0,'Ёмкость конеденсатора Сэ':0,'Ёмкость конеденсатора C_in':0,
                      'Временная постоянная tau н':0,'Временная постоянная tau_T':0,'Верхняя частота пропускания f_v':0,'Рассчитанный коэффициент усиления':0}
    page1_col1_metrics = ['В','Ом','мА','Ом','','В','гр.С','Гц','пФ','пФ']
    page1_col2_metrics = ['нФ','МГц','В','В','мА','В/град','','В','Ом']
    page2_col1_metrics = ['мА','мкА','мА','мА','В','В','В','Ом','Ом','Ом','Ом']
    page2_col2_metrics = ['','мА','мА','мА','В','В','В','Ом','Ом','Ом','Ом']
    page3_col1_metrics = ['Ом','Ом','Ф','Ф','с','с','с']
    page3_col2_metrics = ['Ом','Ом','Ф','Ф','с','с','Гц','']
    font_size = 15
    dict_widgets = {}
    gotoSignal = QtCore.pyqtSignal(str)
    def __init__(self,parent = None):
        super().__init__(parent)
        self.clear_dict(self)

    def newFile(self):
        self.clear_dict(self)
        self.goto("startW")

    def openFile(self,Window):
        filename, filetype = QFileDialog.getOpenFileName(self,
                                                         "Выбрать файл",
                                                         ".",
                                                         "Pickle (*.pickle);;All Files(*)")
        if ".pickle" in filename:
            with open(filename, 'rb') as f:
                self.dict_variables = pickle.load(f)

            self.goto("firstW")
            self.Set_text(self)
        elif ((len(filename) > 0) and (".pickle" not in filename)):
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Информация")
            msg.setText("Выбран неподдерживаемый формат файла")
            x = msg.exec_()


    def saveFile(self,Window):
        filename, ok = QFileDialog.getSaveFileName(self,
                                                   "Сохранить файл",
                                                   ".",
                                                   "Pickle (*.pickle)")
        self.Get_text(self)
        #print(self.dict_widgets)
        #print(self.dict_variables)
        try:
            with open(filename,'wb') as f:
                pickle.dump(self.dict_variables,f)
        except:
            print("Error")
        finally:
            self.goto("firstW")

    def clear_dict(self,Window):
        self.dict_variables = {'Напряжение нагрузки': 0, 'Сопротивление нагрузки': 0,
                      'Ток нагрузки': 0, 'Сопротивление генератора': 0,
                      'Коэффициент усиления': 0, 'E максимально допустимое': 0,
                      'Максимальное отклонение темпиратуры': 0,
                      'Нижняя граничная частота': 0, 'Ёмкость эмиттерного перехода': 0,
                      'Ёмкость коллекторного перехода': 0, 'Ёмкость нагрузки': 0,
                      'Частота единичного усиления': 0, 'Дельта U нелинейное': 0,
                      'Дельта U тепловое': 0, 'Тепловой ток коллектора': 0,
                      'Температурный коэффициент': 0, 'Коэффициент усиления по току': 0,
                      'Напряжение база-эмиттер': 0,
                      'Входное сопротивление транзистора (h11)': 0, 'Ток коллектора': 0,
                      'Ток базы': 0, 'Ток эммитера': 0, 'Допустимый тепловой ток': 0,
                      'Напряжение питания': 0, 'Напряжение коллектор-эмиттер': 0,
                      'Напряжение по переменному току': 0, 'Сопротивление по постоянному току': 0,
                      'Сопротивление по переменному току': 0, 'Сопротивление коллектора': 0,
                      'Первый расчёт Rб': 0, 'Коэффициент перераспределения тока коллектора': 0,
                      'Тепловой разброс тока': 0, 'Разброс тока из-за усиления': 0,
                      'Суммарный разброс по току': 0, 'Напряжение смещения': 0,
                      'Рассчитанный тепловой запас напряжения': 0, 'Нпряжение Uп': 0,
                      'Сопротивление эмиттера': 0, 'Сопротивление R1': 0, 'Сопротивление R2': 0,
                      'Результирующее Rб': 0,'Входное сопротивление':0,'Сопротивление эммитера Rэ1':0,
                      'Ёмкость конеденсатора Сp1':0,'Ёмкость конеденсатора Сp2':0,'Временная постоянная tau_in':0,
                      'Временная постоянная tau_out':0,'Временная постоянная tau_v':0,'Сопротивление эммитера Rэ2':0,
                      'Сопротивление R ТРэ':0,'Ёмкость конеденсатора Сэ':0,'Ёмкость конеденсатора C_in':0,
                      'Временная постоянная tau н':0,'Временная постоянная tau_T':0,'Верхняя частота пропускания f_v':0,'Рассчитанный коэффициент усиления':0}
        PageWindow.dict_results = {'Ток коллектора': 0, 'Ток базы': 0, 'Ток эмиттера': 0, 'Допустимый тепловой ток': 0,
                        'Напряжение питания': 0, 'Напряжение коллектор-эмиттер': 0,
                        'Напряжение по переменному току': 0, 'Сопротивление по постоянному току': 0,
                        'Сопротивление по переменному току': 0, 'Сопротивление коллектора': 0,
                        'Первый расчёт Rб': 0, 'Коэффициент перераспределения тока коллектора': 0,
                        'Тепловой разброс тока': 0, 'Разброс тока из-за усиления': 0,
                        'Суммарный разброс по току': 0, 'Напряжение смещения': 0,
                        'Тепловой запас напряжения': 0, 'Нпряжение Uп': 0,
                        'Сопротивление эмиттера': 0, 'Сопротивление R1': 0, 'Сопротивление R2': 0,
                        'Результирующее Rб': 0, 'Входное сопротивление': 0, 'Сопротивление эммитера Rэ1': 0,
                        'Ёмкость конеденсатора Сp1': 0, 'Ёмкость конеденсатора Сp2': 0,
                        'Временная постоянная tau_in': 0,
                        'Временная постоянная tau_out': 0, 'Временная постоянная tau_v': 0,
                        'Сопротивление эммитера Rэ2': 0,
                        'Сопротивление R ТРэ': 0, 'Ёмкость конеденсатора Сэ': 0, 'Ёмкость конеденсатора C_in': 0,
                        'Временная постоянная tau н': 0, 'Временная постоянная tau_T': 0,
                        'Верхняя частота пропускания f_v': 0, 'Рассчитанный коэффициент усиления': 0}
        self.dict_results = {'Ток коллектора': 0, 'Ток базы': 0, 'Ток эмиттера': 0, 'Допустимый тепловой ток': 0,
                        'Напряжение питания': 0, 'Напряжение коллектор-эмиттер': 0,
                        'Напряжение по переменному току': 0, 'Сопротивление по постоянному току': 0,
                        'Сопротивление по переменному току': 0, 'Сопротивление коллектора': 0,
                        'Первый расчёт Rб': 0, 'Коэффициент перераспределения тока коллектора': 0,
                        'Тепловой разброс тока': 0, 'Разброс тока из-за усиления': 0,
                        'Суммарный разброс по току': 0, 'Напряжение смещения': 0,
                        'Тепловой запас напряжения': 0, 'Нпряжение Uп': 0,
                        'Сопротивление эмиттера': 0, 'Сопротивление R1': 0, 'Сопротивление R2': 0,
                        'Результирующее Rб': 0, 'Входное сопротивление': 0, 'Сопротивление эммитера Rэ1': 0,
                        'Ёмкость конеденсатора Сp1': 0, 'Ёмкость конеденсатора Сp2': 0,
                        'Временная постоянная tau_in': 0,
                        'Временная постоянная tau_out': 0, 'Временная постоянная tau_v': 0,
                        'Сопротивление эммитера Rэ2': 0,
                        'Сопротивление R ТРэ': 0, 'Ёмкость конеденсатора Сэ': 0, 'Ёмкость конеденсатора C_in': 0,
                        'Временная постоянная tau н': 0, 'Временная постоянная tau_T': 0,
                        'Верхняя частота пропускания f_v': 0, 'Рассчитанный коэффициент усиления': 0}
        for i in self.dict_widgets.keys():
            self.dict_widgets[i].clear()

    def Get_text(self,Window):
        for i in self.dict_widgets.keys():
            self.dict_variables[i] = self.dict_widgets[i].text()

    def Set_text(self,Window):
        for i in self.dict_variables.keys():
            if (i in self.dict_widgets.keys()) and (self.dict_variables[i] != '0'):
                self.dict_widgets[i].setText(str(self.dict_variables[i]))

    def copyContent(self):
        pass
    def pasteContent(self):
        pass
    def cutContent(self):
        pass
    def helpContent(self):
        pass
    def about(self):
        pass
    def exit(self):
        sys.exit()

    def set_in_widgets(self):
        j = 2
        k = 0
        i = 63
        if self.dict_widgets != {}:
            for key in self.dict_widgets.keys():
                if key in PageWindow.dict_results.keys():
                    try:
                        if 'tau н' in key:
                            self.dict_widgets[key].setText(str(PageWindow.dict_results[key]))
                        if PageWindow.dict_results[key].shape != 0:
                            if key == 'Ток базы':
                                print(f'!!!{str(PageWindow.dict_results[key].shape)}')
                                self.dict_widgets[key].setText(str(PageWindow.dict_results[key][i]*1000_000))
                            elif 'Сопротивление' in key or 'сопротивление' in key or 'Rб' in key or key == 'Напряжение смещения' or key == 'Тепловой запас напряжения' or key == 'Нпряжение Uп' or key == 'Коэффициент перераспределения тока коллектора':
                                print(f'!!!{str(PageWindow.dict_results[key].shape)}')
                                self.dict_widgets[key].setText(str(PageWindow.dict_results[key][j][k][i]))
                            elif key == 'Ток коллектора' or key == 'Ток эмиттера':
                                print(f'!!!{str(PageWindow.dict_results[key].shape)}')
                                self.dict_widgets[key].setText(str(PageWindow.dict_results[key][i]*1000))
                            elif key == 'Допустимый тепловой ток' or key == 'Тепловой разброс тока' or key == 'Разброс тока из-за усиления' or key == 'Суммарный разброс по току':
                                print(f'!!!{str(PageWindow.dict_results[key].shape)}')
                                self.dict_widgets[key].setText(str(PageWindow.dict_results[key][j][k][i] * 1000))
                            elif key == 'Напряжение питания':
                                print(f'!!!{str(PageWindow.dict_results[key].shape)}')
                                self.dict_widgets[key].setText(str(PageWindow.dict_results[key][j]))
                            elif key == 'Напряжение коллектор-эмиттер' or key == 'Напряжение по переменному току':
                                print(f'!!!{str(PageWindow.dict_results[key].shape)}')
                                self.dict_widgets[key].setText(str(PageWindow.dict_results[key][j][k]))
                            elif 'Ёмкость' in key:
                                self.dict_widgets[key].setText(str(PageWindow.dict_results[key][j][k][i]))
                            elif 'Временная' in key:
                                self.dict_widgets[key].setText(str(PageWindow.dict_results[key][j][k][i]))
                            elif key == 'Рассчитанный коэффициент усиления':
                                self.dict_widgets[key].setText(str(PageWindow.dict_results[key][j][k][i]))
                            elif key == 'Верхняя частота пропускания f_v':
                                self.dict_widgets[key].setText(str(PageWindow.dict_results[key][j][k][i]))
                    except:
                        pass
                        #print('No')

    def goto(self, name):
        self.set_in_widgets()
        self.gotoSignal.emit(name)

    def _createToolbars(self,Window):
        Page_Navigation_ToolBar = self.addToolBar('Pages')
        Page_Navigation_ToolBar.setMovable(False)
        Page_Navigation_ToolBar.addAction(self.ToFirstPageAction)
        Page_Navigation_ToolBar.addAction(self.ToSecondPageAction)
        Page_Navigation_ToolBar.addAction(self.ToThirdPageAction)

    def _connectActions(self,Window):
        self.newAction.triggered.connect(self.newFile)
        self.openAction.triggered.connect(self.openFile)
        self.saveAction.triggered.connect(self.saveFile)
        self.exitAction.triggered.connect(self.exit)

        self.copyAction.triggered.connect(self.copyContent)
        self.pasteAction.triggered.connect(self.pasteContent)
        self.cutAction.triggered.connect(self.cutContent)
        self.helpAction.triggered.connect(self.helpContent)
        self.aboutAction.triggered.connect(self.about)

        self.ToFirstPageAction.triggered.connect(self.make_handleButton('to_one'))
        self.ToSecondPageAction.triggered.connect(self.make_handleButton('to_two'))
        self.ToThirdPageAction.triggered.connect(self.make_handleButton('to_three'))

    def _createActions(self,Window):
        self.newAction = QAction(self)
        self.newAction.setText('New')
        self.openAction = QAction('Open',self)
        self.saveAction = QAction('Save', self)
        self.exitAction = QAction('Exit', self)
        self.copyAction = QAction('Copy', self)
        self.pasteAction = QAction('Paste', self)
        self.cutAction = QAction('Cut', self)
        self.helpAction = QAction('Help', self)
        self.aboutAction = QAction('About', self)
        self.ToFirstPageAction = QAction('First Page',self)
        self.ToSecondPageAction = QAction('Second Page', self)
        self.ToThirdPageAction = QAction('Third Page', self)

    def _createMenuBar(self,Window):
        menuBar = QMenuBar(self)
        self.setMenuBar(menuBar)
        fileMenu = QMenu('File', self)
        menuBar.addMenu(fileMenu)
        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.openAction)
        self.openRecentMenu = fileMenu.addMenu("Open Recent")
        fileMenu.addAction(self.saveAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAction)

        editMenu = menuBar.addMenu('Edit')
        editMenu.addAction(self.copyAction)
        editMenu.addAction(self.pasteAction)
        editMenu.addAction(self.cutAction)
        editMenu.addSeparator()
        findMenu = editMenu.addMenu('Find and Replace')
        findMenu.addAction('Find')
        findMenu.addAction('Replace')

        helpMenu = menuBar.addMenu('Help')
        helpMenu.addAction(self.helpAction)
        helpMenu.addAction(self.aboutAction)

    def set_static_UI(self, Window):
        self._createActions(self)
        self._createToolbars(self)
        self._connectActions(self)
        self._createMenuBar(self)


    def make_handleButton(self,button):
        def handleButton():
            if button == "to_start":
                self.goto("startW")
            if button == "to_one":
                self.goto("firstW")
            if button == "to_two":
                self.goto("secondW")
            if button == "to_three":
                self.goto("thirdW")
        return handleButton

class Calculation(QThread):
    def __init__(self,variables,parent = PageWindow):
        super().__init__()
        self.values = variables
    def run(self):
        PageWindow.dict_results = logic.start_calculate(self.values)

class StartWindow(PageWindow):
    def __init__(self):
        super().__init__()
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        self.btn = QPushButton('Button', self)
        self.btn.setGeometry(300, 300, 300, 200)
        self.btn.clicked.connect(self.make_handleButton('to_one'))
        self.initUI(self)
        self.setWindowTitle("StartWindow")

    def initUI(self,StartWindow):
        # Создание действий
        self.newAction = QAction(self)
        self.newAction.setText('New')
        self.openAction = QAction('Open', self)
        self.saveAction = QAction('Save', self)
        self.exitAction = QAction('Exit', self)
        self.copyAction = QAction('Copy', self)
        self.pasteAction = QAction('Paste', self)
        self.cutAction = QAction('Cut', self)
        self.helpAction = QAction('Help', self)
        self.aboutAction = QAction('About', self)
        # Создание меню бара
        menuBar = QMenuBar(self)
        self.setMenuBar(menuBar)
        fileMenu = QMenu('File', self)
        menuBar.addMenu(fileMenu)
        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.openAction)
        self.openRecentMenu = fileMenu.addMenu("Open Recent")
        fileMenu.addAction(self.saveAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAction)
        editMenu = menuBar.addMenu('Edit')
        editMenu.addAction(self.copyAction)
        editMenu.addAction(self.pasteAction)
        editMenu.addAction(self.cutAction)
        editMenu.addSeparator()
        findMenu = editMenu.addMenu('Find and Replace')
        findMenu.addAction('Find')
        findMenu.addAction('Replace')
        helpMenu = menuBar.addMenu('Help')
        helpMenu.addAction(self.helpAction)
        helpMenu.addAction(self.aboutAction)
        # Реализация действий
        self.newAction.triggered.connect(self.newFile)
        self.openAction.triggered.connect(self.openFile)
        self.saveAction.triggered.connect(self.saveFile)
        self.exitAction.triggered.connect(self.exit)
        self.copyAction.triggered.connect(self.copyContent)
        self.pasteAction.triggered.connect(self.pasteContent)
        self.cutAction.triggered.connect(self.cutContent)
        self.helpAction.triggered.connect(self.helpContent)
        self.aboutAction.triggered.connect(self.about)

class FirstWindow(PageWindow):
    def __init__(self):
        super().__init__()
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        self.setWindowTitle("FirstWindow")
        self.set_static_UI(self)
        self.Calculate_button = QPushButton('Calculate')
        self.Calculate_button.clicked.connect(self.Calc1)
        self.initUI(self)

    def Calc1(self, Window):
        self.Get_text(self)
        #for i,j in self.dict_variables.items():
        #    print(f"{i}->{j}")
        self.Calc_Process_instance = Calculation(self.dict_variables)
        self.Calc_Process_instance.start()


    def initUI(self, Window):
        button = self.Calculate_button
        first_column_labels = self.page1_col1_labels
        second_column_labels = self.page1_col2_labels
        first_column_metrics = self.page1_col1_metrics
        second_column_metrics = self.page1_col2_metrics
        self.grid_layout = QVBoxLayout(self.centralwidget)

        self.grid0 = QHBoxLayout()
        self.grid1 = QHBoxLayout()

        self.grid0_1 = QVBoxLayout()
        self.sep = QSpacerItem(100, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.grid0_2 = QVBoxLayout()

        max_length = max([len(i) for i in (first_column_labels + second_column_labels)])

        for i in range(len(first_column_labels)):
            gridlast = QHBoxLayout()
            label = QLabel()
            value = QLineEdit()
            metric = QLabel()

            #value.setFixedSize(120,40)
            value.setFont(QFont("Times", self.font_size))

            metric.setText(first_column_metrics[i])
            metric.setStyleSheet("QLabel{font-size: " + str(self.font_size) + "pt;}")
            metric.setFixedSize(40, 20)

            label.setText('|{:_>34}:'.format(first_column_labels[i]))
            label.setStyleSheet("QLabel{font-size: "+str(self.font_size)+"pt;}")
            label.setFixedSize(int(10 * max_length), 25)

            self.dict_widgets[first_column_labels[i]] = value

            gridlast.addWidget(label)
            gridlast.addWidget(value)
            gridlast.addWidget(metric)


            self.grid0_1.addLayout(gridlast)


        for i in range(len(second_column_labels)):
            gridlast = QHBoxLayout()
            label = QLabel()
            value = QLineEdit()
            metric = QLabel()

            value.setFont(QFont("Times", self.font_size))

            metric.setText(second_column_metrics[i])
            metric.setStyleSheet("QLabel{font-size: " + str(self.font_size) + "pt;}")
            metric.setFixedSize(40, 20)

            label.setText('|{:_>36}:'.format(second_column_labels[i]))
            label.setStyleSheet("QLabel{font-size: "+str(self.font_size)+"pt;}")
            label.setFixedSize(int(10.5 * max_length), 25)

            self.dict_widgets[second_column_labels[i]] = value

            gridlast.addWidget(label)
            gridlast.addWidget(value)
            gridlast.addWidget(metric)

            self.grid0_2.addLayout(gridlast)


        self.grid0.addLayout(self.grid0_1)
        self.grid0.addItem(self.sep)
        self.grid0.addLayout(self.grid0_2)

        self.grid1.addWidget(QLineEdit())
        self.grid1.addWidget(button)

        self.grid_layout.addLayout(self.grid0)
        self.grid_layout.addLayout(self.grid1)

class SecondWindow(PageWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SecondWindow")
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        self.set_static_UI(self)
        self.Calculate_button = QPushButton('Calculate')
        self.Calculate_button.clicked.connect(self.Calc2)
        self.init_input_UI(self)

    def Calc2(self, Window):
        self.Get_text(self)
        for i, j in self.dict_variables.items():
            print(f"{i}->{j}")
        self.Calc_2_Process_instance = Calculation_point(self.dict_variables)
        self.Calc_2_Process_instance.start()

    def init_input_UI(self,Window):
        button = self.Calculate_button
        first_column_labels = self.page2_col1_labels
        second_column_labels = self.page2_col2_labels
        first_column_metrics = self.page2_col1_metrics
        second_column_metrics = self.page2_col2_metrics
        self.grid_layout = QVBoxLayout(self.centralwidget)

        self.grid0 = QHBoxLayout()
        self.grid1 = QHBoxLayout()

        self.grid0_1 = QVBoxLayout()
        self.sep = QSpacerItem(100, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.grid0_2 = QVBoxLayout()

        max_length = max([len(i) for i in (first_column_labels + second_column_labels)])
        for i in range(len(first_column_labels)):
            gridlast = QHBoxLayout()
            value = QLineEdit()
            label = QLabel()
            metric = QLabel()

            value.setFont(QFont("Times", self.font_size))

            metric.setText(first_column_metrics[i])
            metric.setStyleSheet("QLabel{font-size: " + str(self.font_size) + "pt;}")
            metric.setFixedSize(40, 20)

            value.setFont(QFont("Times", self.font_size))

            label.setText('|{:_>32}:'.format(first_column_labels[i]))
            label.setStyleSheet("QLabel{font-size: "+str(self.font_size)+"pt;}")
            label.setFixedSize(int(8 * max_length), 25)

            self.dict_widgets[first_column_labels[i]] = value

            gridlast.addWidget(label)
            gridlast.addWidget(value)
            gridlast.addWidget(metric)

            self.grid0_1.addLayout(gridlast)


        for i in range(len(second_column_labels)):
            gridlast = QHBoxLayout()
            label = QLabel()
            value = QLineEdit()
            metric = QLabel()

            value.setFont(QFont("Times", self.font_size))

            metric.setText(second_column_metrics[i])
            metric.setStyleSheet("QLabel{font-size: " + str(self.font_size) + "pt;}")
            metric.setFixedSize(40, 20)

            value.setFont(QFont("Times", self.font_size))

            label.setText('|{:_>43}:'.format(second_column_labels[i]))
            label.setStyleSheet("QLabel{font-size: "+str(self.font_size)+"pt;}")
            label.setFixedSize(int(11 * max_length), 25)

            self.dict_widgets[second_column_labels[i]] = value

            gridlast.addWidget(label)
            gridlast.addWidget(value)
            gridlast.addWidget(metric)

            self.grid0_2.addLayout(gridlast)

        self.grid0.addLayout(self.grid0_1)
        self.grid0.addItem(self.sep)
        self.grid0.addLayout(self.grid0_2)

        self.grid1.addWidget(QLineEdit())
        self.grid1.addWidget(button)

        self.grid_layout.addLayout(self.grid0)
        self.grid_layout.addLayout(self.grid1)

class ThirdWindow(PageWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ThirdWindow")
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        self.set_static_UI(self)
        self.Calculate_button = QPushButton('Calculate')
        #self.Calculate_button.clicked.connect(self.Calc2)
        self.init_input_UI(self)

    def init_input_UI(self, Window):
        button = self.Calculate_button
        first_column_labels = self.page3_col1_labels
        second_column_labels = self.page3_col2_labels
        first_column_metrics = self.page3_col1_metrics
        second_column_metrics = self.page3_col2_metrics
        self.grid_layout = QVBoxLayout(self.centralwidget)

        self.grid0 = QHBoxLayout()
        self.grid1 = QHBoxLayout()

        self.grid0_1 = QVBoxLayout()
        self.sep = QSpacerItem(100, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.grid0_2 = QVBoxLayout()

        max_length = max([len(i) for i in (first_column_labels + second_column_labels)])
        for i in range(len(first_column_labels)):
            gridlast = QHBoxLayout()
            value = QLineEdit()
            label = QLabel()
            metric = QLabel()

            value.setFont(QFont("Times", self.font_size))

            metric.setText(first_column_metrics[i])
            metric.setStyleSheet("QLabel{font-size: " + str(self.font_size) + "pt;}")
            metric.setFixedSize(40, 20)

            value.setFont(QFont("Times", self.font_size))

            label.setText('|{:_>32}:'.format(first_column_labels[i]))
            label.setStyleSheet("QLabel{font-size: " + str(self.font_size) + "pt;}")
            label.setFixedSize(int(11 * max_length), 25)

            self.dict_widgets[first_column_labels[i]] = value

            gridlast.addWidget(label)
            gridlast.addWidget(value)
            gridlast.addWidget(metric)

            self.grid0_1.addLayout(gridlast)

        for i in range(len(second_column_labels)):
            gridlast = QHBoxLayout()
            label = QLabel()
            value = QLineEdit()
            metric = QLabel()

            value.setFont(QFont("Times", self.font_size))

            metric.setText(second_column_metrics[i])
            metric.setStyleSheet("QLabel{font-size: " + str(self.font_size) + "pt;}")
            metric.setFixedSize(40, 20)

            value.setFont(QFont("Times", self.font_size))

            label.setText('|{:_>35}:'.format(second_column_labels[i]))
            label.setStyleSheet("QLabel{font-size: " + str(self.font_size) + "pt;}")
            label.setFixedSize(int(12 * max_length), 25)

            self.dict_widgets[second_column_labels[i]] = value

            gridlast.addWidget(label)
            gridlast.addWidget(value)
            gridlast.addWidget(metric)

            self.grid0_2.addLayout(gridlast)

        self.grid0.addLayout(self.grid0_1)
        self.grid0.addItem(self.sep)
        self.grid0.addLayout(self.grid0_2)

        self.grid1.addWidget(QLineEdit())
        self.grid1.addWidget(button)

        self.grid_layout.addLayout(self.grid0)
        self.grid_layout.addLayout(self.grid1)


class Window(QtWidgets.QMainWindow):
    # Инициализация главного окна
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Start Window")
        self.resize(1920//2, 1080//2)
        self.stacked_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)


        self.m_pages = {}
        # Запись всех страниц в словарь
        self.register(StartWindow(), "startW")
        self.register(FirstWindow(), "firstW")
        self.register(SecondWindow(), "secondW")
        self.register(ThirdWindow(), "thirdW")
        self.goto("startW")
    # Функция записи страницы с title = name в словарь
    def register(self, widget, name):
        self.m_pages[name] = widget
        self.stacked_widget.addWidget(widget)
        if isinstance(widget, PageWindow):
            widget.gotoSignal.connect(self.goto)

    @QtCore.pyqtSlot(str)
    def goto(self,name):
        if name in self.m_pages:
            widget = self.m_pages[name]
            self.stacked_widget.setCurrentWidget(widget)
            self.setWindowTitle(widget.windowTitle())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())