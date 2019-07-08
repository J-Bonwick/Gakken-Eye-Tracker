# Installation
## Part 1 - The Raspberry Pi:
1. Clone this repo to the raspberry pi.
2. Install `python-pip python-dev python-pil python-smbus`
3. Install required dependicies for python with `pip install pi3d numpy websocket_client svg.path`
4. Then start start the program by running `eye.py`

To test that everything is working use [web_Contoller.html](web_Contoller.html) on a local computer with a web browser to control the eye.
## Part 2 - The tracker:
This will need to run on a different computer to the raspberry pi.
1. Clone the repo [PoseNet Sketchbook](https://github.com/googlecreativelab/posenet-sketchbook/) to the server.
2. Then copy folder [colormapper](colormapper/) from this repository into the sketches folder and replace the existing one.
3. Install dependancies by running `yarn` in the top level of the cloned repository.
4. Then run `yarn watch`. The server should be running at **localhost:1234**.
5. From there Click on **Color Mapper** to load up the tracking program.
 ## Part 3 - Running the tracker on a server:
 In oder to get this running under apache we need to copy the compiled javascript to another folder.
 1. Follow Part 2, steps 1-4. This will build posenet into a dist folder in the root of the posenet sketchbook repository.
 2. Once built then terminate the yarn process.
 3. Make a folder to place the compiled javascript `posenet-dist`.
 4. Copy `dist/sketches/colormapper/index.html` to `posenet-dist`.
 5. Look in the `index.html` and also copy the relevant `style[HEXID].css` and `main[HEXID].js`.
 6. Then you should be able to access the modified colormapper at `posenet-dist/index.html`
