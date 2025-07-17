from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QListWidget, QDialog, QTextEdit, QLabel, QGridLayout
)
from PySide6.QtGui import QAction, QFont, QFontInfo
from PySide6.QtCore import Qt, Signal
from themes import THEMES
from variables import TOPICS, FUNCTIONS
import functions


class OutputDialog(QDialog):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Output")
        self.resize(900, 700)
        self.setMinimumSize(300, 200)
        layout = QVBoxLayout()
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.text_edit.setText(text)

        for family in ["DejaVu Sans Mono", "Liberation Mono", "Courier New", "Monospace"]:
            font = QFont(family)
            font.setStyleHint(QFont.Monospace)
            if QFontInfo(font).fixedPitch():
                break
        font.setPointSize(11)
        self.text_edit.setFont(font)

        layout.addWidget(self.text_edit)
        self.setLayout(layout)


class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("About")
        self.setMinimumSize(400, 200)
        layout = QVBoxLayout()
        label = QLabel("Linux Functionality (LinFunct)\n\nGitHub: https://github.com/df8819/LinFunct")
        label.setWordWrap(True)
        label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        layout.addWidget(label)
        ok_btn = QPushButton("OK")
        ok_btn.clicked.connect(self.accept)
        layout.addWidget(ok_btn, alignment=Qt.AlignRight)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    output_ready = Signal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Linux Support Tool")
        self.setMinimumSize(900, 500)
        self.theme = "dark"
        self.setStyleSheet(THEMES["Earthern Tone"])
        self.output_ready.connect(self.show_output)

        # Menüleiste
        menu_bar = self.menuBar()
        menu = menu_bar.addMenu("File")
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        menu.addAction(exit_action)

        # Theme-Menü als Untermenü
        theme_menu = menu_bar.addMenu("Theme")
        for name in THEMES:
            action = QAction(name, self)
            action.triggered.connect(lambda checked, n=name: self.set_theme(n))
            theme_menu.addAction(action)

        about_menu = menu_bar.addMenu("About")
        about_action = QAction("About LinFunct...", self)
        about_action.triggered.connect(self.show_about)
        about_menu.addAction(about_action)

        # Layouts
        main_widget = QWidget()
        outer_layout = QVBoxLayout(main_widget)
        outer_layout.setContentsMargins(10, 10, 10, 10)
        outer_layout.setSpacing(6)

        # Header mit drei Labels in einer Zeile, jeweils in eigenem Container
        header_layout = QHBoxLayout()
        header_layout.setSpacing(12)

        # col1-Label
        col1_label = QLabel("1. Category")
        col1_label.setObjectName("headerLabel")
        col1_label.setAlignment(Qt.AlignCenter)
        col1_label.setStyleSheet("font-weight: bold; font-size: 15px; margin-bottom: 6px; margin-top: 6px;")
        col1_label_container = QWidget()
        col1_label_container.setObjectName("headerLabelContainer")
        col1_label_container.setFixedWidth(110)
        col1_label_layout = QVBoxLayout(col1_label_container)
        col1_label_layout.setContentsMargins(0, 0, 0, 0)
        col1_label_layout.addWidget(col1_label)
        header_layout.addWidget(col1_label_container)

        # col2-Label
        col2_label = QLabel("2. Topic")
        col2_label.setObjectName("headerLabel")
        col2_label.setAlignment(Qt.AlignCenter)
        col2_label.setStyleSheet("font-weight: bold; font-size: 15px; margin-bottom: 6px; margin-top: 6px;")
        col2_label_container = QWidget()
        col2_label_container.setObjectName("headerLabelContainer")
        col2_label_container.setFixedWidth(120)
        col2_label_layout = QVBoxLayout(col2_label_container)
        col2_label_layout.setContentsMargins(0, 0, 0, 0)
        col2_label_layout.addWidget(col2_label)
        header_layout.addWidget(col2_label_container)

        # col3-Label
        col3_label = QLabel("3. Command")
        col3_label.setObjectName("headerLabel")
        col3_label.setAlignment(Qt.AlignCenter)
        col3_label.setStyleSheet("font-weight: bold; font-size: 15px; margin-bottom: 6px; margin-top: 6px;")
        col3_label_container = QWidget()
        col3_label_container.setObjectName("headerLabelContainer")
        col3_label_layout = QVBoxLayout(col3_label_container)
        col3_label_layout.setContentsMargins(0, 0, 0, 0)
        col3_label_layout.addWidget(col3_label)
        header_layout.addWidget(col3_label_container, stretch=1)

        outer_layout.addLayout(header_layout)

        # Spalten-Layout darunter
        main_layout = QHBoxLayout()
        main_layout.setSpacing(12)

        # col1: Category
        self.topic_list = QListWidget()
        self.topic_list.setStyleSheet("QListWidget::item { min-height: 18px; padding: 8px 4px; }")
        self.topic_list.addItems(TOPICS.keys())
        self.topic_list.currentItemChanged.connect(self.update_subtopics)
        self.topic_list.setFixedWidth(110)
        main_layout.addWidget(self.topic_list)

        # col2: Topic
        self.subtopic_list = QListWidget()
        self.subtopic_list.setStyleSheet("QListWidget::item { min-height: 18px; padding: 8px 4px; }")
        self.subtopic_list.setFixedWidth(120)
        self.subtopic_list.currentItemChanged.connect(self.update_functions)
        main_layout.addWidget(self.subtopic_list)

        # col3: Command
        self.function_area = QWidget()
        self.function_layout = QGridLayout(self.function_area)
        self.function_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.function_columns = 4  # <---  Spaltenanzahl
        main_layout.addWidget(self.function_area, stretch=1)

        outer_layout.addLayout(main_layout)

        self.setCentralWidget(main_widget)

        # Initialauswahl
        self.topic_list.setCurrentRow(0)

    def run_function(self, func_name):
        func = getattr(functions, func_name, None)
        if func:
            func(self.output_ready.emit)
        else:
            self.show_output(f"Function '{func_name}' not implemented.")

    def show_output(self, text):
        dlg = OutputDialog(text, self)
        dlg.exec()

    def update_subtopics(self):
        topic = self.topic_list.currentItem().text()
        self.subtopic_list.clear()
        self.subtopic_list.addItems(TOPICS[topic])
        self.subtopic_list.setCurrentRow(0)

    def update_functions(self):
        topic = self.topic_list.currentItem().text()
        subtopic = self.subtopic_list.currentItem().text()
        self.clear_function_area()
        functions_list = FUNCTIONS.get((topic, subtopic), [])
        columns = self.function_columns  # Anzahl Spalten
        for idx, func in enumerate(functions_list):
            btn = QPushButton(func["label"])
            btn.clicked.connect(lambda _, f=func["function"]: self.run_function(f))
            btn.setMinimumHeight(40)
            row = idx // columns
            col = idx % columns
            self.function_layout.addWidget(btn, row, col)

    def clear_function_area(self):
        while self.function_layout.count():
            child = self.function_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def set_theme(self, theme_name):
        self.setStyleSheet(THEMES[theme_name])
        self.theme = theme_name.lower()

    def show_about(self):
        dlg = AboutDialog(self)
        dlg.exec()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()