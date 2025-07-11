from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QListWidget, QLabel, QMenuBar, QMenu, QDialog, QTextEdit
)
from PySide6.QtGui import QAction  # Import QAction from QtGui instead
from PySide6.QtCore import Qt
from themes import DARK_THEME, LIGHT_THEME

TOPICS = {
    "System": ["Btrfs", "Grep"],
    "Network": ["Rclone"],
    "Display": ["Nvidia"],
}

FUNCTIONS = {
    ("Display", "Nvidia"): ["nvidia-smi", "Driver Info", "GPU Usage"],
    ("System", "Btrfs"): ["btrfs send", "btrfs list"],
    # ... weitere Funktionen
}

class OutputDialog(QDialog):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Output")
        self.setMinimumSize(400, 200)
        layout = QVBoxLayout()
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.text_edit.setText(text)
        layout.addWidget(self.text_edit)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Linux Support Tool")
        self.setMinimumSize(900, 500)
        self.theme = "dark"
        self.setStyleSheet(DARK_THEME)

        # Menüleiste
        menu_bar = QMenuBar()
        menu = QMenu("Menu")
        theme_action = QAction("Switch Theme")
        theme_action.triggered.connect(self.toggle_theme)
        exit_action = QAction("Exit")
        exit_action.triggered.connect(self.close)
        menu.addAction(theme_action)
        menu.addAction(exit_action)
        about_menu = QMenu("About")
        about_action = QAction("About this app")
        about_action.triggered.connect(self.show_about)
        about_menu.addAction(about_action)
        menu_bar.addMenu(menu)
        menu_bar.addMenu(about_menu)
        self.setMenuBar(menu_bar)

        # Layouts
        main_widget = QWidget()
        main_layout = QHBoxLayout(main_widget)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(12)

        # col1: Topics
        self.topic_list = QListWidget()
        self.topic_list.addItems(TOPICS.keys())
        self.topic_list.currentItemChanged.connect(self.update_subtopics)
        self.topic_list.setFixedWidth(110)
        main_layout.addWidget(self.topic_list)

        # col2: Subtopics
        self.subtopic_list = QListWidget()
        self.subtopic_list.setFixedWidth(120)
        self.subtopic_list.currentItemChanged.connect(self.update_functions)
        main_layout.addWidget(self.subtopic_list)

        # col3: Main area (functions)
        self.function_area = QWidget()
        self.function_layout = QVBoxLayout(self.function_area)
        self.function_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        main_layout.addWidget(self.function_area)

        self.setCentralWidget(main_widget)

        # Initialauswahl
        self.topic_list.setCurrentRow(0)

    def update_subtopics(self):
        topic = self.topic_list.currentItem().text()
        self.subtopic_list.clear()
        self.subtopic_list.addItems(TOPICS[topic])
        self.subtopic_list.setCurrentRow(0)

    def update_functions(self):
        topic = self.topic_list.currentItem().text()
        subtopic = self.subtopic_list.currentItem().text()
        self.clear_function_area()
        functions = FUNCTIONS.get((topic, subtopic), [])
        for func in functions:
            btn = QPushButton(func)
            btn.clicked.connect(lambda _, f=func: self.show_output(f))
            btn.setMinimumHeight(40)
            self.function_layout.addWidget(btn)

    def clear_function_area(self):
        while self.function_layout.count():
            child = self.function_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def show_output(self, func_name):
        dlg = OutputDialog(f"Output for: {func_name}", self)
        dlg.exec()

    def toggle_theme(self):
        if self.theme == "dark":
            self.setStyleSheet(LIGHT_THEME)
            self.theme = "light"
        else:
            self.setStyleSheet(DARK_THEME)
            self.theme = "dark"

    def show_about(self):
        dlg = OutputDialog("Linux Support Tool\nFOSS\nGitHub: <your-link-here>", self)
        dlg.exec()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()