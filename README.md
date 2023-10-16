# Rocksmith Song Download Helper

Rocksmith Song Download Helper is a tool designed to streamline the process of adding custom DLC (downloadable content) songs to Rocksmith 2014. With a simple GUI interface, it monitors a specified download directory for any `.psarc` files (Rocksmith's custom song format) and automatically moves them to the Rocksmith 2014 DLC directory.

## Features

* Monitor your Download directory for `.psarc` files.
* Automatically move detected `.psarc` files to the Rocksmith 2014 DLC directory.
* User-friendly GUI interface.
* Provides logs of moved files.

## Installation
 
 1. Ensure you have Python installed on your machine.
 2. Clone or download the rocksmith-song-download-helper repository.
 3. Navigate to the directory and install the required dependencies using:
 ``
 pip install -r requirements.txt
 ``

 ## Usage
 1. Run the script:
 `` 
 python rocksmith_song_download_helper.py
``
 2. Use the GUI to specify:
    * The download path where new `.psarc` files will appear.
    * The Rocksmith 2014 DLC directory where songs should be moved.

3. Click **Start** to begin monitoring the download directory. Any detected `.psarc` files will be automatically moved to the DLC directory and logged in the interface.

## Contributing

Contributions are welcome! Please create an issue or submit a pull request if you'd like to improve the tool.

## Credits
Made by .[miketsak.gr](https://miketsak.gr/)