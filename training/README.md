# Radioactive Pybrix - Robotics Training

An interactive training module for learning Python programming and PyBricks robotics!

## What's This?

This is an interactive learning experience designed for middle school students (grades 6-8) to learn:

- 🐍 **What Python is** - Understanding the programming language we use
- 🧱 **What PyBricks is** - How it helps control LEGO robots
- 📚 **Why libraries matter** - Why pre-written code saves time
- 🚀 **How to use PyBricks** - Practical examples and patterns

## Features

✨ **Visual Presentation** - 8 engaging slides with icons, code examples, and comparisons
✅ **Interactive Quiz** - 12 questions with immediate feedback
📊 **Score Tracking** - See how you're doing in real-time
🔍 **Answer Review** - Learn from mistakes with detailed explanations
📱 **Mobile Friendly** - Works on computers, tablets, and phones

## How to Use

### Option 1: Use the Launcher Script (Recommended)

```bash
python launch_training.py
```

This will automatically open the training quiz in your web browser!

### Option 2: Open Directly

Simply double-click `quiz.html` or open it in any web browser.

### Option 3: From Command Line

```bash
# macOS/Linux
open quiz.html

# Windows
start quiz.html
```

## Structure

The training follows this flow:

1. **Welcome Screen** - Introduction to what you'll learn
2. **Presentation** - 8 visual slides covering key concepts:
   - What is Python?
   - Why use Python?
   - What can Python do?
   - What is PyBricks?
   - What's a library?
   - Why use libraries?
   - How to use PyBricks
   - How we use it in our projects
3. **Interactive Quiz** - 12 questions testing your knowledge
4. **Results** - See your score and performance feedback
5. **Review** - Go through all questions with explanations

## Topics Covered

### 1. What is Python?

Learn that Python is a programming language designed to be easy to read and write, using human-friendly words instead of complicated syntax.

### 2. What is PyBricks?

Understand that PyBricks is a special Python library that makes controlling LEGO SPIKE Prime robots simple and fun.

### 3. Why Libraries?

Discover how libraries save time by providing pre-written code, just like using LEGO bricks instead of molding your own plastic!

### 4. How to Use It

See practical examples of how we use PyBricks in our robot missions, including:
- Driving the robot forward/backward
- Turning left/right
- Displaying messages
- Using the RobotController

## Quiz Details

- **12 Questions** covering all key concepts
- **Multiple Choice** format (4 options per question)
- **Immediate Feedback** after each answer
- **Detailed Explanations** for every question
- **Score Tracking** throughout the quiz
- **Review Mode** to learn from mistakes

### Grading

- 100% - Perfect! You're a PyBricks expert!
- 80-99% - Great job! Solid understanding
- 60-79% - Good effort! Keep learning
- Below 60% - Keep trying! Review and retake

## Files

- `quiz.html` - Main quiz interface
- `quiz.css` - Styling and visual design
- `quiz.js` - Quiz logic, slides, and questions
- `launch_training.py` - Python launcher script
- `README.md` - This file

## Technical Details

### Requirements

- Any modern web browser (Chrome, Firefox, Safari, Edge)
- No internet connection needed (runs completely offline)
- No special software or installations required

### Browser Compatibility

- ✅ Chrome/Edge (v90+)
- ✅ Firefox (v88+)
- ✅ Safari (v14+)
- ✅ Mobile browsers

### Features Used

- HTML5 semantic elements
- CSS3 animations and gradients
- Vanilla JavaScript (ES6+)
- Responsive design (mobile-friendly)

## For Educators

### Using in Class

1. **Pre-Lesson** - Have students complete before starting robot programming
2. **Post-Lesson** - Use as assessment after teaching concepts
3. **Homework** - Assign for review and practice
4. **Quick Check** - Use during class for knowledge checks

### Customization

To add more questions or modify content:

1. Open `quiz.js`
2. Add questions to the `quizQuestions` array
3. Follow the existing format:
   ```javascript
   {
       question: "Your question here?",
       answers: ["Option A", "Option B", "Option C", "Option D"],
       correctIndex: 0,  // Index of correct answer (0-3)
       explanation: "Why this is the correct answer..."
   }
   ```

To modify presentation slides:

1. Open `quiz.js`
2. Edit the `presentationSlides` array
3. Use HTML within the `content` field
4. Available CSS classes: `.highlight-box`, `.code-example`, `.comparison-grid`

## Troubleshooting

### Quiz won't open

- Make sure all files are in the same directory
- Try right-click → "Open With" → Your browser
- Check file permissions

### Styles look broken

- Ensure `quiz.css` is in the same directory as `quiz.html`
- Try clearing your browser cache
- Make sure you're opening `quiz.html`, not `quiz.js`

### Quiz not working

- Open browser console (F12) to see errors
- Make sure JavaScript is enabled
- Try a different browser

## License

This training material is part of the PyBricks Learning Project for middle school robotics education.

## Questions or Issues?

If you encounter any problems or have suggestions for improvement, please reach out to your instructor or mentor.

---

**Have fun learning!** 🚀🤖
