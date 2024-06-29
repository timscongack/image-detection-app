# Image Detection and Web Display Application

This project consists of two main components: a Python application for real-time image detection using YOLO and an Express web server to display the detected images with previews.

## Overview

The application captures image feed from a camera, performs object detection using the YOLO model, and records images when specified objects are detected. The detected objects and image recordings are saved local file and paths are stored in a SQLite database. The Express web server provides a web interface to display the list of detected images along with previews and details.

## Features

- Real-time object detection using YOLO
- Records images when specified objects are detected
- Stores detection details and image files links in an SQLite database
- Express web server to display detected images with previews
- Configurable to detect specific objects like people, dogs, and trucks

## Libraries and Packages

### Python

- `opencv-python`: For capturing image and performing image processing
- `numpy`: For numerical operations
- `sqlite3`: For interacting with the SQLite database (included in Python's standard library)

### Node.js

- `express`: For creating the web server
- `sqlite3`: For interacting with the SQLite database
- `ejs`: For rendering HTML templates

## Setup Instructions

### Prerequisites

- Docker
- Python 3.9+
- Node.js 14+

### Initial Setup

1. Clone the repository to your local machine:
   ```sh
   git clone <repository-url>
   cd <repository-directory>

2.	Place the YOLO model files ([yolov3.weights](https://github.com/patrick013/Object-Detection---Yolov3/blob/master/model/yolov3.weights), [yolov3.cfg](https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg), [coco.names](https://github.com/pjreddie/darknet/blob/master/data/)) in the project/app root directory.

3.	Create the necessary directories and files as shown in the directory structure above.

## Running with Docker

1. Build `docker build -t image-detection-app .`
2. Run `docker run -p 3007:3007 image-detection-app`
3. Visit http://localhost:3007 in your browser to view the detected images.