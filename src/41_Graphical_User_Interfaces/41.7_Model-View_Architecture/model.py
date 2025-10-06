from PySide6 import QtCore


class Model(QtCore.QAbstractListModel):
    def __init__(self, filename, parent=None):
        super().__init__(parent)
        self.dataset = []
        
        # Lade Datensatz
        with open(filename) as f:
            lst = []
            for line in f:
                if not line.strip():
                    self.dataset.append(lst)
                    lst = []
                else: 
                    lst.append(line.strip())
            if lst: 
                self.dataset.append(lst)

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.dataset)
        
    def data(self, index, role=QtCore.Qt.DisplayRole): 
        return self.dataset[index.row()]
        
    def flags(self, index):
        return QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        self.dataset[index.row()] = value
        self.layoutChanged.emit()
        return True

