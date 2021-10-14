<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://github.com/agrima30/Lab-Eyes/blob/master/Desktop-App/assets/textures/icon.png" alt="Project logo"></a>
</p>

<h3 align="center">LAB EYES</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/agrima30/Lab-Eyes.svg)](https://github.com/agrima30/Lab-Eyes/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/agrima30/Lab-Eyes.svg)](https://github.com/agrima30/Lab-Eyes/pulls)
<!-- [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE) -->

</div>

---

<p align="center"> A Website/Desktop App to assist visually challenged researchers in laboratories.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Deployment](#deployment)
- [Built Using](#built_using)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🔬 About <a name = "about"></a>
We aim at making synthetic biology laboratories more accessable for visually challenged researchers by helping them distinguish between apparatus of similar build. This app can even be used to know what chemical is stored in a container.<br>
Users can easily make qr codes for individual apparatus and paste it on them. The apparatus can then be easily identified by placing qr code infront of the camera. The scanner also reads it out for people who are visually challenged.

## 🏁 Getting Started <a name = "getting_started"></a>

To access the website, visit this link: [https://lab-eyes.netlify.app/]()<br>

To download the Desktop App, visit this link: [https://www.google.com]()<br>


## 🎈 Usage <a name="usage"></a>
- Website<br>
On the homepage, click on ```GENERATE QR``` and enter your text/link to instantly generate a static QR code. The QR can be then downloaded by clicking on the ```DOWNLOAD``` button.<br>
To scan a QR code, click on ```SCAN QR``` on homepage and present the QR code infront of the camera. Make sure the code is clearly visible and is within the bounding box. The scanner will then decode it and present you the result in a box below. Press any key to hear the text through connected speakers.
> The website must have access to your camera device for this feature to work.

- Desktop App<br>
On the homepage, click on ```GENERATE QR``` and enter your text/link. Press 'Enter' to generate a static QR code. The QR will be saved automatically in ```qr_codes``` folder at the app's location.<br>
To scan a QR code, click on ```SCAN QR``` on homepage and present the QR code infront of the camera. Make sure the code is clearly visible. The scanner will then decode it and read it out through connected speakers.
> You can also navigate in the app using keyboard buttons
> - ```UP```: To go to generation page
> - ```DOWN```: To go to scanning page
> - ```LEFT CTRL```: To go to home page
> - ```ESC```: To close the app

## 🚀 Deployment <a name = "deployment"></a>

The website is deployed on [Netlify](https://www.netlify.com/)

## ⛏️ Built Using <a name = "built_using"></a>
- Website
    - [ReactJS](https://reactjs.org/) - Front-end javascript library
    - [Material UI](https://mui.com/) - React UI library
- Desktop App
    - [PyGame](https://www.pygame.org/docs/) - Library
    - [OpenCV](https://docs.opencv.org/master/d6/d00/tutorial_py_root.html) - QR scanning
    - [qrcode](https://pypi.org/project/qrcode/) - QR generation

## ✍️ Authors <a name = "authors"></a>

- [@agrima30](https://github.com/agrima30)
- [@copyninja17](https://github.com/copyninja17)