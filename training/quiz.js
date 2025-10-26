// Presentation Slides
const presentationSlides = [
    {
        title: "What is Python?",
        icon: "🐍",
        content: `
            <div class="slide-content">
                <div class="highlight-box">
                    <h3>Python is a <strong>programming language</strong> that talks like you do!</h3>
                </div>
                <p>Instead of complicated codes, Python uses words you already know:</p>
                <div class="code-example">
<span style="color: #dcdcaa;">print</span>(<span style="color: #ce9178;">"Hello, Robot!"</span>)
<span style="color: #c586c0;">if</span> temperature > <span style="color: #b5cea8;">100</span>:
    turn_on_fan()
                </div>
                <p><strong>It's designed to be easy to read and write</strong></p>
            </div>
        `
    },
    {
        title: "Why Use Python?",
        icon: "✨",
        content: `
            <div class="slide-content">
                <div class="comparison-grid">
                    <div class="comparison-card good">
                        <h3>✓ Python</h3>
                        <div class="code-example" style="font-size: 0.9em;">
<span style="color: #dcdcaa;">print</span>(<span style="color: #ce9178;">"Hello!"</span>)

<span style="color: #c586c0;">for</span> i <span style="color: #c586c0;">in</span> <span style="color: #dcdcaa;">range</span>(<span style="color: #b5cea8;">5</span>):
    motor.run(<span style="color: #b5cea8;">100</span>)
                        </div>
                        <p>Easy to read!</p>
                    </div>
                    <div class="comparison-card bad">
                        <h3>✗ Other Languages</h3>
                        <div class="code-example" style="font-size: 0.9em;">
printf(<span style="color: #ce9178;">"Hello!"</span>);

<span style="color: #c586c0;">for</span>(<span style="color: #c586c0;">int</span> i=<span style="color: #b5cea8;">0</span>;i<<span style="color: #b5cea8;">5</span>;i++){
  motor.run(<span style="color: #b5cea8;">100</span>);
}
                        </div>
                        <p>More confusing!</p>
                    </div>
                </div>
                <p><strong>Python lets you focus on solving problems, not memorizing syntax!</strong></p>
            </div>
        `
    },
    {
        title: "Python vs Block Programming",
        icon: "⚔️",
        content: `
            <div class="slide-content">
                <h3>Why Python instead of LEGO's block programming?</h3>
                <div style="text-align: left; max-width: 600px; margin: 30px auto;">
                    <div class="highlight-box" style="margin: 15px 0; background: #e8f5e9; border-left: 5px solid #4caf50;">
                        <strong>📝 Source Control (Git)</strong>
                        <p style="margin-top: 10px;">Track changes, work as a team, never lose code! Just like professional developers.</p>
                    </div>
                    <div class="highlight-box" style="margin: 15px 0; background: #e3f2fd; border-left: 5px solid #2196f3;">
                        <strong>🔍 Easy to Read & Review</strong>
                        <p style="margin-top: 10px;">See all your code at once. No scrolling through blocks!</p>
                    </div>
                    <div class="highlight-box" style="margin: 15px 0; background: #f3e5f5; border-left: 5px solid #9c27b0;">
                        <strong>💾 Save & Share</strong>
                        <p style="margin-top: 10px;">Copy, paste, backup easily. Text files work everywhere!</p>
                    </div>
                    <div class="highlight-box" style="margin: 15px 0; background: #fff3e0; border-left: 5px solid #ff9800;">
                        <strong>🚀 Professional Skills</strong>
                        <p style="margin-top: 10px;">Learn real programming used in jobs & college!</p>
                    </div>
                    <div class="highlight-box" style="margin: 15px 0; background: #fce4ec; border-left: 5px solid #e91e63;">
                        <strong>⚡ More Powerful</strong>
                        <p style="margin-top: 10px;">Do complex logic, math, and algorithms easily!</p>
                    </div>
                </div>
            </div>
        `
    },
    {
        title: "What Can Python Do?",
        icon: "🎯",
        content: `
            <div class="slide-content">
                <h3>Python is like a Swiss Army knife - it does EVERYTHING!</h3>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin: 30px 0; text-align: left;">
                    <div>🌐 Build websites (Instagram, YouTube)</div>
                    <div>🎮 Create games</div>
                    <div>🤖 Control robots (that's us!)</div>
                    <div>📊 Analyze data</div>
                    <div>🧠 Power AI & machine learning</div>
                    <div>📱 Make mobile apps</div>
                </div>
                <div class="highlight-box">
                    <p><strong>In this class, we use Python to control LEGO robots!</strong></p>
                </div>
            </div>
        `
    },
    {
        title: "What is PyBricks?",
        icon: "🧱",
        content: `
            <div class="slide-content">
                <div class="highlight-box">
                    <h3>PyBricks = <span style="color: #667eea;">Python</span> + <span style="color: #764ba2;">LEGO Bricks</span></h3>
                </div>
                <p style="font-size: 1.3em; margin: 30px 0;">It's a <strong>library</strong> (toolkit) that makes controlling LEGO robots super easy!</p>
                <div class="code-example">
<span style="color: #6a9955;"># Control your SPIKE Prime robot with simple commands:</span>

<span style="color: #6a9955;"># Drive forward</span>
robot.drivebase.straight(<span style="color: #b5cea8;">500</span>)

<span style="color: #6a9955;"># Turn right</span>
robot.drivebase.turn(<span style="color: #b5cea8;">90</span>)

<span style="color: #6a9955;"># Show message</span>
robot.hub.display.text(<span style="color: #ce9178;">"Hi!"</span>)
                </div>
            </div>
        `
    },
    {
        title: "What's a Library?",
        icon: "📚",
        content: `
            <div class="slide-content">
                <h3>Think of it like LEGO blocks...</h3>
                <div class="comparison-grid" style="margin: 30px 0;">
                    <div class="comparison-card bad">
                        <h3>❌ Without a Library</h3>
                        <p>Mold your own plastic</p>
                        <p>Create every piece from scratch</p>
                        <p>Takes forever!</p>
                    </div>
                    <div class="comparison-card good">
                        <h3>✅ With a Library</h3>
                        <p>Use pre-made LEGO bricks</p>
                        <p>Snap them together</p>
                        <p>Build amazing things fast!</p>
                    </div>
                </div>
                <div class="highlight-box">
                    <p><strong>A library = Pre-written code you can use in your programs!</strong></p>
                </div>
            </div>
        `
    },
    {
        title: "Why Use PyBricks Library?",
        icon: "⚡",
        content: `
            <div class="slide-content">
                <h3>Without PyBricks: 😰</h3>
                <div class="code-example" style="font-size: 0.85em;">
<span style="color: #6a9955;"># Hundreds of lines of complicated code to control a motor:</span>
calculate_voltage_signals()
manage_motor_timing()
sync_multiple_motors()
handle_acceleration_curves()
monitor_position_feedback()
<span style="color: #6a9955;"># ... and much more!</span>
                </div>
                <h3 style="margin-top: 30px;">With PyBricks: 😎</h3>
                <div class="code-example" style="font-size: 1em;">
<span style="color: #6a9955;"># That's it!</span>
motor.run(500)
                </div>
            </div>
        `
    },
    {
        title: "How to Use PyBricks",
        icon: "🚀",
        content: `
            <div class="slide-content">
                <h3>Three Simple Steps:</h3>
                <div style="text-align: left; max-width: 500px; margin: 30px auto;">
                    <div class="highlight-box">
                        <h4>1️⃣ Import what you need</h4>
                        <div class="code-example" style="margin-top: 10px;">
<span style="color: #c586c0;">from</span> pybricks.hubs <span style="color: #c586c0;">import</span> PrimeHub
                        </div>
                    </div>
                    <div class="highlight-box">
                        <h4>2️⃣ Create objects</h4>
                        <div class="code-example" style="margin-top: 10px;">
hub = PrimeHub()
                        </div>
                    </div>
                    <div class="highlight-box">
                        <h4>3️⃣ Use them!</h4>
                        <div class="code-example" style="margin-top: 10px;">
hub.display.text(<span style="color: #ce9178;">"Hello!"</span>)
                        </div>
                    </div>
                </div>
            </div>
        `
    },
    {
        title: "In Our Robot Projects...",
        icon: "🎓",
        content: `
            <div class="slide-content">
                <div class="highlight-box">
                    <h3>Good news! We made it even easier!</h3>
                </div>
                <p style="margin: 20px 0;">The <strong>RobotController</strong> does all the setup for you:</p>
                <div class="code-example">
<span style="color: #c586c0;">def</span> <span style="color: #dcdcaa;">run</span>(robot: RobotController, display):
    <span style="color: #6a9955;"># Everything is ready to use!</span>

    <span style="color: #6a9955;"># Drive forward</span>
    robot.drivebase.straight(<span style="color: #b5cea8;">500</span>)

    <span style="color: #6a9955;"># Turn right</span>
    robot.drivebase.turn(<span style="color: #b5cea8;">90</span>)

    <span style="color: #6a9955;"># Count down</span>
    display.show_countdown(<span style="color: #b5cea8;">3</span>)
                </div>
                <div class="highlight-box" style="margin-top: 20px;">
                    <p>✅ Robot already initialized<br>
                    ✅ Motors already configured<br>
                    ✅ Just write your mission logic!</p>
                </div>
            </div>
        `
    },
    {
        title: "Our Project Setup System",
        icon: "🏗️",
        content: `
            <div class="slide-content">
                <div class="highlight-box">
                    <h3>We built automated scripts that do the hard work for you!</h3>
                </div>
                <div style="margin: 30px 0; text-align: left; max-width: 500px; margin: 30px auto;">
                    <div style="background: #e8f5e9; padding: 20px; border-radius: 10px; margin: 15px 0; border-left: 5px solid #4caf50;">
                        <strong>1️⃣ Create Season</strong><br>
                        <code>python new_season.py</code>
                    </div>
                    <div style="background: #e3f2fd; padding: 20px; border-radius: 10px; margin: 15px 0; border-left: 5px solid #2196f3;">
                        <strong>2️⃣ Add Missions</strong><br>
                        <code>python new_mission.py</code>
                    </div>
                    <div style="background: #fff3e0; padding: 20px; border-radius: 10px; margin: 15px 0; border-left: 5px solid #ff9800;">
                        <strong>3️⃣ Write & Run</strong><br>
                        Code → Upload → Test!
                    </div>
                </div>
                <p><strong>No manual configuration. No errors. Just robot fun!</strong></p>
            </div>
        `
    },
    {
        title: "Step 1: Create Your Season",
        icon: "🎬",
        content: `
            <div class="slide-content">
                <div class="code-example">
<span style="color: #4ec9b0;">python</span> new_season.py
                </div>
                <h3 style="margin: 30px 0 20px 0;">The script asks you simple questions:</h3>
                <div style="text-align: left; max-width: 550px; margin: 0 auto;">
                    <div style="padding: 10px; margin: 8px 0;">❓ What's your season name?</div>
                    <div style="padding: 10px; margin: 8px 0;">❓ What's your team name?</div>
                    <div style="padding: 10px; margin: 8px 0;">🔌 Which ports are your motors plugged into?</div>
                    <div style="padding: 10px; margin: 8px 0;">📏 What size are your wheels?</div>
                    <div style="padding: 10px; margin: 8px 0;">📐 How far apart are your wheels?</div>
                </div>
                <div class="highlight-box" style="margin-top: 25px;">
                    <p><strong>Then it creates a complete season folder, perfectly configured for YOUR robot!</strong></p>
                </div>
            </div>
        `
    },
    {
        title: "What's in Your Season Folder?",
        icon: "📂",
        content: `
            <div class="slide-content">
                <h3>Everything you need, automatically generated:</h3>
                <div class="comparison-grid" style="margin: 25px 0;">
                    <div style="background: #f5f5f5; padding: 20px; border-radius: 10px; border: 2px solid #667eea;">
                        <div style="font-size: 2em;">⚙️</div>
                        <strong>season_config.py</strong>
                        <p style="margin-top: 10px; font-size: 0.9em;">Your robot's specs:<br>ports, wheel size, speeds</p>
                    </div>
                    <div style="background: #f5f5f5; padding: 20px; border-radius: 10px; border: 2px solid #667eea;">
                        <div style="font-size: 2em;">📋</div>
                        <strong>season_menu.py</strong>
                        <p style="margin-top: 10px; font-size: 0.9em;">Mission selector<br>(auto-updated!)</p>
                    </div>
                    <div style="background: #f5f5f5; padding: 20px; border-radius: 10px; border: 2px solid #667eea;">
                        <div style="font-size: 2em;">🤖</div>
                        <strong>robot_controller.py</strong>
                        <p style="margin-top: 10px; font-size: 0.9em;">Robot brain<br>(handles all setup)</p>
                    </div>
                    <div style="background: #f5f5f5; padding: 20px; border-radius: 10px; border: 2px solid #667eea;">
                        <div style="font-size: 2em;">🛠️</div>
                        <strong>Utilities</strong>
                        <p style="margin-top: 10px; font-size: 0.9em;">Helper tools for<br>displays, line following, etc.</p>
                    </div>
                </div>
            </div>
        `
    },
    {
        title: "Step 2: Add Missions",
        icon: "🎯",
        content: `
            <div class="slide-content">
                <div class="highlight-box">
                    <h3>Run from INSIDE your season folder:</h3>
                </div>
                <div class="code-example">
<span style="color: #4ec9b0;">cd</span> my_season
<span style="color: #4ec9b0;">python</span> ../new_mission.py
                </div>
                <h3 style="margin: 30px 0 20px 0;">What it does:</h3>
                <div style="text-align: left; max-width: 550px; margin: 0 auto;">
                    <div style="background: #e8f5e9; padding: 15px; margin: 10px 0; border-radius: 8px;">
                        ✅ Asks for mission name & description
                    </div>
                    <div style="background: #e8f5e9; padding: 15px; margin: 10px 0; border-radius: 8px;">
                        ✅ Asks for speed settings (slow, medium, fast)
                    </div>
                    <div style="background: #e8f5e9; padding: 15px; margin: 10px 0; border-radius: 8px;">
                        ✅ Lets you choose Simple or Guided template
                    </div>
                    <div style="background: #e8f5e9; padding: 15px; margin: 10px 0; border-radius: 8px;">
                        ✅ Creates mission file with helpful examples
                    </div>
                    <div style="background: #fff3cd; padding: 15px; margin: 10px 0; border-radius: 8px; border: 2px solid #ffc107;">
                        <strong>✨ Automatically updates season_menu.py!</strong>
                    </div>
                </div>
            </div>
        `
    },
    {
        title: "Step 3: Write Your Mission Code",
        icon: "✍️",
        content: `
            <div class="slide-content">
                <h3>Edit your mission file - it has helpful examples!</h3>
                <div class="highlight-box" style="margin-bottom: 20px;">
                    <p><strong>Simple template:</strong> Quick-start examples at the top<br>
                    <strong>Guided template:</strong> Quick-start + detailed examples by category</p>
                </div>
                <div class="code-example" style="text-align: left;">
<span style="color: #c586c0;">def</span> <span style="color: #dcdcaa;">run</span>(robot: RobotController, display):
    <span style="color: #ce9178;">"""Your mission code goes here!"""</span>

    <span style="color: #6a9955;"># Uncomment examples from the template:</span>
    <span style="color: #6a9955;"># Drive forward</span>
    <span style="color: #6a9955;"># robot.drivebase.straight(500)</span>

    <span style="color: #6a9955;"># Turn right</span>
    <span style="color: #6a9955;"># robot.drivebase.turn(90)</span>

    <span style="color: #6a9955;"># Count down</span>
    <span style="color: #6a9955;"># display.show_countdown(3)</span>

    <span style="color: #6a9955;"># Write your own mission logic!</span>
    robot.drivebase.straight(<span style="color: #b5cea8;">300</span>)
    robot.drivebase.turn(<span style="color: #b5cea8;">90</span>)
    robot.drivebase.straight(<span style="color: #b5cea8;">300</span>)
                </div>
                <div class="highlight-box" style="margin-top: 20px;">
                    <p>The template has tons of examples in comments - just uncomment and modify!</p>
                </div>
            </div>
        `
    },
    {
        title: "Step 4: Upload and Run!",
        icon: "🚀",
        content: `
            <div class="slide-content">
                <h3>Almost there!</h3>
                <div style="text-align: left; max-width: 500px; margin: 30px auto;">
                    <div class="highlight-box">
                        <h4>1️⃣ Upload season_menu.py to hub</h4>
                        <p style="margin-top: 10px;">✨ PyBricks automatically uploads all the other files it needs through imports!</p>
                        <p style="margin-top: 5px; font-size: 0.9em; opacity: 0.8;">All files must be in the same folder (flat structure)</p>
                    </div>
                    <div class="highlight-box">
                        <h4>2️⃣ Run the program on the hub</h4>
                        <p style="margin-top: 10px;">When you run season_menu.py, it shows your mission selector</p>
                    </div>
                    <div class="highlight-box">
                        <h4>3️⃣ Use hub buttons to pick your mission</h4>
                        <p style="margin-top: 10px;">← → to navigate, Center button to select and run</p>
                    </div>
                </div>
                <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 20px; border-radius: 15px; margin-top: 25px;">
                    <strong style="font-size: 1.3em;">🎉 Your robot runs your mission!</strong>
                </div>
            </div>
        `
    }
];

// Quiz Questions Database
const quizQuestions = [
    // Section 1: What is Python?
    {
        question: "What is Python?",
        answers: [
            "A type of snake that lives in computers",
            "A programming language that uses human-readable words",
            "A game for building robots",
            "A special type of LEGO brick"
        ],
        correctIndex: 1,
        explanation: "Python is a programming language that's designed to be easy to read and write. It uses words like 'if', 'for', and 'print' that make sense to humans, unlike older languages that look more like secret codes!"
    },
    {
        question: "Why do programmers like using Python?",
        answers: [
            "It's the fastest programming language",
            "It only works on expensive computers",
            "It's easy to read and learn, with simple syntax",
            "It can only be used for games"
        ],
        correctIndex: 2,
        explanation: "Python is popular because its code looks almost like English! For example, to print 'Hello', you just write: print('Hello'). This makes it perfect for beginners and lets you focus on solving problems instead of memorizing complicated syntax."
    },
    {
        question: "What kind of tasks can you do with Python?",
        answers: [
            "Only make websites",
            "Only control robots",
            "Many things: websites, games, robots, data analysis, and more",
            "Only do math homework"
        ],
        correctIndex: 2,
        explanation: "Python is incredibly versatile! It's used to build websites (like Instagram), create games, analyze data, control robots (like our SPIKE Prime!), and even power artificial intelligence. It's like a Swiss Army knife for programming!"
    },

    // Section 2: What is PyBricks?
    {
        question: "What is PyBricks?",
        answers: [
            "A type of LEGO brick made of Python snakes",
            "A Python library specifically designed to control LEGO robots",
            "A video game about building with LEGO",
            "A new flavor of ice cream"
        ],
        correctIndex: 1,
        explanation: "PyBricks is a special Python library (a collection of pre-written code) that makes it easy to control LEGO robots like the SPIKE Prime. Instead of writing complicated low-level code, you can use simple commands like 'drive forward' or 'turn left'!"
    },
    {
        question: "What does PyBricks let you control on your LEGO robot?",
        answers: [
            "Only the motors",
            "Only the display screen",
            "Motors, sensors, display, speakers, lights, and more",
            "Nothing - it's just for planning"
        ],
        correctIndex: 2,
        explanation: "PyBricks gives you control over everything on your LEGO SPIKE Prime hub! You can control motors to make it move, read sensors to detect colors or obstacles, show patterns on the 5×5 LED display, play sounds, and even check the battery level."
    },
    {
        question: "How do you make your robot drive forward in PyBricks?",
        answers: [
            "robot.drivebase.straight(500)",
            "robot.go.forward.now()",
            "drive_forward(yes)",
            "move.robot.ahead"
        ],
        correctIndex: 0,
        explanation: "In PyBricks, you use 'robot.drivebase.straight(500)' to drive forward 500 millimeters. The number tells the robot how far to go. Negative numbers make it go backward! This simple command handles all the complicated motor coordination for you."
    },

    // Section 3: Why use libraries?
    {
        question: "What is a 'library' in programming?",
        answers: [
            "A building where books are stored",
            "A collection of pre-written code you can use in your programs",
            "A type of computer memory",
            "A list of rules you must follow"
        ],
        correctIndex: 1,
        explanation: "A programming library is like a toolbox full of ready-made tools! Instead of building everything from scratch, you can use code that other programmers have already written and tested. It's like using LEGO bricks instead of molding your own plastic!"
    },
    {
        question: "Why is using a library like PyBricks helpful?",
        answers: [
            "It makes your code longer and more complicated",
            "It saves time by providing ready-made functions for common tasks",
            "It only works on Tuesdays",
            "It makes robots slower"
        ],
        correctIndex: 1,
        explanation: "Libraries like PyBricks save you tons of time! Instead of writing hundreds of lines of code to control a motor, you can use one simple command like 'motor.run(500)'. This lets you focus on making your robot do cool things instead of figuring out low-level technical details!"
    },
    {
        question: "Without PyBricks, what would you need to do to control motors?",
        answers: [
            "Just think about it really hard",
            "Write complex code to send electrical signals and manage motor timing",
            "Use a remote control instead",
            "Motors can't be controlled without PyBricks"
        ],
        correctIndex: 1,
        explanation: "Without libraries like PyBricks, you'd have to write detailed code to send precise electrical signals to motors, calculate speeds, handle acceleration, sync multiple motors, and manage timing. PyBricks does all this complicated work for you with simple commands!"
    },

    // Section 4: How to use PyBricks
    {
        question: "What's the first thing your PyBricks program needs to do?",
        answers: [
            "Print 'Hello World' on the screen",
            "Import the PyBricks modules you want to use",
            "Calculate the meaning of life",
            "Delete all your files"
        ],
        correctIndex: 1,
        explanation: "Before you can use PyBricks features, you need to import them! For example: 'from pybricks.hubs import PrimeHub'. This tells Python to load the code for the SPIKE Prime hub so you can use it in your program. Think of it like opening a toolbox before you start working!"
    },
    {
        question: "In our robot projects, what does 'robot.drivebase.turn(90)' do?",
        answers: [
            "Makes the robot explode",
            "Turns the robot 90 degrees to the right",
            "Sets the robot's age to 90",
            "Makes the robot drive 90 millimeters"
        ],
        correctIndex: 1,
        explanation: "The command 'robot.drivebase.turn(90)' makes your robot turn 90 degrees (a right angle) to the right. If you use a negative number like turn(-90), it turns left instead! The robot's built-in gyro sensor helps make these turns accurate."
    },
    {
        question: "If you want your robot to wait for 2 seconds before doing something, what should you use?",
        answers: [
            "wait(2000)",
            "sleep(2)",
            "pause(2 seconds)",
            "hold_on(2)"
        ],
        correctIndex: 0,
        explanation: "In PyBricks, you use 'wait(2000)' to pause for 2 seconds. The number is in milliseconds, so 2000 milliseconds = 2 seconds. This is super useful when you want your robot to drive for a certain amount of time or wait between movements!"
    },
    {
        question: "What's TRUE about using the robot in our season missions?",
        answers: [
            "You have to initialize everything yourself every time",
            "The RobotController already initialized everything - just use robot.drivebase!",
            "You need to write 100 lines of setup code first",
            "The robot programs itself"
        ],
        correctIndex: 1,
        explanation: "Great news! In our project, the RobotController class does all the initialization for you. When your mission's run() function receives the 'robot' parameter, everything is ready to go - motors, sensors, display, everything! You just focus on making your robot do cool things!"
    },

    // Section 5: Using the Project - Setup
    {
        question: "What command creates a new season for your robot?",
        answers: [
            "python new_season.py",
            "python create_season.py",
            "python start_robot.py",
            "python make_season.py"
        ],
        correctIndex: 0,
        explanation: "You use 'python new_season.py' to create a new season! This script asks you questions about your robot (motor ports, wheel size, etc.) and generates a complete season folder with all the files you need, perfectly configured for YOUR robot."
    },
    {
        question: "What does new_season.py ask you about?",
        answers: [
            "Only your team name",
            "Your robot's motor ports, wheel size, and team information",
            "What color you like",
            "How fast you can run"
        ],
        correctIndex: 1,
        explanation: "new_season.py asks important questions about your actual robot: which ports your motors are plugged into, how big your wheels are, how far apart they are, and your team info. It uses these answers to create a configuration file (season_config.py) that matches YOUR specific robot!"
    },
    {
        question: "Why do you need to measure your robot's wheels?",
        answers: [
            "Just for fun",
            "So the robot knows how far it actually travels when motors turn",
            "To make the robot look pretty",
            "Measurements don't matter"
        ],
        correctIndex: 1,
        explanation: "Wheel measurements are crucial for accuracy! When you tell the robot to drive 500mm, it needs to know your wheel size to calculate how many rotations that takes. Bigger wheels = fewer rotations needed. Accurate measurements = accurate movements!"
    },

    // Section 6: Using the Project - Missions
    {
        question: "Where do you run the new_mission.py script from?",
        answers: [
            "From the project root folder",
            "From inside your season folder",
            "From your home directory",
            "It doesn't matter where"
        ],
        correctIndex: 1,
        explanation: "You must run new_mission.py from INSIDE your season folder! The script needs to access season_config.py and season_menu.py in the current folder. Example: 'cd my_season' then 'python ../new_mission.py'"
    },
    {
        question: "What does new_mission.py automatically update for you?",
        answers: [
            "Nothing - you have to update everything manually",
            "Only the mission file",
            "The season_menu.py file with imports and mission options",
            "Your robot's firmware"
        ],
        correctIndex: 2,
        explanation: "This is the magic! new_mission.py automatically updates season_menu.py to add the import statement AND add your mission to the missions dictionary. You never have to manually edit season_menu.py - the script does it all for you!"
    },
    {
        question: "What file contains your robot's motor ports and wheel measurements?",
        answers: [
            "robot_settings.py",
            "config.py",
            "season_config.py",
            "mission_config.py"
        ],
        correctIndex: 2,
        explanation: "season_config.py is where all your robot-specific settings live! It has the motor ports, motor directions, wheel diameter, axle track (distance between wheels), and default speeds. This file is generated by new_season.py based on your answers."
    },

    // Section 7: Using the Project - Coding & Running
    {
        question: "What function do you write your mission logic in?",
        answers: [
            "def main():",
            "def start():",
            "def run(robot: RobotController, display):",
            "def mission():"
        ],
        correctIndex: 2,
        explanation: "Every mission has a run() function that receives two parameters: 'robot' (the RobotController with everything initialized) and 'display' (helper for showing patterns). This is where you write all your robot's movements and actions!"
    },
    {
        question: "What two parameters does the run() function receive?",
        answers: [
            "robot and motor",
            "robot and RobotController",
            "hub and display",
            "robot and display"
        ],
        correctIndex: 3,
        explanation: "The run() function receives 'robot' (the RobotController instance with drivebase, hub, attachments, etc. all ready to use) and 'display' (a helper object with shortcuts like show_countdown and show_completion_checkmark)."
    },
    {
        question: "When uploading files to the SPIKE Prime hub, how should they be organized?",
        answers: [
            "In separate folders by type",
            "All .py files in the same flat folder (no subfolders)",
            "In a missions/ subfolder",
            "Organization doesn't matter"
        ],
        correctIndex: 1,
        explanation: "IMPORTANT: PyBricks MicroPython doesn't support subdirectories! All your .py files must be uploaded to the same folder on the hub with NO subfolders. This is a PyBricks limitation - imports must be simple like 'import mission_01' not 'from missions.mission_01'."
    },
    {
        question: "What file do you run on the hub to see your mission menu?",
        answers: [
            "main.py",
            "start.py",
            "season_menu.py",
            "robot_controller.py"
        ],
        correctIndex: 2,
        explanation: "You run season_menu.py on the hub! This file creates a menu on the hub's display showing all your missions. Use the left/right buttons to navigate and the center button to select and run a mission. The menu was automatically set up by new_season.py and updated by new_mission.py!"
    }
];

// Presentation State
let currentSlideIndex = 0;

// Quiz State
let currentQuestionIndex = 0;
let score = 0;
let userAnswers = [];

// DOM Elements
const welcomeScreen = document.getElementById('welcome-screen');
const presentationScreen = document.getElementById('presentation-screen');
const quizScreen = document.getElementById('quiz-screen');
const resultsScreen = document.getElementById('results-screen');
const reviewScreen = document.getElementById('review-screen');

const startPresentationButton = document.getElementById('start-presentation-button');
const startQuizButton = document.getElementById('start-quiz-button');
const nextButton = document.getElementById('next-button');
const reviewButton = document.getElementById('review-button');
const restartButton = document.getElementById('restart-button');
const finishButton = document.getElementById('finish-button');

const prevSlideButton = document.getElementById('prev-slide');
const nextSlideButton = document.getElementById('next-slide');
const currentSlideElement = document.getElementById('current-slide');
const totalSlidesElement = document.getElementById('total-slides');
const slidesContent = document.getElementById('slides-content');

const progressFill = document.getElementById('progress-fill');
const progressText = document.getElementById('progress-text');
const questionText = document.getElementById('question-text');
const answersContainer = document.getElementById('answers-container');
const feedback = document.getElementById('feedback');
const feedbackText = document.getElementById('feedback-text');
const currentScoreElement = document.getElementById('current-score');
const totalQuestionsElement = document.getElementById('total-questions');

// Event Listeners
startPresentationButton.addEventListener('click', startPresentation);
prevSlideButton.addEventListener('click', previousSlide);
nextSlideButton.addEventListener('click', nextSlide);
startQuizButton.addEventListener('click', startQuiz);
nextButton.addEventListener('click', nextQuestion);
reviewButton.addEventListener('click', showReview);
restartButton.addEventListener('click', restartQuiz);
finishButton.addEventListener('click', showResults);

// Presentation Functions
function startPresentation() {
    currentSlideIndex = 0;
    welcomeScreen.classList.remove('active');
    presentationScreen.classList.add('active');

    totalSlidesElement.textContent = presentationSlides.length;
    renderSlides();
    showSlide(0);
}

function renderSlides() {
    slidesContent.innerHTML = '';
    presentationSlides.forEach((slide, index) => {
        const slideDiv = document.createElement('div');
        slideDiv.className = 'slide';
        slideDiv.innerHTML = `
            <div class="slide-icon">${slide.icon}</div>
            <h2>${slide.title}</h2>
            ${slide.content}
        `;
        slidesContent.appendChild(slideDiv);
    });
}

function showSlide(index) {
    currentSlideIndex = index;
    currentSlideElement.textContent = index + 1;

    // Show/hide slides
    const slides = slidesContent.querySelectorAll('.slide');
    slides.forEach((slide, i) => {
        slide.classList.toggle('active', i === index);
    });

    // Update navigation buttons
    prevSlideButton.disabled = index === 0;

    // Show quiz button on last slide
    if (index === presentationSlides.length - 1) {
        nextSlideButton.style.display = 'none';
        startQuizButton.style.display = 'inline-block';
    } else {
        nextSlideButton.style.display = 'inline-block';
        startQuizButton.style.display = 'none';
    }
}

function previousSlide() {
    if (currentSlideIndex > 0) {
        showSlide(currentSlideIndex - 1);
    }
}

function nextSlide() {
    if (currentSlideIndex < presentationSlides.length - 1) {
        showSlide(currentSlideIndex + 1);
    }
}

// Quiz Functions
function startQuiz() {
    currentQuestionIndex = 0;
    score = 0;
    userAnswers = [];

    welcomeScreen.classList.remove('active');
    presentationScreen.classList.remove('active');
    quizScreen.classList.add('active');

    totalQuestionsElement.textContent = quizQuestions.length;

    showQuestion();
}

function showQuestion() {
    const question = quizQuestions[currentQuestionIndex];

    // Update progress
    const progress = ((currentQuestionIndex + 1) / quizQuestions.length) * 100;
    progressFill.style.width = progress + '%';
    progressText.textContent = `Question ${currentQuestionIndex + 1} of ${quizQuestions.length}`;

    // Display question
    questionText.textContent = question.question;

    // Clear previous answers
    answersContainer.innerHTML = '';
    feedback.classList.add('hidden');

    // Create answer buttons
    question.answers.forEach((answer, index) => {
        const button = document.createElement('button');
        button.className = 'answer-button';
        button.textContent = answer;
        button.addEventListener('click', () => selectAnswer(index));
        answersContainer.appendChild(button);
    });
}

function selectAnswer(selectedIndex) {
    const question = quizQuestions[currentQuestionIndex];
    const answerButtons = answersContainer.querySelectorAll('.answer-button');

    // Disable all buttons
    answerButtons.forEach(button => {
        button.classList.add('disabled');
        button.style.pointerEvents = 'none';
    });

    // Mark selected answer
    const isCorrect = selectedIndex === question.correctIndex;
    answerButtons[selectedIndex].classList.add(isCorrect ? 'correct' : 'incorrect');

    // If incorrect, also highlight the correct answer
    if (!isCorrect) {
        answerButtons[question.correctIndex].classList.add('correct');
    }

    // Update score
    if (isCorrect) {
        score++;
        currentScoreElement.textContent = score;
    }

    // Store user's answer
    userAnswers.push({
        questionIndex: currentQuestionIndex,
        selectedIndex: selectedIndex,
        correct: isCorrect
    });

    // Show feedback
    showFeedback(isCorrect, question.explanation);
}

function showFeedback(isCorrect, explanation) {
    feedback.classList.remove('hidden', 'correct', 'incorrect');
    feedback.classList.add(isCorrect ? 'correct' : 'incorrect');

    const icon = isCorrect ? '✓' : '✗';
    const message = isCorrect ? 'Correct!' : 'Not quite...';

    feedbackText.innerHTML = `<strong>${icon} ${message}</strong><br><br>${explanation}`;
}

function nextQuestion() {
    currentQuestionIndex++;

    if (currentQuestionIndex < quizQuestions.length) {
        showQuestion();
    } else {
        showResults();
    }
}

function showResults() {
    quizScreen.classList.remove('active');
    reviewScreen.classList.remove('active');
    resultsScreen.classList.add('active');

    const percentage = Math.round((score / quizQuestions.length) * 100);

    document.getElementById('final-score').textContent = score;
    document.getElementById('final-total').textContent = quizQuestions.length;
    document.getElementById('percentage').textContent = percentage + '%';

    // Performance message
    const performanceMessage = document.getElementById('performance-message');
    let message = '';

    if (percentage === 100) {
        message = '🎉 Perfect score! You\'re a PyBricks expert! You clearly understand Python, libraries, and how to use PyBricks to control your robot.';
    } else if (percentage >= 80) {
        message = '🌟 Great job! You have a solid understanding of PyBricks and Python. Review the questions you missed to become an expert!';
    } else if (percentage >= 60) {
        message = '👍 Good effort! You\'re learning the basics. Review the explanations and try the quiz again to improve your score.';
    } else {
        message = '💪 Keep learning! Don\'t worry - everyone starts somewhere. Read through the explanations carefully and try again. You\'ve got this!';
    }

    performanceMessage.textContent = message;
}

function showReview() {
    resultsScreen.classList.remove('active');
    reviewScreen.classList.add('active');

    const reviewContainer = document.getElementById('review-container');
    reviewContainer.innerHTML = '';

    userAnswers.forEach((userAnswer, index) => {
        const question = quizQuestions[userAnswer.questionIndex];

        const reviewItem = document.createElement('div');
        reviewItem.className = `review-item ${userAnswer.correct ? 'correct' : 'incorrect'}`;

        const questionDiv = document.createElement('div');
        questionDiv.className = 'review-question';
        questionDiv.textContent = `${index + 1}. ${question.question}`;

        const yourAnswerDiv = document.createElement('div');
        yourAnswerDiv.className = 'review-answer your-answer';
        yourAnswerDiv.innerHTML = `<strong>Your answer:</strong> ${question.answers[userAnswer.selectedIndex]}`;

        reviewItem.appendChild(questionDiv);
        reviewItem.appendChild(yourAnswerDiv);

        if (!userAnswer.correct) {
            const correctAnswerDiv = document.createElement('div');
            correctAnswerDiv.className = 'review-answer correct-answer';
            correctAnswerDiv.innerHTML = `<strong>Correct answer:</strong> ${question.answers[question.correctIndex]}`;
            reviewItem.appendChild(correctAnswerDiv);
        }

        const explanationDiv = document.createElement('div');
        explanationDiv.className = 'review-explanation';
        explanationDiv.innerHTML = `<strong>Explanation:</strong> ${question.explanation}`;
        reviewItem.appendChild(explanationDiv);

        reviewContainer.appendChild(reviewItem);
    });
}

function restartQuiz() {
    resultsScreen.classList.remove('active');
    welcomeScreen.classList.add('active');
}

// Update score display on load
currentScoreElement.textContent = '0';
totalQuestionsElement.textContent = quizQuestions.length;
