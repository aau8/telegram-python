from pydub import AudioSegment

audio = AudioSegment.from_file('./music/music_1.mp3', 'mp3')

audio = audio[:1000]
audio.export('music_1.mp3', format='mp3')