from gtts import gTTS  #  convert the text to mp3 audio
s = input("Enter the File name: ") # enter the txt file name
f = open(s)
text = f.read()
obj = gTTS(text= text, lang= 'ru' ,slow= False) 
f1 = input("Enter the Audio name to be saved : ")  # enter the audio file name that will be auto generated.
obj.save(f1)  # audio file will auto saved in the same directory