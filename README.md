# DragonVale-Automation

## Introduction
The program files in this repository are made to automate aspects of the mobile game DragonVale using computer vision. 
The current goal of programs are to farm event currency, however, more may be added in the future.


The benefit of using computer vision is that, if done correctly, there should be no risk of damage to your island if it misclicks.

If you enjoy this, I would appreciate a star on the repository to let me know.

## Requirements
If you have used GitHub before, I recommend you fork the repository. Otherwise, you can download the files and work on them without github.

All programs are written with Python 3.
The following libraries are also needed:
```sh
numpy
opencv
pyautogui
```
These libraries can be installed by running the following command in a terminal wherever you installed the files:
```sh
pip install -r requirements.txt
```

## Setup


In order to use the program, you need to take a screenshot of each item the program will need to click/tap. This will include things such as the breeding cave, habitat, confirmation buttons, etc.
Each picture should be distinct from everything else in the game so the program does not interact with the wrong things. These pictures should not contain elements that can change randomly and should be
taken with the emulator at a consistent resolution.

Once you have your pictures of each of the steps saved in the same area as the python file, their names need to be added to the images array in the correct order:
```sh
images = ["step1.png", "step2.png", "step3.png", "etc.png"]
```

This should be enough to get something working, however, it is recommended you play around with adding a delay between clicks/taps for some consistency. 
I recommend starting with 1 second and lowering or raising it depending on the results.
```sh
time.sleep(1)
```
This should be enough to get the program working! Run the python file and see how it goes. I recommend running it from a terminal/command line interface, but it should work regardless.

## Recommendations

There are a few areas where things may go wrong, and where extra coding may be needed.

For game crashes, it is possible to detect the game icon or the continue/retry buttons. However, you may need to backtrack to an earlier step depending on when you crash.
I only recommend this if your game crashes often on your emulator.
