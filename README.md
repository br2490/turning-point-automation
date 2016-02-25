Code for the automation of TurningPoint in an experimental setting.
======

Purpose
------
This script automatically progresses through a set of TurningPoint polling questions in an experimental setting. It will automatically open polling for a given question, wait for the participant to answer, close polling and move to the next slide. It will repeat this process indefinitely until stopped by the experimenter. It will continue to try to open polling even on slides that are not designed to be polling slides, permitting the experimenter to introduce delay (e.g., distraction activities) by way of PowerPoint automatic slide progression. When a polling slide is again present it will pickup where it left off and continue to automate the remainder of the presentation.

Design
------
This code automates response device by [Turning Technologies](https://www.turningtechnologies.com/) through use of their "TurningPoint" Microsoft PowerPoint plugin and [Sikuli](http://sikulix.com). Due to the proprietary nature of Turning Technologies intercepting and using raw data from the USB IR receiver was not an option to automate our polls. Sikuli is a Java application that utilizes [OpenCV](http://opencv.org/) to preform screen region recognition and act accordingly on a match. Scripts for Sikuli are written in Jython. 

Our script recognizes the TurningPoint toolbar and set it as the main region (ROI) for the remaining searches. Polling at a rate of 50 times per second after recognizing our toolbar the script looks for the following: "Polling Closed" and the number of responses going from "0" to "1". If "Polling Closed" is true, the script attempts to send the hotkey to open polling, and will continue to do so until "Polling Closed" disappears from the region - signaling polling has opened. Next the script sits idle waiting for the number of responses to change from "O" to "1" - signaling a response from the participant has been registered. We provide a one second delay for the participant to change their answer; the script then sends the hotkey to close polling, focus Microsoft PowerPoint, send the hotkey (spacebar) to progress slides, and continues execution. 

License
------
GNU General Public License v3 

Contributors
------
Instructional Media and Technology Services, Barnard College, NY. 2016. 

Maintainer: Benjamin Rosner, brosner@barnard.edu 

