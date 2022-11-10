<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/uberskier/Webcam-Security-System">
    <img src="ReadMe-Images/Webcam-Security-System-Logo-Crop.jpg" alt="Logo" width="138" height="200">
  </a>

  <h3 align="center">Webcam Security System</h3>

  <p align="center">
    WSS is an affordable home security camera with facial recognition, phone alerts, and smart home controls. 
    <br />
    <a href="https://github.com/uberskier/Webcam-Security-System"><strong>Explore the System »</strong></a>
    <br />
    <br />
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

This is a great and easy way to keep track of who enters your home when your away. The Webcam Security System is the cheapest way to keep tabs on your home and family. WSS uses facial recognition to tell you exactly who is entering your home and even offers smart home connectivity to prepare your home for your arival. 

Here's why:
* Home security should be cheap and easily accessible 
* Everyone deserves to know who and when people enter their home

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* Python 3

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

Here is how to get your Webcam Security System up in running!

### Prerequisites

Before setting up WSS you need to have a few things prepared!

#### Hardware:

##### Recommended 
* Raspberry Pi 4
* External Webcam 720p or better
##### Other Options 
* Old laptop that can be dedicated to Security

<br />

#### Expected Software:
* Python 3
* Pip



### Installation

Below is the install requirements for running the System.

1. Open the Command Prompt or terminal

2. Install openCV
   ```sh
   pip install opencv-python
   ```

3. Install face_recognition
   ```sh
   pip install face_recognition
   ```

4. Install dlib 
   For Windows follow the instructions here: 
   https://www.geeksforgeeks.org/how-to-install-dlib-library-for-python-in-windows-10/
   
   For Raspberry Pi follow the instructions here:
   https://pyimagesearch.com/2017/05/01/install-dlib-raspberry-pi/

5. Install PushBullet
   ```sh
   pip install pushbullet.py==0.9.1
   ```

6. Install Requests
   ```sh
   pip install requests
   ```

7. Clone the Security System
   ```sh
   git clone https://github.com/uberskier/Webcam-Security-System.git
   ```



### Facial Recognition Setup

1. locate the People-Folders folder

2. Add a folder inside People-Folders named after the first name of the person you want to add

3. Add 20+ photos of said person with only their face present in each photo. The more photos you add the more accurate the system will be.

4. Once you have added all the people you want to run the following:
   ```sh
   python FaceEncoding.py
   ```
5. If you ever add more photos or more people re-run the FaceEncoding file.


### PushBullet and IFTTT Setup

To let the system send notifications and control smart products you will have to create accounts for Pushbullet and IFTTT.

#### API keys
1. In the Camera-Pictures folder add a file named
   ```sh
   APIkey.txt
   ```

#### PushBullet 

1. Follow these steps till you get the API key and copy it:
   https://www.geeksforgeeks.org/python-web-app-to-send-push-notification-to-your-phone/

2. In the APIkey file put the pushbullet key on the first line


#### IFTTT

1. Follow these stes till you get an API key and copy it:
   https://pimylifeup.com/using-ifttt-with-the-raspberry-pi/

2. In the APIkey file put the IFTTT key on the second line

3. Next line in the file put the following:
   ```sh
   New Person
   ```
4. On the next line put the name of the person the command belongs to spelled and capitilized just like how it is in the persons photo folder.

5. On the following lines put Always or People followed by any IFTTT commands broken up with colens. Always for always activated when the person is seen or People if it is activate only when the person is seen with another person. 
   ```sh
   Always:Baylor_Seen_Coming_In:Baylor_Set_Brightness_BedRoom
   People:Baylor_Seen_Several_People_Liv:Baylor_Seen_Several_People_Kit
   ```

6. Repeat steps 3-5 for commands for other people

<br />
<br />
The whole APIkey.txt file should look something like this:
```sh
o.HihH9n7ns&n2snuUn9n*0snf
sn8JFP9N7snB97Knw0nGSM
New Person
Baylor
Always:Baylor_Seen_Coming_In:Baylor_Set_Brightness_BedRoom
People:Baylor_Seen_Several_People_Liv:Baylor_Seen_Several_People_Kit
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>