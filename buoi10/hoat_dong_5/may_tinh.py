import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QGridLayout, 
    QLineEdit, QPushButton
)
from PyQt5.QtCore import Qt

class MayTinhCoBan(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Máy tính bỏ túi - PyQt5")
        self.setFixedSize(300, 400)
        self.khoi_tao_giao_dien()

    def khoi_tao_giao_dien(self):
      
        self.hien_thi = QLineEdit()
        self.hien_thi.setFixedHeight(50)
        self.hien_thi.setAlignment(Qt.AlignRight)
        self.hien_thi.setReadOnly(True)
        self.hien_thi.setStyleSheet("font-size: 22px; padding: 5px;")

       
        grid_layout = QGridLayout()
        
       
        nut_bam = [
            ('C', 0, 0), ('(', 0, 1), (')', 0, 2), ('/', 0, 3),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('DEL', 4, 2), ('=', 4, 3),
        ]

       
        for text, row, col in nut_bam:
            nut = QPushButton(text)
            nut.setFixedHeight(50)
            nut.setStyleSheet("font-size: 16px; font-weight: bold;")
            nut.clicked.connect(self.xu_ly_nut_bam)
            grid_layout.addWidget(nut, row, col)

     
        layout_chinh = QVBoxLayout()
        layout_chinh.addWidget(self.hien_thi)
        layout_chinh.addLayout(grid_layout)

        self.setLayout(layout_chinh)

    def xu_ly_nut_bam(self):
        nut = self.sender()
        gia_tri = nut.text()
        bieu_thuc_hien_tai = self.hien_thi.text()

        if gia_tri == 'C':
           
            self.hien_thi.clear()

        elif gia_tri == 'DEL':
           
            self.hien_thi.setText(bieu_thuc_hien_tai[:-1])

        elif gia_tri == '=':
          
            try:

                ket_qua = eval(bieu_thuc_hien_tai)
                self.hien_thi.setText(str(ket_qua))
            except Exception:
                self.hien_thi.setText("Lỗi")

        else:
            
            if bieu_thuc_hien_tai == "Lỗi":
                bieu_thuc_hien_tai = ""
           
            self.hien_thi.setText(bieu_thuc_hien_tai + gia_tri)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cua_so = MayTinhCoBan()
    cua_so.show()
    sys.exit(app.exec_())