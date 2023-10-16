import os
import time
import shutil
import PySimpleGUI as sg
import threading
import webbrowser

sg.theme('DarkGrey5')
sg.set_options(font=('Arial Bold', 10))

def move_psarc_files(source_path, destination_path, window):
    # Check if both source and destination directories exist
    if not os.path.exists(source_path) or not os.path.exists(destination_path):
        sg.popup_error("Either source or destination path does not exist.")
        return

    while True:
        # List files in source directory
        for file in os.listdir(source_path):
            if file.endswith('.psarc'):
                source_file = os.path.join(source_path, file)
                destination_file = os.path.join(destination_path, file)
                
                # Move the file from source to destination
                shutil.move(source_file, destination_file)
                window.write_event_value('-FILE_MOVED-', file)
        
        time.sleep(5)  # Sleep for 5 seconds before checking again

def main():
    layout = [
        [sg.Text("Enter the dowload path:"), sg.InputText(key='-SOURCE-'), sg.FolderBrowse()],
        [sg.Text("Enter the Rocksmith2014\dlc path:"), sg.InputText(key='-DEST-'), sg.FolderBrowse()],
        [sg.Button('Start'), sg.Button('Exit'), sg.Button('Open Site')],
        [sg.Listbox(values=[], size=(50, 10), key='-FILE_LIST-')],
        [sg.Text("", size=(50,1), key='-STATUS-')],
        [sg.Text("Not Started", size=(20,1), key='-INDICATOR-', text_color='red'),sg.Text(" ", size=(35,1)), sg.Text("made by miketsak.gr")],
    ]

    window = sg.Window("PSARC File Mover", layout)

    while True:
        event, values = window.read()
        
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        elif event == 'Start':
            source_path = values['-SOURCE-']
            dest_path = values['-DEST-']
            
            threading.Thread(target=move_psarc_files, args=(source_path, dest_path, window), daemon=True).start()
            window['-INDICATOR-'].update("Started", text_color='green')
        elif event == '-FILE_MOVED-':
            moved_file = values['-FILE_MOVED-']
            window['-FILE_LIST-'].update([moved_file] + window['-FILE_LIST-'].get_list_values())
            window['-STATUS-'].update(f"Moved {moved_file} to {dest_path}")
        elif event == 'Open Site':
            webbrowser.open("https://ignition4.customsforge.com/")

    window.close()

if __name__ == "__main__":
    main()
