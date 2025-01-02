import ffmpeg


input_video = './Data/video2.mp4'


output_audio = './Data/audio3.wav'


ffmpeg.input(input_video).output(output_audio).run()
