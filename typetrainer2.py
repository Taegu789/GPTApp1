import random
import sys
from PyQt5.QtWidgets import *
import time
from PyQt5.QtCore import Qt, QTimer


class TypingTrainer(QWidget):
    def __init__(self):
        super().__init__()

        # Create widgets
        self.word_label = QLabel()
        self.word_label.setAlignment(Qt.AlignCenter)
        self.input_field = QLineEdit()
        self.input_field.setMaxLength(10)
        self.input_field.returnPressed.connect(self.check_input)
        self.start_button = QPushButton('Start')
        self.start_button.clicked.connect(self.start_game)

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.word_label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.start_button)
        self.setLayout(layout)

        # Create timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_word)

    def get_word():
        words = ['cat', 'dog', 'bird', 'fish','Give me One dollar!']
        return random.choice(words)

    def update_word(self):
        self.word = self.get_word()
        self.word_label.setText(self.word)

    def start_game(self):
        self.start_time = time.time()
        self.input_field.setFocus()
        self.update_word()
        self.timer.start(3000)
    
    def check_input(self):
        user_input = self.input_field.text()
        if user_input == self.word:
            print('Correct!')
            elapsed_time = time.time() - self.start_time
            print('Elapsed time: %.2f seconds' % elapsed_time)
            self.timer.stop()
            self.input_field.clear()
        else:
            print('Incorrect!')
            self.input_field.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    trainer = TypingTrainer()
    trainer.show()
    sys.exit(app.exec_())
