# Custom Discord RPC

## Setting up the config:
1. Create a new Discord application
2. Copy `Client ID` and paste into config.yaml `client_id`
3. To setup the game list, we will need to seperate each of the games by a "-" with the spacing from the config for the dashes and the remaining keys. Each game can contain the following:
    - `details` - This is the shorter description for the game:

        ![details](https://i.imgur.com/9Z7OdfI.png)
    - `state` - This is the longer description for the game:

        ![state](https://i.imgur.com/i1YbCfd.png)
    - `large_image` - The image key for the large image on the game. In order to attach your image to a key, open up your Discord Developers page for your app and scroll down to "Rich Presence Assets". From here, since we want a large image, we upload the image, enter the key (which we will write in the config) and select "Large". Then make sure to click "Upload Asset" and "Save Changes". After we add to the config, this will look like this:

        ![lg_image](https://i.imgur.com/KbQdc61.png)
    - `large_text` - This will be the text for when you hover over the large image:

        ![lg_text](https://i.imgur.com/nNRHtxo.png)
    - `small_image` - The image key for the small image on the game. In order to attach your image to a key, open up your Discord Developers page for your app and scroll down to "Rich Presence Assets". From here, since we want a small image, we upload the image, enter the key (which we will write in the config) and select "Small". Then make sure to click "Upload Asset" and "Save Changes". After we add to the config, this will look like this:

        ![sm_image](https://i.imgur.com/wjo0Nkx.png)
    - `small_text` - This will be the text for when you hover over the small image:

        ![sm_text](https://i.imgur.com/EApOnTl.png)


## How to run:

`python3 rpc.py`

To make this start on Windows boot, simply take the `dcustomrpc.py`, right click it, hover over "Send to" then click "Desktop (create shortcut)". Then cut the icon from your desktop, go to `shell:startup` in Windows Explorer and paste it in there.

## Requirements
- Pypresence
- ruamel.yaml
- Pillow
- Pystray
- Requests

To quickly install these, run the command: `python3 -m pip install -r requirements.txt` (Python3)

## Credits
Originally created by JakeMakesStuff

