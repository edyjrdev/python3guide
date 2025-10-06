from PySide6 import QtWidgets, QtGui, QtCore


class ViewDelegate(QtWidgets.QItemDelegate):
    def __init__(self, parent=None): 
        super().__init__(parent) 
        self.frame_pen = QtGui.QPen(QtGui.QColor(0, 0, 0))
        self.title_text_pen = QtGui.QPen(QtGui.QColor(255, 255, 255))
        self.title_color = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        self.text_pen = QtGui.QPen(QtGui.QColor(0, 0, 0))
        self.title_color_active = QtGui.QBrush(QtGui.QColor(0, 0, 120))
        self.background_color_active = QtGui.QBrush(QtGui.QColor(230, 230, 255))
        self.title_font = QtGui.QFont("Helvetica", 10, QtGui.QFont.Bold)
        self.text_font = QtGui.QFont("Helvetica", 10)
        self.row_height = 15
        self.title_height = 20
        self.outer_padding = 4
        self.inner_padding = 2
        self.text_padding = 4
        
    def sizeHint(self, option, index):
        num = len(index.data())
        return QtCore.QSize(170, self.row_height * num + self.title_height)

    def paint(self, painter, option, index):
        frame = option.rect.adjusted(self.outer_padding, self.outer_padding, -self.outer_padding, -self.outer_padding)
        frame_title = frame.adjusted(self.inner_padding, self.inner_padding, -self.inner_padding + 1, 0)
        frame_title.setHeight(self.title_height)
        frame_title_text = frame_title.adjusted(self.text_padding, 0, self.text_padding, 0)
        data = index.data()
        
        painter.save()
        if option.state & QtWidgets.QStyle.State_Selected:
            painter.fillRect(frame, self.background_color_active)
            painter.fillRect(frame_title, self.title_color_active)
        else:
            painter.fillRect(frame_title, self.title_color)
        painter.setPen(self.frame_pen)
        painter.drawRect(frame)
        
        # Paint title
        painter.setPen(self.title_text_pen)
        painter.setFont(self.title_font)
        painter.drawText(frame_title_text, QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter, data[0])
                    
        # Paint address
        painter.setPen(self.text_pen)
        painter.setFont(self.text_font)
        for i, entry in enumerate(data[1:]):
            painter.drawText(frame_title.x() + self.text_padding, frame_title.bottom() + (i + 1) * self.row_height, entry)
        painter.restore()
        
    def createEditor(self, parent, option, index):
        return QtWidgets.QTextEdit(parent)
            
    def setEditorData(self, editor, index):
        editor.setPlainText("\n".join(index.data()))

    def updateEditorGeometry(self, editor, option, index):
        frame = option.rect.adjusted(self.outer_padding, self.outer_padding, -self.outer_padding, -self.outer_padding)
        editor.setGeometry(frame)
            
    def setModelData(self, editor, model, index):
        model.setData(index, editor.toPlainText().split("\n"))
            
    def eventFilter(self, editor, event):
        if event.type() == QtCore.QEvent.KeyPress and event.key() in (QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter):
            return False
        return QtWidgets.QItemDelegate.eventFilter(self, editor, event)


class View(QtWidgets.QListView):
   def __init__(self, model, parent=None):
       super().__init__(parent) 
       self.delegate = ViewDelegate()
       self.setItemDelegate(self.delegate) 
       self.setModel(model)
       self.setVerticalScrollMode(QtWidgets.QListView.ScrollPerPixel)
