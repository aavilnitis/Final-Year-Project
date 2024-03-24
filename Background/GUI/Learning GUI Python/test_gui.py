import unittest
import tkinter as tk
from create_gui import create_gui

class TestGUI(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.gui = create_gui(self.root)
        
    def test_gui_exists(self):
        self.assertIsNotNone(self.gui)
        
    def test_gui_title(self):
        self.assertEqual(self.gui.title(), "Simple GUI")
        
    def test_label_exists(self):
        label = self.gui.children["hello_label"]
        self.assertIsNotNone(label)
        
    def test_button_exists(self):
        button = self.gui.children["button"]
        self.assertIsNotNone(button)

if __name__ == "__main__":
    unittest.main()