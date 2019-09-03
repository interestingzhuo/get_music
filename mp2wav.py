from pydub import AudioSegment
import os 
 
def trans_mp3_to_wav(filepath):
    try:
       song = AudioSegment.from_mp3(filepath)
       song.export('./wav/'+filepath.split('/')[-1][:-3]+'wav', format="wav")
    except:
        print(filepath)
if __name__=='__main__':
    dirname='./music/'
    files=os.listdir(dirname)
    for fil in files:
        trans_mp3_to_wav(dirname+fil)
