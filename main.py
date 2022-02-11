import PyQt5.QtWidgets as qtw
from pygame import mixer
import os


class Window(qtw.QWidget):

    def __init__(self):
        super().__init__()

        mixer.init()

        # setting the title
        self.setWindowTitle("PyPlayer")

        # self.setMaximumSize(1200, 700)
        self.setMinimumSize(1000, 600)

        self.setStyleSheet("""
        
        #btn{
            padding:12px 14px;
            font-size:20px;
            border-radius:5px;
            margin-right:14px;
            background:#FF0000;
            color:#fff;
        }

        #musicList{
            background:#212121;
            font-size:22px;
            border:none;
            color:#fff;
        }

        #body{
            background:#212121;
        }

      
       


        """)

        # setting layout
        self.setLayout(qtw.QVBoxLayout())

        self.setObjectName("body")

        # music list
        self.musicList = qtw.QListWidget()

        self.musicList.setObjectName("musicList")

        # adding space
        self.musicList.setSpacing(8)

        self.musicList.setWordWrap(True)

        # adding songs to list
        self.musicList.addItems(self.readSongs())

        # adding on click
        self.musicList.clicked.connect(self.playSong)

        self.musicList.setCurrentRow(0)

        self.layout().addWidget(self.musicList)

        # creating controll layout
        controls = qtw.QWidget()

        controls.setObjectName("controls")

        self.layout().addWidget(controls)

        # setting layout
        controls.setLayout(qtw.QHBoxLayout())

      

        # prev button
        self.prevBtn = qtw.QPushButton(
            "Prev", clicked=lambda: self.prevSong())
        controls.layout().addWidget(self.prevBtn)

        self.prevBtn.setObjectName("btn")

        # play and resume button
        self.playResumeBtn = qtw.QPushButton(
            "Play", clicked=lambda: self.playResumeSong())
        controls.layout().addWidget(self.playResumeBtn)

        self.playResumeBtn.setObjectName("btn")

        # next button
        self.nextBtn = qtw.QPushButton(
            "Next", clicked=lambda: self.nextSong())
        controls.layout().addWidget(self.nextBtn)

        self.nextBtn.setObjectName("btn")

        # show the window
        self.show()

    # methods
    def readSongs(self):
       


        songList = []
        
       
        # fetching all file
        files = os.listdir(path)
        # filtering mp3 files
        for file in files:
            if(file.endswith(".mp3")):
                songList.append(file)

        return songList

    def playSong(self):
        # unloading previous music
        mixer.music.unload()
        # get curent song
        selectedMusic = self.musicList.currentItem()
        # loading song
        mixer.music.load(f"./music/{selectedMusic.text()}")
        # playing
        mixer.music.play()
        # changin playbtn label
        self.playResumeBtn.setText("Pause")

    def playResumeSong(self):
        # cheking if song is already playing pause the song otherwise play
        if(mixer.music.get_busy()):
            mixer.music.pause()
            # changin playbtn label
            self.playResumeBtn.setText("Play")

        else:
            # play music
            mixer.music.unpause()
            # changin playbtn label
            self.playResumeBtn.setText("Pause")

    def nextSong(self):
        # finding cureent song  index
        currentSongIndex = self.musicList.currentRow()

        if(currentSongIndex < self.musicList.count()-1):
            # incrementing music index
            self.musicList.setCurrentRow(currentSongIndex+1)

            self.playSong()

    def prevSong(self):
        # finding cureent song  index
        currentSongIndex = self.musicList.currentRow()

        if(currentSongIndex > 0):
            # incrementing music index
            self.musicList.setCurrentRow(currentSongIndex-1)

            self.playSong()


app = qtw.QApplication([])
window = Window()
app.exec_()
