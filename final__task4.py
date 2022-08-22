from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from pyqtgraph import PlotWidget, PlotItem
import pyqtgraph as pg
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sympy
from sympy import S, symbols, printing
import sys
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import matplotlib.pylab as plt
import math 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(777, 672)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        #self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        #self.label_6.setText("")
        #self.label_6.setObjectName("label_6")
        #self.horizontalLayout.addWidget(self.label_6)
        self.verticalLayout_7.addWidget(self.groupBox_2)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.widget_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.percentag_error = QtWidgets.QLabel(self.widget_2)
        self.percentag_error.setText("")
        self.percentag_error.setObjectName("percentag_error")

        self.percentag_error.setStyleSheet("background-color: lightgreen;  border: 1px solid black;")
       # self.percentag_error.resize(200,20)
        #self.percentag_error.setFont(QtCore.Qt.Font(10))
        #self.percentag_error.setAlignment(self.AlignCenter)
        #self.verticalLayout_6.addWidget(self.percentag_error) ori

        self.verticalLayout_6.addWidget(self.percentag_error, 0, QtCore.Qt.AlignHCenter)
        #self.verticalLayout_7.addWidget(self.widget_2, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_7.addWidget(self.widget_2)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.main_graph= PlotWidget(self.centralwidget)
 
        self.main_graph.setObjectName("main_graph\n""")
        self.main_graph.setBackground("w")


        self.verticalLayout_5.addWidget(self.main_graph)

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Chunks_Equations_Combobox = QtWidgets.QComboBox(self.groupBox)
        self.Chunks_Equations_Combobox.setObjectName("Chunks_Equations_Combobox")
        self.Chunks_Equations_Combobox.addItem("")
        self.verticalLayout.addWidget(self.Chunks_Equations_Combobox)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.num_of_chunks = QtWidgets.QLineEdit(self.groupBox)
        self.num_of_chunks.setObjectName("num_of_chunks")
        self.verticalLayout.addWidget(self.num_of_chunks)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.order_of_fitting = QtWidgets.QSpinBox(self.groupBox)
        self.order_of_fitting.setObjectName("order_of_fitting")
        self.verticalLayout.addWidget(self.order_of_fitting)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.clipping_percentage = QtWidgets.QSpinBox(self.groupBox)
        self.clipping_percentage.setObjectName("clipping_percentage")
        self.verticalLayout.addWidget(self.clipping_percentage)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        #self.Error_map_label = QtWidgets.QLabel(self.widget)
        #self.Error_map_label.setText("")
        #self.Error_map_label.setObjectName("Error_map_label")
        #self.verticalLayout_2.addWidget(self.Error_map_label)
        self.verticalLayout_4.addWidget(self.widget)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.x_axis = QtWidgets.QComboBox(self.groupBox_5)
        self.x_axis.setObjectName("x_axis")
        #options=["x-axis","number of chunks","order of polynomial"]
        #self.x_axis.addItems(options)
        self.x_axis.addItem("")
        self.x_axis.addItem("")
        self.x_axis.addItem("")
        self.x_axis.addItem("")
        self.horizontalLayout_3.addWidget(self.x_axis)
        self.y_axis = QtWidgets.QComboBox(self.groupBox_5)
        self.y_axis.setObjectName("y_axis")
        #self.y_axis.addItems(options)
        self.y_axis.addItem("")
        self.y_axis.addItem("")
        self.y_axis.addItem("")
        self.y_axis.addItem("")
        self.horizontalLayout_3.addWidget(self.y_axis)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        #self.Controlling_Factor_Label = QtWidgets.QLabel(self.groupBox_5)
        #self.Controlling_Factor_Label.setObjectName("Controlling_Factor_Label")
        #self.verticalLayout_3.addWidget(self.Controlling_Factor_Label)
        #self.Controlling_Factor_EditLine = QtWidgets.QLineEdit(self.groupBox_5)
        #self.Controlling_Factor_EditLine.setObjectName("Controlling_Factor_EditLine")
        #self.verticalLayout_3.addWidget(self.Controlling_Factor_EditLine)
        self.Overlapping_Label = QtWidgets.QLabel(self.groupBox_5)
        self.Overlapping_Label.setObjectName("Overlapping_Label")
        self.verticalLayout_3.addWidget(self.Overlapping_Label)
        self.Overlapping_EditLine = QtWidgets.QLineEdit(self.groupBox_5)
        self.Overlapping_EditLine.setObjectName("Overlapping_EditLine")
        self.verticalLayout_3.addWidget(self.Overlapping_EditLine)
        self.generate_an_error_map = QtWidgets.QPushButton(self.groupBox_5)
        self.generate_an_error_map.setObjectName("generate_an_error_map")
        self.verticalLayout_3.addWidget(self.generate_an_error_map)
        self.verticalLayout_4.addWidget(self.groupBox_5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_8.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 777, 18))
        self.menubar.setObjectName("menubar")
        self.menuOpen = QtWidgets.QMenu(self.menubar)
        self.menuOpen.setObjectName("menuOpen")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.menuOpen.addAction(self.actionOpen)
        self.menubar.addAction(self.menuOpen.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.order_of_fitting.setValue(3)
        self.actionOpen.triggered.connect(lambda: self.open_file())
        self.order_of_fitting.valueChanged.connect(self.Update_maingraph)
        self.clipping_percentage.valueChanged.connect(self.extrapolation)
        self.num_of_chunks.setText("8")
        self.num_of_chunks.textChanged.connect(self.Update_maingraph)
        self.generate_an_error_map.clicked.connect(self.Generate_error_map)

        self.pbar = QtWidgets.QProgressBar()
        self.pbar.setGeometry(30, 40, 200, 25)
        self.verticalLayout_3.addWidget(self.pbar)
        self.pbar.setMaximum(100)

        self.Canvas_for_equation = MplCanvas(self, width=3, height=0.4)
        self.horizontalLayout.addWidget(self.Canvas_for_equation)

        
        self.Canvas_for_errormap = MplCanvas2(self)
        self.verticalLayout_2.addWidget(self.Canvas_for_errormap)
        self.Chunks_Equations_Combobox.activated.connect(self.chunk_displayed)
        self.generate_is_pressed = False
        self.generate_an_error_map.setStyleSheet("background-color : lightgreen")
        
    def open_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "",                                                  "All Files (*);;csv Files (*.csv)", options=options)
        if fileName:
            self.read_file(fileName)

    def read_file(self, file_path):
        self.main_graph.clear()
        path = file_path
        data = pd.read_csv(path)
        #self.t = np.arange(0, 9.99, 0.01)
        self.t = data.values[:, 0]
        self.amp = data.values[:, 1]
        self.main_graph.plot(self.t, self.amp)
        self.interpolatian( 8,3)
        
    def interpolatian(self,number_of_chunks,order_of_polynomial):
        chunks_x = np.array_split(self.t,number_of_chunks)
        chunks_y=np.array_split(self.amp, number_of_chunks)
        self.All_chunks_parameters=[]
        self.equation_list=[]
        self.error_for_all_chunks=[]

        for chunk_number in range(len(chunks_x)):
            self.parameters_Array = np.polyfit(chunks_x[chunk_number],chunks_y[chunk_number],order_of_polynomial)
            self.All_chunks_parameters.append(self.parameters_Array)
            y_fitting_list=[]
            error_for_each_chunk=[]

            for x in (chunks_x[chunk_number]):
                index_x = list(chunks_x[chunk_number]).index(x)
                y_fitting=0
                for i in range(len( self.parameters_Array)):
                     y_fitting+=self.parameters_Array[i]*(x**(order_of_polynomial-i))
                error_for_each_point=(y_fitting-chunks_y[chunk_number][index_x])**2
                error_for_each_chunk.append(error_for_each_point)
                y_fitting_list.append( y_fitting)
            
            percentage_error_for_each_chunk=math.sqrt((sum(error_for_each_chunk)/len(chunks_x[chunk_number])))*100
            self.error_for_all_chunks.append( percentage_error_for_each_chunk)
            self.percentag_error.setText("Percentage Error= "+ str(percentage_error_for_each_chunk)+ "%")
            self.main_graph.plot(chunks_x[chunk_number],np.array(y_fitting_list),pen=pg.mkPen(color=(255, 148, 4),width=3, style=QtCore.Qt.DotLine))
            self.main_graph.plot(self.t, self.amp,pen=pg.mkPen(color=(0, 0, 0),width=2,style=QtCore.Qt.SolidLine))    
        x = symbols("x")
        for i in range(len(self.All_chunks_parameters)):
             poly = sum(S("{:6.2f}".format(v)) * x ** i for i, v in enumerate(self.All_chunks_parameters[i][::-1]))
             eq_latex = printing.latex(poly)
             label = "${}$".format(eq_latex)
             self.equation_list.append(label)
             self.Chunks_Equations_Combobox.addItem(str(i+1))
             self.Canvas_for_equation .fig.suptitle(label)
             self.Canvas_for_equation .draw()
        self.main_graph.addLegend()
        self.main_graph.setLabel("left", "Amplitude (volt)")
        self.main_graph.setLabel("bottom", "Time (t)")
        self.main_graph.showGrid(x=True, y=True)

    def Update_maingraph(self):
        self.main_graph.clear()
        self.main_graph.plot(self.t, self.amp,pen=pg.mkPen(color=(0, 0, 0),width=2,style=QtCore.Qt.SolidLine))
        self.interpolatian( int(self.num_of_chunks.text()),self.order_of_fitting.value())

    def  overlap(self,chunks_x,overlap):
        chunks_x_overlaped=[chunks_x[0]]

        for chunk_number in range(1,len(chunks_x)):
            num_of_elements = int(overlap*len(chunks_x[chunk_number]))*chunk_number
            chunkx_new=[]
            for x in (chunks_x[chunk_number]):
                 xnew=x-num_of_elements
                 chunkx_new.append(xnew)
            chunks_x_overlaped.append( chunkx_new) 
        return chunks_x_overlaped

    def calculate_error_map(self,number_of_chunks,order_of_polynomial,overlap):
        chunks_x = np.array_split(self.t,number_of_chunks)
        chunks_x = self.overlap(chunks_x,overlap)
        chunks_y=np.array_split(self.amp, number_of_chunks)
        error_for_all_chunks=[]

        for chunk_number in range(len(chunks_x)):
            self.parameters_Array = np.polyfit(chunks_x[chunk_number],chunks_y[chunk_number],order_of_polynomial)
            y_fitting_list=[]
            error_for_each_chunk=[]

            for x in (chunks_x[chunk_number]):
                 index_x = list(chunks_x[chunk_number]).index(x)
                 y_fitting=0

                 for i in range(len( self.parameters_Array)):
                     y_fitting+=self.parameters_Array[i]*(x**(order_of_polynomial-i))
                 error_for_each_point=(y_fitting-chunks_y[chunk_number][index_x])**2
                 error_for_each_chunk.append(error_for_each_point)
                 y_fitting_list.append( y_fitting)
            error_for_each_chunk=math.sqrt((sum(error_for_each_chunk)/len(chunks_x[chunk_number])))
            error_for_all_chunks.append( error_for_each_chunk)
            
        return (sum(error_for_all_chunks)/number_of_chunks)

    def axes_of_error_map(axis):
        if axis=="num pf chunks" or axis=="number of chunks":
             return int(self.num_of_chunks.text()) //3
        if axis=="order of fitting" :
            return self.order_of_fitting.value() //4
        if axis=="overlapping" :
            return 5
 
            
    def Generate_error_map(self):
        self.generate_an_error_map.setText("Cancel")
        self.generate_an_error_map.setStyleSheet("background-color : red")
        #self.Canvas_for_errormap.axes.clear()
        self.Canvas_for_errormap.fig.clear()
        self.axes = self.Canvas_for_errormap.fig.add_subplot(111)
        #self.cbar.remove()
        self.Canvas_for_errormap.draw()
        rows, cols = 5,5

        overlap_list=np.arange(0,30,5)
        x=self.x_axis.currentIndex()
        y= self.y_axis.currentIndex()
        overlap_list=np.arange(0,20,1)
        #print(overlap_list)
        #print(len(overlap_list))
        z = int( self.Overlapping_EditLine.text())
        arr=[]
        for i in range(rows):
           col = []
           for j in range( cols):
               #condlist = [x==1 and y==2, x==2 and y==1]
               #choicelist = [col.append(self.calculate_error_map(j+1,i+1,z/100)), col.append(self.calculate_error_map(i+1,j+1,z/100))]
               #np.select(condlist, choicelist)
               #print(np.select(condlist, choicelist))
               dic={bool(x==1 and y==2):self.calculate_error_map(j+1,i+1,z/100),bool( x==2 and y==1):self.calculate_error_map(i+1,j+1,z/100)}
               a=dic.get(True)
               col.append(a)
              #if self.x_axis.currentIndex()==1 and self.y_axis.currentIndex()==2:
              #   col.append(self.calculate_error_map(j+1,i+1,z/100)) #number,order
              #if self.x_axis.currentIndex()==2 and self.y_axis.currentIndex()==1:
              #    col.append(self.calculate_error_map(i+1,j+1,z/100)) #order,number
              #if self.x_axis.currentIndex()==3 and self.y_axis.currentIndex()==1:
              #   col.append(self.calculate_error_map(i+1,z,overlap_list[j]/100))  #overlap,number
              #if self.x_axis.currentIndex()==3 and self.y_axis.currentIndex()==2:
              #   col.append(self.calculate_error_map(z,i+1,overlap_list[j]/100))  #overlap,order
              #if self.x_axis.currentIndex()==1 and self.y_axis.currentIndex()==3:
              #   col.append(self.calculate_error_map(j+1,z,overlap_list[i]/100))  #number,overlap
              #if self.x_axis.currentIndex()==2 and self.y_axis.currentIndex()==3:
              #   col.append(self.calculate_error_map(z,j+1,overlap_list[i]/100))  #order,overlap
           print(len(col))
           arr.append(col)
           self.pbar.setValue((i+1)*10)
        
        self.canv = self.axes.imshow(np.array(arr), interpolation = 'nearest',cmap="rainbow", extent = [0.5,5.5,0.5,5.5],origin="lower")
        self.Canvas_for_errormap.draw()
        self.cbar = self.Canvas_for_errormap.fig.colorbar(self.canv)
        self.generate_an_error_map.setText("Generate an error map")
        self.generate_an_error_map.setStyleSheet("background-color : lightgreen")
        #self.Canvas_for_errormap.axes.set_xticks(np.arange(1,cols+1))
        #self.Canvas_for_errormap.axes.set_yticks(np.arange(1,rows+1))
        #self.Canvas_for_errormap.axes.set_xlabel(self.x_axis.currentText())
        #self.Canvas_for_errormap.axes.set_ylabel(self.y_axis.currentText())
        #self.Canvas_for_errormap.axes.set_title('error map')

        self.axes.set_xticks(np.arange(1,cols+1))
        self.axes.set_yticks(np.arange(1,rows+1))
        self.axes.set_xlabel(self.x_axis.currentText())
        self.axes.set_ylabel(self.y_axis.currentText())
        self.axes.set_title('error map')


        self.Canvas_for_errormap.draw()
        #self.verticalLayout_2.addWidget(self.canv)


    def extrapolation(self,clipping_percentage):
        self.main_graph.clear()
        chunks_x = np.array_split(self.t,10)
        chunks_y = np.array_split(self.amp,10)
        number_chunks_concatenating=clipping_percentage/10
        concatenating_list_x=[]
        concatenating_list_y=[]

        for i in range(int(number_chunks_concatenating)):
            concatenating_list_x+=list(chunks_x[i])
            concatenating_list_y+=list(chunks_y[i])
        self.parameters_Array = np.polyfit(concatenating_list_x,concatenating_list_y,self.order_of_fitting.value())
        y_fitting_list=[]

        for x in (self.t):
                y_fitting=0
                for i in range(len( self.parameters_Array)):
                     y_fitting+=self.parameters_Array[i]*(x**(self.order_of_fitting.value()-i))
                y_fitting_list.append( y_fitting)
        
        self.main_graph.plot(self.t,self.amp,pen=pg.mkPen(color=(0, 0, 0),width=2,style=QtCore.Qt.SolidLine) , name='The Orignal Signal')
        self.main_graph.plot(self.t,np.array(y_fitting_list),pen=pg.mkPen(color=(0, 255, 255),width=5, style=QtCore.Qt.DotLine), name='The Fitted Curve')
        self.main_graph.addLegend()
        self.main_graph.setLabel("left", "Amplitude (volt)")
        self.main_graph.setLabel("bottom", "Time (t)")
        self.main_graph.showGrid(x=True, y=True)

    def chunk_displayed(self,i):
        self.Canvas_for_equation.fig.suptitle(self.equation_list[i])
        self.Canvas_for_equation.draw()
        self.percentag_error.setText("percentag error = "+ str(self.error_for_all_chunks[i])+"%")      

    #def toggle_button(self):
    #    if  self.generate_is_pressed == False:
    #        self.generate_is_pressed = True
    #        self.pbar.setVisible(True)
    #        self.Generate_error_map()   
    #    else: 
    #        self.generate_is_pressed = False
    #        self.pbar.setVisible(True)
    #        self.Canvas_for_errormap.axes.cla()
    #        self.Canvas_for_errormap.draw()
    #        self.cbar.remove()
    #        self.cbar.remove()
            
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainWindow", "The fitting Equation"))
        self.groupBox.setTitle(_translate("MainWindow", "The control of the main graph"))
        self.Chunks_Equations_Combobox.setItemText(0, _translate("MainWindow", "Chunks Equations"))
        self.label_3.setText(_translate("MainWindow", "Num of chunks"))
        self.label_4.setText(_translate("MainWindow", "Order of Fitting"))
        self.label_7.setText(_translate("MainWindow", "Clipping"))
        self.groupBox_5.setTitle(_translate("MainWindow", "The control of the error map"))
        self.x_axis.setItemText(0, _translate("MainWindow", "x- axis "))
        self.x_axis.setItemText(1, _translate("MainWindow", "number of chunks"))
        self.x_axis.setItemText(2, _translate("MainWindow", "order of fitting"))
        self.x_axis.setItemText(3, _translate("MainWindow", "overlapping percentage"))
        self.y_axis.setItemText(0, _translate("MainWindow", "y - axis"))
        self.y_axis.setItemText(1, _translate("MainWindow", "number of chunks"))
        self.y_axis.setItemText(2, _translate("MainWindow", "order of fitting "))
        self.y_axis.setItemText(3, _translate("MainWindow", "overlapping percentage "))
        #self.Controlling_Factor_Label.setText(_translate("MainWindow", "Controlling Factor"))
        self.Overlapping_Label.setText(_translate("MainWindow", "Z constant"))
        self.generate_an_error_map.setText(_translate("MainWindow", "Generate an error map"))
        self.menuOpen.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))

class MplCanvas(FigureCanvasQTAgg):
   def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        super(MplCanvas, self).__init__(self.fig) 

class MplCanvas2(FigureCanvasQTAgg):
   def __init__(self, parent=None, width=3.5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.fig.tight_layout()      
        self.axes = self.fig.add_subplot(111)
        super(MplCanvas2, self).__init__(self.fig) 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

