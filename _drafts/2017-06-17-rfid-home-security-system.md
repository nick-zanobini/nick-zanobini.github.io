---
layout: post
title: RFID Home Security System
date: 2016-11-05 19:15
author: nickzanobini
comments: true
categories: [Uncategorized]
---

<!-- 
Bill of Materials
Housing Design
Electronics Design
Software 
-->

My house and my garage weren't attached and after continuously having to go into the garage with my arms full I got tired of putting my stuff on the ground, digging my keys out of my pocket and unlocking my garage. That's when I decided there has to be a better way to get in to my garage. I did some research and decided building a RFID door lock would both solve my problems and be fun.  

I have since moved and no longer have a garage to have this installed in, so I designed and 3D printed a housing for everything.

<!-- Image of the first iteration, 2 images of the final version -->

<!-- Table of Contents -->

###Bill of Materials
*My Macbook Pro
*Arduino IDE
*USB A to USB B cable
*Arduino Mega
*20x4 LCD Screen
*Parallax RFID Reader
*16 digit keypad
*Jumper cables
*Enclosure for the electronics
*12VDC 300mA power supply
*9VDC 500mA power supply
*12V NC Electric Strike Plate
*TIP29 Transistor
*Breadboard or soldering iron and so
*Zener switching diode

###Hosing Design

I needed a housing that would hold the keypad, LCD screen Arduino and door strike in relative proximity to eachother. I decided this would be a perfect time to work on my 3D modeling skills and got to work designing a housing.

<!-- 3 images of the setup. 1 of the whole assembly and 1 of both the front pannel and the door strike holder. -->


###Electronics Selection and Design
I decided on building an RFID Door lock system that is also password protected for two factor authenticaton. First I started with just the Arduino and the RFID reader. I chose to use an Arduino Mega for its expansive I/O and the Parallax RFID because RadioShack had them on sale for $10 awhile ago and a NC electric door strike so even if the system failed the door would remain locked. I then expanded the system to include both a LCD screen and a 16 digit keypad.

After developing the system with the Arduino Mega I decided I wanted to shrink the project down into a smaller package. I decided to go with the ATmega328P because it had just enough I/O and is easily programmed using Arduino. I utilized the ATmega's analog pins for reading the keypad and the rest of the digital pins for the LCD screen, trigging the door strike and the RFID reader.

<!-- Arduino Schematic -->
<!-- ATmega Schematic -->




Improvements: 
*Build a small circuit so there’s only one power supply and regulate the voltage to the Arduino and the strike plate
*Touch screen?
*convert to a Raspberry Pi
*trigger security camera to take a picture when user tries to swipe in
*logging user attempts and time stampd to text file

Here is the code for the project and the wiring diagram.

{% highlight arduino %}
// Updated 4/02/2015
// Nick Z.
// Keypad Door Lock
#include &lt;LiquidCrystal.h&gt;
#include &lt;Keypad.h&gt;
//constants for LEDs and Pins
int greenLED = 13;
int redLED = 12;
int RFIDEnablePin = 11;
int relay = 10;
LiquidCrystal lcd(8, 9, 4, 5, 6, 7);   
//set our employees
const byte numEmployees = 4;
// Array values are TAG ID, First Name, Last Name, Secret Code
char *employees[][4] = {
  {"1900711ACC","Jane","Doe","6566"},         // blue faab
  {"010D8EA279","Neil","Caffrey","1234"},     // black circle
  {"1600199FB3","Leroy","Gibbs","1234"},      // white circle
  };
  //setup the state table states
int currentState = 1;                 // State variable initialized to state 1 (read card)
const int waitingForTagID = 1;        // Waiting for Card input
const int waitingForPasscode = 2;     // Waiting for keypad input
// Misc Global Variables
char* ourCode;                        // Used to store the secret code for the user who's RFID was read
int currentPosition = 0;              // Used to remember the location of the code input
int  val = 0;                         // Used in reading the card
char code[10];                        // The TAG ID of the card
int bytesread = 0;                    // Used in reading the card
int currentEmployee;                  // The current employee being worked is stored here
long myTimer;                         // Used for the code entry timeout
char currPassword[4];
boolean passCheck;
// The name of the location for this reader.  This is displayed in the serial output
const char locationName[] = "Neils's Room";
//define the keypad
const byte rows = 4;
const byte cols = 4;
char keys[rows][cols] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','#','D'}
  };
  byte rowPins[rows] = {38,40,42,44};
byte colPins[cols] = {46,48,50,52};
Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, rows, cols);
/* ==================================    Setup    ================================== */
void setup() {
  Serial.begin(2400); // The RFID reader outputs at a whopping 2400 Baud
  Serial.println("Start Running");
  Serial.println("====================");
    pinMode(RFIDEnablePin, OUTPUT);   // Set as OUTPUT to connect it to the RFID /ENABLE pin
  digitalWrite(RFIDEnablePin, LOW); // Activate the RFID reader
    //setup and turn off both LEDs
  lcd.begin(16, 4);
  pinMode(redLED, OUTPUT);
  pinMode(greenLED, OUTPUT);
  digitalWrite(redLED, LOW);
  digitalWrite(greenLED, LOW);
    displayTagScanScreen();          //Put up default screen for reading the tags
}
void loop() {
  int l;
  int empid;
    switch (currentState)  {
    case waitingForTagID:
      digitalWrite(RFIDEnablePin, LOW);      // Enable RFID Reader
            if(Serial.available() &gt; 0) {           // if data available from reader
        if((val = Serial.read()) == 10) {    // check for header
          bytesread = 0; 
                    while(bytesread&lt;10) {              // read 10 digit code              if( Serial.available() &gt; 0) {
              val = Serial.read();
              if((val == 10)||(val == 13)) { // if header or stop bytes before the 10 digit reading
                break;                       // stop reading
              }
              code[bytesread] = val;         // add the digit
              bytesread++;                   // ready to read next digit
            }
          } 
                    if(bytesread == 10) {              // if 10 digit read is complete
            // Check to see if tag is valid and attached to an employee
                        code[10] = '\0';                // Add null at end to terminate the string
             empid = getEmployee(code);     // Get the employee id of the tag read, -1 means no match
             if (empid == -1) {
               digitalWrite(RFIDEnablePin, HIGH);  // Turn off RFID Reader
               invalidCard();                      // Display invalid card message
               Serial.print("Unkown Code: ");
               Serial.println(code);
               digitalWrite(RFIDEnablePin, LOW);   // Turn on RFID reader
             } else {
               currentEmployee = empid;            // Store for future use
               displayCodeEntryScreen(employees[empid][1]);  //Display code entry screen with first name of employee
               currentState = waitingForPasscode;            // Change the state to waiting for passcode entry
               ourCode = employees[empid][3];                // Place the employee secret code into the code entry value
               Serial.println(ourCode);//TESTING
               clearSerial();                                // Clear any extra data on the serial port
               myTimer = millis();
             }
          } 
                    bytesread = 0; 
        }
      }
      break;
          case waitingForPasscode:
      digitalWrite(RFIDEnablePin, HIGH);                    // Disable the RFID reader while doing code input
            // Nicks Added Code
      // Higer Security
            // Clear the asterisk area for code entry
      lcd.setCursor(14,3);
      lcd.print("    ");
      lcd.setCursor(14,3);
            for(int i=0; i&lt;=3; i++){
        currPassword[i] = keypad.waitForKey();
        lcd.print("*");
        Serial.print(currPassword[i]);//TESTING
      }
      Serial.println("");
      Serial.println(sizeof(currPassword));//TESTING
      Serial.println(currPassword);//TESTING
            for(int k=0; k&lt;4; k++){
        passCheck = true;
        char ourCodeTemp = ourCode[k];
        char currPasswordTemp = currPassword[k];
        if(ourCodeTemp != currPasswordTemp){
            passCheck = false;
        }
      }
            if ( passCheck ) {
        logEmployee(currentEmployee, true);
        unlockDoor();
        currentPosition = 0;
        currentState = waitingForTagID;
        clearSerial();
      } else if (currPassword != ourCode) {
        // Does not match so it is an invalid code
        logEmployee(currentEmployee, false);          // Log to the serial port the failue
        invalidCode();                                // Display invalid code screen
        currentPosition = 0;                          // Set the read position back to 0
        currentState = waitingForTagID;               // Change the state back to waiting for RFID read
        clearSerial();                                // Clear and junk that is on the serial port
      }
      // End of Nicks Code
  }
  }
  /***********************************************************************************************
  FUNCTION: getEmployee
    RETURNS:
    The array element id of the employee that matches the RFID TAG.  If no employee matches
    then -1 is returned.
      INPUTS:
    tagID (char)  : The value read from the RFID TAG
      COMMENTS:
    This function will take the tag id that was read from the RFID reader and loop through all
    employees looking for a match.  When it finds a match it returnes the element id for that
    employee.
        If all employees have been read without a match, it returns -1 for no match
***********************************************************************************************/
int getEmployee(char tagID[]) {
    int l;
        for (l=0; l&lt;numEmployees; ++l) {       if (strcmp(tagID, employees[l][0]) == 0)          return l;     }          return -1; } /***********************************************************************************************   FUNCTION: logEmployee      RETURNS:      NOTHING (void)        INPUTS:     empid (int)        : This is the employee id or element number from the employee array     grantAccess (int)  : If the emplyee was granted access then this is true, if the employee                          was denied access then this is false.        COMMENTS:     This function simply outputs to the serial port if a user was granted or denied access,     the user name and the location of this reader.          This function could be cleaned up by using sprintf to create a combined employee name (FOR),     the TO: as well.  But it was quick and used what we have talked about so far.     ***********************************************************************************************/ void logEmployee(int empid, int grantedAccess) {   if (grantedAccess) {     Serial.println("ACCESS GRANTED:");   } else {     Serial.println("ACCESS DENIED:");   }   Serial.print("  TO: ");   Serial.println(locationName);   Serial.print("  FOR: ");   Serial.print(employees[empid][1]);   Serial.print(" ");   Serial.println(employees[empid][2]);   Serial.println(" ");   Serial.println(" "); } /***********************************************************************************************   FUNCTION: clearSerial      RETURNS:      NOTHING (void)        INPUTS:     NONE        COMMENTS:     This function simply reads any data on the serial port until there is no more data.  It     is basically throwing away any extra input on the serial port effectivly clearing it.    ***********************************************************************************************/ void clearSerial() {   while (Serial.available() &gt; 0) {
    Serial.read();
  }
  }
  void invalidCode() {
  digitalWrite(redLED, HIGH);
  clearScreen();
  lcd.setCursor(0,0);
  lcd.print("********************");
  lcd.setCursor(0,1);
  lcd.print("** ACCESS DENIED! **");
  lcd.setCursor(0,2);
  lcd.print("**  INVALID CODE  **");
  lcd.setCursor(0,3);
  lcd.print("********************");
    delay(5000);
  digitalWrite(redLED, LOW);
  displayTagScanScreen();
  }
  void invalidCard() {
  digitalWrite(redLED, HIGH);
  clearScreen();
  lcd.setCursor(0,0);
  lcd.print("********************");
  lcd.setCursor(0,1);
  lcd.print("** ACCESS DENIED! **");
  lcd.setCursor(0,2);
  lcd.print("**  INVALID CARD  **");
  lcd.setCursor(0,3);
  lcd.print("********************");
    delay(5000);
  digitalWrite(redLED, LOW);
  displayTagScanScreen();
  }
  void unlockDoor() {
  digitalWrite(greenLED, HIGH);
  clearScreen();
  lcd.setCursor(0,0);
  lcd.print("********************");
  lcd.setCursor(0,1);
  lcd.print("** ACCESS GRANTED **");
  lcd.setCursor(0,2);
  lcd.print("**   WELCOME!!    **");
  lcd.setCursor(0,3);
  lcd.print("********************");
    digitalWrite(relay, HIGH); // Unlock door!
  delay(5000);
  digitalWrite(relay, LOW); // Unlock door!
  digitalWrite(greenLED, LOW);
  displayTagScanScreen();
  }
  void codeEntryTimeout() {
  digitalWrite(redLED, HIGH);
  clearScreen();
  lcd.setCursor(0,0);
  lcd.print("********************");
  lcd.setCursor(0,1);
  lcd.print("**   CODE ENTRY   **");
  lcd.setCursor(0,2);
  lcd.print("**   TIMEOUT!!    **");
  lcd.setCursor(0,3);
  lcd.print("********************");
    //add any code to unlock the door here
  delay(5000);
  digitalWrite(greenLED, LOW);
  displayTagScanScreen();
  }
  void displayTagScanScreen() {
  clearScreen();
  lcd.setCursor(0,0);
  lcd.print("     Welcome to     ");
  lcd.setCursor(0,1);
  lcd.print("    Nick's Room    ");
  lcd.setCursor(2,2);
  lcd.print("In order to enter");
  lcd.setCursor(3,3);
  lcd.print("Please Scan Tag");
  }
  void displayCodeEntryScreen(char *firstName) {
  clearScreen();
  lcd.setCursor(0,0);
  lcd.print("Welcome");
  lcd.setCursor(8,0);
  lcd.print(firstName);
  lcd.setCursor(0,2);
  lcd.print("Please Enter Your");
  lcd.setCursor(1,3);
  lcd.print("Secret Code:");
  }
  void clearScreen() {
  lcd.setCursor(0,0);
  lcd.print("                    ");
  lcd.setCursor(0,1);
  lcd.print("                    ");
  lcd.setCursor(0,2);
  lcd.print("                    ");
  lcd.setCursor(0,3);
  lcd.print("                    ");
  }
{% endhighlight %}
