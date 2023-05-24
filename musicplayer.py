def unmutemusic():
    global currentvol
    root.unmutebutton.grid_remove()
    root.mutebutton.grid()
    mixer.music.set_volume(currentvol)

def mutemusic():
    global currentvol
    root.mutebutton.grid_remove()
    root.unmutebutton.grid()
    currentvol = mixer.music.get_volume()
    mixer.music.set_volume(0)

def resumemusic():
    root.ResumeButton.grid_remove()
    root.PauseButton.grid()
    mixer.music.unpause()
    AudioStatusLabel.configure(text='playing......')

def volumeup():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol+0.05)
    ProgressbarVolumeLabel.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    ProgressbarVolume['value'] = mixer.music.get_volume()*100

def volumedown():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol-0.05)
    ProgressbarVolumeLabel.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    ProgressbarVolume['value'] = mixer.music.get_volume()*100

def stopmusic():
    mixer.music.stop()
    AudioStatusLabel.configure(text='Stopped......')

def pausemusic():
    mixer.music.pause()
    root.PauseButton.grid_remove()
    root.ResumeButton.grid()
    AudioStatusLabel.configure(text='Paused......')

def playmusic():
    ad = audiotrack.get()
    mixer.music.load(ad)
    ProgressbarLabel.grid()
    root.mutebutton.grid()
    ProgressbarMusicLabel.grid()
    mixer.music.set_volume(0.4)
    ProgressbarVolume['value'] = 40
    ProgressbarVolumeLabel['text'] = '40%'
    mixer.music.play()
    AudioStatusLabel.configure(text='playing......')

    song = MP3(ad)
    totalsonglength = int(song.info.length)
    ProgressbarMusic['maximum'] = totalsonglength
    ProgressbarMusicEndTimeLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=totalsonglength))))
    ProgressbarMusicStarTimeLabel.grid()
    def ProgressbarMusicTick():
        CurrentSongLength = mixer.music.get_pos()//1000
        ProgressbarMusic['value'] = CurrentSongLength
        ProgressbarMusicStarTimeLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=CurrentSongLength))))
        ProgressbarMusic.after(2,ProgressbarMusicTick)
    ProgressbarMusicTick()

def musicurl():
    try:
        dd = filedialog.askopenfilename(initialdir='Music',
                                        title='Select Audio File',
                                        filetype=(('.mp3','.MP3'),('.wav','.WAV')))
    except:
        dd = filedialog.askopenfilename(title='Select Audio File',
                                        filetype=(('.mp3','.MP3'),('.wav','.WAV')))
    audiotrack.set(dd)

def createwidthes():
    global imbrowse,impause,implay,imstop,imvolumeudown,imvolumeup,imresume,imunmute,immute
    global AudioStatusLabel,ProgressbarVolumeLabel,ProgressbarVolume,ProgressbarLabel,ProgressbarMusicLabel,ProgressbarMusic,ProgressbarMusicEndTimeLabel,ProgressbarMusicStarTimeLabel


    implay = PhotoImage(file='play.png')
    impause = PhotoImage(file='pause-button.png')
    imstop = PhotoImage(file='stop-button.png')
    imvolumeup = PhotoImage(file='sound (1).png')
    imvolumeudown = PhotoImage(file='sound.png')
    imbrowse = PhotoImage(file='search.png')
    imresume = PhotoImage(file='end.png')
    immute = PhotoImage(file='mute.png')
    imunmute = PhotoImage(file='unmute.png')


    imbrowse = imbrowse.subsample(20,20)
    implay = implay.subsample(20,20)
    impause = impause.subsample(20,20)
    imstop = imstop.subsample(20,20)
    imvolumeup = imvolumeup.subsample(20,20)
    imvolumeudown = imvolumeudown.subsample(20,20)
    imresume = imresume.subsample(20,20)
    immute = immute.subsample(20,20)
    imunmute = imunmute.subsample(20,20)


    TrackLabel = Label(root,text='Select Audio Track : ',background='lightskyblue',font=('aerial', 15 ,'italic bold'))
    TrackLabel.grid(row=0,column=0,padx=20,pady=20)

    AudioStatusLabel = Label(root,text='',background='lightskyblue',font=('aerial',15,'italic bold'),width=20)
    AudioStatusLabel.grid(row=2,column=1)


    TrackLabelEntry = Entry(root,font=('aerial', 16 ,'italic bold'),width=35,textvariable=audiotrack)
    TrackLabelEntry.grid(row=0,column=1,padx=20,pady=20)


    BrowseButton = Button(root,text='Search  ',bg='azure2',font=('aerial', 13 ,'italic bold'),
                          width=200,bd=5,activebackground='purple4',image=imbrowse,compound=RIGHT,command=musicurl)
    BrowseButton.grid(row=0,column=2,padx=20,pady=20)
    
    PlayButton = Button(root,text='Play  ',bg='DarkOrchid3',font=('aerial', 13 ,'italic bold'),
                        width=200,bd=5,activebackground='purple4',image=implay,compound=RIGHT,command=playmusic)
    PlayButton.grid(row=1,column=0,padx=20,pady=20)
    
    root.PauseButton = Button(root,text='Pause  ',bg='Gold',font=('aerial', 13 ,'italic bold'),
                         width=200,bd=5,activebackground='purple4',image=impause,compound=RIGHT,command=pausemusic)
    root.PauseButton.grid(row=1,column=1,padx=20,pady=20)

    root.ResumeButton = Button(root,text='Resume  ',bg='Gold',font=('aerial', 13 ,'italic bold'),
                         width=200,bd=5,activebackground='purple4',image=imresume,compound=RIGHT,command=resumemusic)
    root.ResumeButton.grid(row=1,column=1,padx=20,pady=20)
    root.ResumeButton.grid_remove()

    root.unmutebutton = Button(root,text='UnMute  ',width=100,bg='yellow',activebackground='purple4',
                             bd=5,image=imunmute,compound=RIGHT,command=unmutemusic)
    root.unmutebutton.grid(row=3,column=3)
    root.unmutebutton.grid_remove()

    root.mutebutton = Button(root,text='Mute  ',width=100,bg='yellow',activebackground='purple4',
                             bd=5,image=immute,compound=RIGHT,command=mutemusic)
    root.mutebutton.grid(row=3,column=3)
    root.mutebutton.grid_remove()
    
    StopButton = Button(root,text='Stop  ',bg='red',font=('aerial', 13 ,'italic bold'),
                        width=200,bd=5,activebackground='purple4',image=imstop,compound=RIGHT,command=stopmusic)
    StopButton.grid(row=2,column=0,padx=20,pady=20)
    
    VolumeUpButton = Button(root,text='VolumeUp  ',bg='peach puff',font=('aerial', 13 ,'italic bold'),
                            width=200,bd=5,activebackground='purple4',image=imvolumeup,compound=RIGHT,command=volumeup)
    VolumeUpButton.grid(row=1,column=2,padx=20,pady=20)
    
    VolumeDownButton = Button(root,text='VolumeDown  ',bg='thistle1',font=('aerial', 13 ,'italic bold'),
                              width=200,bd=5,activebackground='purple4',image=imvolumeudown,compound=RIGHT,command=volumedown)
    VolumeDownButton.grid(row=2,column=2,padx=20,pady=20)
    

    ProgressbarLabel = Label(root,text='',bg='red')
    ProgressbarLabel.grid(row=0,column=3,rowspan=3,padx=20,pady=20)
    ProgressbarLabel.grid_remove()
    
    ProgressbarVolume = Progressbar(ProgressbarLabel,orient=VERTICAL,mode='determinate',
                                    value=0,length=190)
    ProgressbarVolume.grid(row=0,column=0,ipadx=5)

    ProgressbarVolumeLabel = Label(ProgressbarLabel,text='0%',bg='lightgrey',width=3)                                
    ProgressbarVolumeLabel.grid(row=0,column=0)
    

    ProgressbarMusicLabel = Label(root,text='',bg='red')
    ProgressbarMusicLabel.grid(row=3,column=0,columnspan=3,padx=20,pady=20)
    ProgressbarMusicLabel.grid_remove()

    ProgressbarMusicStarTimeLabel = Label(ProgressbarMusicLabel,text='0:00:0',bg='red',width=6)
    ProgressbarMusicStarTimeLabel.grid(row=0,column=0)

    ProgressbarMusic = Progressbar(ProgressbarMusicLabel,orient=HORIZONTAL,mode='determinate',value=0)
    ProgressbarMusic.grid(row=0,column=1,ipadx=370,ipady=3)

    ProgressbarMusicEndTimeLabel = Label(ProgressbarMusicLabel,text='0:00:0',bg='red')
    ProgressbarMusicEndTimeLabel.grid(row=0,column=2)


from tkinter import *
from tkinter import filedialog
from pygame import mixer
from tkinter.ttk import Progressbar
import datetime
from mutagen.mp3 import MP3


root = Tk()
root.geometry('1100x350+200+180')
root.title('Music Player')
root.iconbitmap('Music.ico')
root.resizable(False,False)
root.configure(bg = 'lightskyblue')


audiotrack = StringVar()
currentvol = 0
totalsonglength = 0
count = 0
text = ''

mixer.init()
createwidthes()
root.mainloop()
