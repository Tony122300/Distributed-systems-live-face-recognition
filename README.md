# Distributed-systems-live-face-recognition

To launch the application install the following packages first.
```
pip install opencv-python
pip install Flask
pip install numpy
pip install Flask-SocketIO
pip install eventlet
pip install waitress

pip install cmake
git clone https://github.com/davisking/dlib.git
cd dlib
mkdir build; cd build; cmake ..; cmake --build .
cd ..
python3 setup.py install --user
conda update conda
conda create -n env_dlib python=3.8
conda activate env_dlib
conda install -c conda-forge dlib
pip3 install face_recognition
```

To Launch the this use the command
```
python server.py
```
It will launch a web page on localhost:5000 or use "ipconfig" use the ipaddress and :5000
for example 192.168.0.185:5000

this is how the application should look like working
![image](https://user-images.githubusercontent.com/59939389/210273410-aa45e2ef-c036-4f4f-9faf-0083d4e90070.png)
