DARK_THEME = '''
QMainWindow {
    background: #23272e;
    border-radius: 18px;
}
QMenuBar, QMenu {
    background: #23272e;
    color: #e0e6f0;
    border-radius: 8px;
}
QListWidget {
    background: #2c313a;
    color: #e0e6f0;
    border-radius: 12px;
}
QPushButton {
    background: #283347;
    color: #e0e6f0;
    border-radius: 10px;
    min-width: 120px;
    min-height: 36px;
    margin: 6px;
}
QPushButton:hover {
    background: #3a4a6d;
}
QTextEdit {
    background: #23272e;
    color: #e0e6f0;
    border-radius: 12px;
}
QListWidget, QListView {
    background: #2c313a;  /* oder #e8eaf0 für Light */
    color: #e0e6f0;       /* oder #222 für Light */
    border-radius: 12px;
    padding: 6px;
    border: none;
}
QListWidget::item:selected, QListView::item:selected {
    background: #3a4a6d;  /* oder #bcd4ff für Light */
    color: #fff;
    border-radius: 8px;
}
'''

LIGHT_THEME = '''
QMainWindow {
    background: #f5f7fa;
    border-radius: 18px;
}
QMenuBar, QMenu {
    background: #e0e6f0;
    color: #222;
    border-radius: 8px;
}
QListWidget {
    background: #e8eaf0;
    color: #222;
    border-radius: 12px;
}
QPushButton {
    background: #e0eaff;
    color: #222;
    border-radius: 10px;
    min-width: 120px;
    min-height: 36px;
    margin: 6px;
}
QPushButton:hover {
    background: #bcd4ff;
}
QTextEdit {
    background: #f5f7fa;
    color: #222;
    border-radius: 12px;
}
QListWidget, QListView {
    background: #2c313a;  /* oder #e8eaf0 für Light */
    color: #e0e6f0;       /* oder #222 für Light */
    border-radius: 12px;
    padding: 6px;
    border: none;
}
QListWidget::item:selected, QListView::item:selected {
    background: #3a4a6d;  /* oder #bcd4ff für Light */
    color: #fff;
    border-radius: 8px;
}
'''