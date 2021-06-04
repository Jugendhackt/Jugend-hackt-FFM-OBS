# Jugend hackt FFM OBS

## Setup

1. Download this as a ZIP file or clone the repository
2. Run the script configure.py with python and answer the questions.

```term
$ python configure.py
```

3. Import the Scene Collection into OBS
4. Switch to the imported Jugend_hackt Scene
5. Join the configured BBB meeting by right-clicking the "BigBlueButton" source in the scene named "BBB" and choosing "Interact". In BBB you should then select to join in "Listen only" mode.
6. Now hide the chat and user by moving your mouse to the top left corner of the area where the presentation and cameras are located and clicking there.
7. Close the interaction window.

## Usage

Most of the time you will simply have to choose the right scene. There also is the possibility to use the included lower thirds feature. This currently only works in the BBB scene. 

If you are using Windows you can add the control panel via the menu bar (View/Panels/Browser panels). You will have to choose a title and the file obs-lower-thirds\control-panel\index.html. You can now dock the panel between existing panels.

If you are using macOS or GNU/Linux, you can right-click on the "Steuerung Bauchbinden" Source and choose "Interact".

Now you can control the lower thirds. If you want to change the items in the predefined lower thirds list, you will have to edit the file obs-lower-thirds/control-panel/names.json. Alternatively, you can simply use the input fields.


