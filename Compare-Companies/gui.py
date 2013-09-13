import sys
from PyQt4 import QtGui, QtCore
import comparison

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        #set labels for company
        self.label1 = QtGui.QLabel("Company-1", self)
        self.label2 = QtGui.QLabel("Company-2", self)

        #set labels for date
        self.label3 = QtGui.QLabel("Start Date", self)
        self.label4 = QtGui.QLabel("End Date", self)

        #combo box for companies
        comp1 = self.comp1 = QtGui.QComboBox(self)
        comp2 = self.comp2 = QtGui.QComboBox(self)

        #combo box for start day, month, year
        day1 = self.day1 = QtGui.QComboBox(self)
        month1 = self.month1 = QtGui.QComboBox(self)
        year1 = self.year1 = QtGui.QComboBox(self)

        #combo box for end day, month, year
        day2 = self.day2 = QtGui.QComboBox(self)
        month2 = self.month2 = QtGui.QComboBox(self)
        year2 = self.year2 = QtGui.QComboBox(self)

        #get list of companies & add to combo
        ls_comp = []
        for line in open('list.txt','r').readlines():
            ls_comp.append(line.strip())
        for i in ls_comp:
            comp1.addItem(i)
        for i in ls_comp:
            comp2.addItem(i)

        #get list of days & add to combo
        ls_day = []
        for line in open('day.txt','r').readlines():
            ls_day.append(line.strip())
        for i in ls_day:
            day1.addItem(i)
        for i in ls_day:
            day2.addItem(i)

        #get list of months & add to combo
        ls_month = []
        for line in open('month.txt','r').readlines():
            ls_month.append(line.strip())
        for i in ls_month:
            month1.addItem(i)
        for i in ls_month:
            month2.addItem(i)

        #get list of years & add to combo
        ls_year = []
        for line in open('year.txt','r').readlines():
            ls_year.append(line.strip())
        for i in ls_year:
            year1.addItem(i)
        for i in ls_year:
            year2.addItem(i)                

        #move & resize combo boxes
        comp1.move(200, 100)
        comp1.resize(100, 50)

        comp2.move(200, 200)
        comp2.resize(100, 50)

        day1.move(100, 330)
        day1.resize(50, 30)

        day2.move(100, 430)
        day2.resize(50, 30)

        month1.move(160, 330)
        month1.resize(50, 30)

        month2.move(160, 430)
        month2.resize(50, 30)

        year1.move(220, 330)
        year1.resize(80, 30)

        year2.move(220, 430)
        year2.resize(80, 30)
        #done move & resize combo boxes

        #move & resize labels
        self.label1.move(100, 100)
        self.label1.resize(100, 50)
        self.label2.move(100, 200)
        self.label2.resize(100, 50)

        self.label3.move(150, 280)
        self.label3.resize(100, 50)
        self.label4.move(150, 380)
        self.label4.resize(100, 50)
        #done move & resize labels

        #resize window & centering
        self.resize(900, 600)
        self.center()

        #make 'compare' button to execute backend code
        self.btn = QtGui.QPushButton('Compare', self)
        self.btn.setToolTip('<b>compare stocks</b>')
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(150, 500)

        #make a call to the function calculate
        self.btn.clicked.connect(self.calculate)
        
        #make labels to display the images as pixmaps
        self.normalized_label = QtGui.QLabel(self)
        self.scatter_label = QtGui.QLabel(self)

        #move and resize labels (images)
        self.normalized_label.move(440, 50)
        self.normalized_label.resize(320, 240)
        self.scatter_label.move(440, 310)
        self.scatter_label.resize(320, 240)

        #set the scaled content of image in case resolutions don't match
        self.normalized_label.setScaledContents(True)
        self.scatter_label.setScaledContents(True)

        #give title
        self.setWindowTitle('The Elancer')


    def calculate(self):
        
        #get input data from various combo boxes
        start_day = int(self.day1.currentText())
        start_month = int(self.month1.currentText())
        start_year = int(self.year1.currentText())
        end_day = int(self.day2.currentText())
        end_month = int(self.month2.currentText())
        end_year = int(self.year2.currentText())

        #make list of companies to be compared
        list_companies = []
        company_1 = str(self.comp1.currentText())
        company_2 = str(self.comp2.currentText())
        list_companies.append(company_1)
        list_companies.append(company_2)

        #call the 'compare' function from the imported file 'comparison.py'
        comparison.compare(start_day, start_month, start_year, end_day, end_month, end_year, list_companies)

        #get pixmaps from saved files
        normalized_returns = QtGui.QPixmap('normalized_returns.jpg')
        scatter1v2 = QtGui.QPixmap('scatter1v2.jpg')

        #set the frames for labels & display pixmaps
        self.normalized_label.setFrameStyle(QtGui.QFrame.Panel)
        self.normalized_label.setPixmap(normalized_returns)
        self.scatter_label.setFrameStyle(QtGui.QFrame.Panel)
        self.scatter_label.setPixmap(scatter1v2)


    def center(self):
        
        #for centering of window
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
          
                
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
