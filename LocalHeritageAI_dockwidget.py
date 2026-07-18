# -*- coding: utf-8 -*-
import os
import requests
import json
import speech_recognition as sr
from qgis.PyQt import QtWidgets, uic
from qgis.PyQt.QtCore import pyqtSignal

# Load your UI file
FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'LocalHeritageAI_dockwidget_base.ui'))

class LocalHeritageAIDockWidget(QtWidgets.QDockWidget, FORM_CLASS):
    closingPlugin = pyqtSignal()

    def __init__(self, parent=None):
        super(LocalHeritageAIDockWidget, self).__init__(parent)
        self.setupUi(self)
        
        # Connect buttons
        self.btn_upload.clicked.connect(self.upload_audio)
        self.btn_geolocate.clicked.connect(self.run_geolocate)
        self.btn_classify.clicked.connect(self.run_classify)
        self.btn_analyze.clicked.connect(self.run_analyze)

    def upload_audio(self):
        # File selector
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select Audio", "", "Audio Files (*.wav)")
        if filename:
            self.txt_output.append("Transcribing... please wait.")
            recognizer = sr.Recognizer()
            with sr.AudioFile(filename) as source:
                audio = recognizer.record(source)
                text = recognizer.recognize_google(audio)
                self.txt_input.setPlainText(text)
                self.txt_output.append("Transcription complete.")

    def query_local_ollama(self, prompt_text):
        url = "http://localhost:11434/api/generate"
        payload = {"model": "qwen2.5", "prompt": prompt_text, "stream": False}
        try:
            response = requests.post(url, json=payload)
            return response.json()['response'] if response.status_code == 200 else "AI Error"
        except:
            return "Ollama is not running!"

    def run_geolocate(self):
        text = self.txt_input.toPlainText()
        result = self.query_local_ollama("Extract only location names from: " + text)
        self.txt_output.setText(result)

    def run_classify(self):
        text = self.txt_input.toPlainText()
        result = self.query_local_ollama("Categorize into [Flood, Social, Infrastructure]: " + text)
        self.txt_output.setText(result)

    def run_analyze(self):
        text = self.txt_input.toPlainText()
        result = self.query_local_ollama("Provide climate insights: " + text)
        self.txt_output.setText(result)

    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()