#!/usr/bin/env python3
"""
PyBricks Training Launcher

This script opens the PyBricks interactive training quiz in your default web browser.
Students will learn about Python, PyBricks, and robot programming through
visual presentations and interactive quizzes.
"""

import webbrowser
import os
import sys

def launch_training():
    """Launch the training quiz in the default web browser."""

    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Path to the quiz HTML file
    quiz_path = os.path.join(script_dir, 'quiz.html')

    # Check if the quiz file exists
    if not os.path.exists(quiz_path):
        print("Error: quiz.html not found!")
        print(f"Looking for: {quiz_path}")
        sys.exit(1)

    # Convert to file:// URL
    file_url = f'file://{quiz_path}'

    print("=" * 60)
    print("Radioactive Pybrix - Robotics Training")
    print("=" * 60)
    print("\nLaunching training quiz in your web browser...")
    print(f"Location: {quiz_path}")
    print("\nIf the browser doesn't open automatically,")
    print("you can manually open: quiz.html")
    print("=" * 60)

    # Open in default browser
    try:
        webbrowser.open(file_url)
        print("\nTraining quiz opened successfully!")
        print("You can close this window now.")
    except Exception as e:
        print(f"\nError opening browser: {e}")
        print(f"Please manually open: {quiz_path}")
        sys.exit(1)

if __name__ == "__main__":
    launch_training()
