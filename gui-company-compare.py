import sys
from PyQt4 import QtGui, QtCore

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
        comp1 = QtGui.QComboBox(self)
        comp2 = QtGui.QComboBox(self)

        #combo box for start day, month, year
        day1 = QtGui.QComboBox(self)
        month1 = QtGui.QComboBox(self)
        year1 = QtGui.QComboBox(self)

        #combo box for end day, month, year
        day2 = QtGui.QComboBox(self)
        month2 = QtGui.QComboBox(self)
        year2 = QtGui.QComboBox(self)

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

        day1.move(100, 350)
        day1.resize(40, 30)

        day2.move(100, 450)
        day2.resize(40, 30)

        month1.move(160, 350)
        month1.resize(40, 30)

        month2.move(160, 450)
        month2.resize(40, 30)

        year1.move(220, 350)
        year1.resize(80, 30)

        year2.move(220, 450)
        year2.resize(80, 30)
        #done move & resize combo boxes

        #move & resize labels
        self.label1.move(100, 100)
        self.label1.resize(100, 50)
        self.label2.move(100, 200)
        self.label2.resize(100, 50)

        self.label3.move(150, 300)
        self.label3.resize(100, 50)
        self.label4.move(150, 400)
        self.label4.resize(100, 50)
        #done move & resize labels

        #resize window & centering
        self.resize(900, 600)
        self.center()

        #give title
        self.setWindowTitle('TheElancer')
        self.show()

    def center(self):
        
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
          
                
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
