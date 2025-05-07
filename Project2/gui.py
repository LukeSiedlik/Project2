from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QHBoxLayout
from controller import GradingController

class GradingView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.error_label = None
        self.submit_button = None
        self.scores_layout = None
        self.score_inputs = None
        self.score_labels = None
        self.attempts_input = None
        self.attempts_label = None
        self.name_input = None
        self.name_label = None
        self.setWindowTitle("Grading Window")
        self.setGeometry(100, 100, 400, 300)
        self.controller = GradingController(self)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        name_layout = QHBoxLayout()
        self.name_label = QLabel("Student name: ")
        self.name_input = QLineEdit(self)
        name_layout.addWidget(self.name_label)
        name_layout.addWidget(self.name_input)

        attempts_layout = QHBoxLayout()
        self.attempts_label = QLabel("No. of attempts: ")
        self.attempts_input = QLineEdit(self)
        self.attempts_input.textChanged.connect(self.update_score_inputs)
        attempts_layout.addWidget(self.attempts_label)
        attempts_layout.addWidget(self.attempts_input)

        self.score_labels = []
        self.score_inputs = []
        self.scores_layout = QVBoxLayout()
        for i in range(4):
            score_layout = QHBoxLayout()
            score_label = QLabel(f"Score {i + 1}:")
            score_input = QLineEdit(self)
            score_label.setVisible(False)
            score_input.setVisible(False)
            self.score_labels.append(score_label)
            self.score_inputs.append(score_input)
            score_layout.addWidget(score_label)
            score_layout.addWidget(score_input)
            self.scores_layout.addLayout(score_layout)

        self.submit_button = QPushButton("Submit", self)
        self.submit_button.clicked.connect(self.controller.submit_scores)

        self.error_label = QLabel("", self)

        layout.addLayout(name_layout)
        layout.addLayout(attempts_layout)
        layout.addLayout(self.scores_layout)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.error_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    #AI helped write this method, couldn't figure out how to make them only visible from certain inputs
    def update_score_inputs(self):
        attempts = self.attempts_input.text().strip()
        if attempts.isdigit():
            attempts = int(attempts)
            if 1 <= attempts <= 4:
                self.clear_score_inputs()  # Hide all first
                for i in range(attempts):
                    self.score_labels[i].setVisible(True)
                    self.score_inputs[i].setVisible(True)
                self.error_label.clear()
            else:
                self.show_error("Enter an attempt from 1-4")
                self.clear_score_inputs()
        else:
            self.clear_score_inputs()

    def clear_score_inputs(self):
        for label, input_box in zip(self.score_labels, self.score_inputs):
            label.setVisible(False)
            input_box.setVisible(False)
            input_box.clear()
        self.error_label.clear()

    def show_error(self, message):
        self.error_label.setText(message)
        self.error_label.setStyleSheet("color: red")

    def show_success(self, message):
        self.error_label.setText(message)
        self.error_label.setStyleSheet("color: green")
        self.clear_fields()

    def clear_fields(self):
        self.name_input.clear()
        self.attempts_input.clear()
        self.clear_score_inputs()
        self.error_label.clear()
