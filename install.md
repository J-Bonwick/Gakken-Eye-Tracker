#Installation
##Part 1 - The Raspberry Pi:
1. Clone this repo to the raspberry pi.
2. Install `python-pip python-dev python-pil python-smbus`
3. Install required dependicies for python with `pip install pi3d numpy websocket_client svg.path`
4. Then start start the program by running `eye.py`

To test that everything is working use [web_Contoller.html](web_Contoller.html) on a local computer with a web browser to control the eye.
##Part 2 - The tracker:
This will need to run on a different computer to the raspberry pi.
1. Clone the repo [PoseNet Sketchbook](https://github.com/googlecreativelab/posenet-sketchbook/) to the server.
2. Then copy folder [colormapper](colormapper/) from this repository into the sketches folder and replace the existing one.
3. Install dependancies by running `yarn` in the top level of the cloned repository.
4. Then run `yarn watch`. The server should be running at **localhost:1234**.
5. From there Click on **Color Mapper** to load up the tracking program.
