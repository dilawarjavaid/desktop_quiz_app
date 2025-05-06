import json
import tkinter as tk
import requests
from tkinter import messagebox

#Define the QuizApp Class and Initialize UI
class QuizApp:
    def __init__(self, root):
        # Fetch Quiz Data from a Remote URL
        url = "https://raw.githubusercontent.com/arditsulceteaching/hosted_files/main/geo.json"
        response = requests.get(url)


