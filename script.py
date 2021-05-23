# ******** Author - Asif Ali Mehmuda (aliasif1)*******************
# This script returns the average transcdoing time (decoding time + Encoding time) for a number of video segments for various hevc params
# input - target resolution 
# input - number of video segments to consider
# output - result.csv file with average transcdoing time for various HEVC params 

#Requirements 
#Input videos stored in /Input folder
#Transcoded segments go to Output/ folder

import subprocess
import argparse
import os
import time

def ffmpegTranscode(segments):
    for case in commands:
            print('Working on case {}'.format(case['id']))
            time_arr = []
            for segment in segments:
                cmd = case['cmd']
                cmd = cmd.replace('<input>', 'Input/' + segment)
                cmd = cmd.replace('<target>', targetResolution) 
                removeFile()
                start_time = time.time()
                subprocess.call(cmd,shell=True)
                end_time = time.time()
                seconds_elapsed = end_time - start_time
                time_arr.append(seconds_elapsed)
            average_time = sum(time_arr) / len(time_arr)
            writeResult(case['id'],case['cmd'],average_time)
    

def writeResult(id, title, duration):
    with open('result.csv', 'a') as csvfile:
        csvfile.write('{},{},{}\n'.format(id,title,duration))
    
def removeFile():
    filePath = "Output/out.mp4"
    if os.path.exists(filePath):
        os.remove(filePath)

def getVideoList(lastIndex):
    filePath = "Input/"
    segments = sorted(list(os.listdir(filePath)))
    segments = segments[0:lastIndex]
    return segments

parser = argparse.ArgumentParser(description='HEVC params Profiling')
parser.add_argument('target', help='Target Resolution')
parser.add_argument('--num', type=int, default=10, help='Number of segmnets to consider')
args = parser.parse_args()

#global variable 
targetResolution = args.target
stopIndex = args.num
commands = [
    {
        'id': 1,
        'cmd': 'ffmpeg -loglevel error -i <input> -c:v libx265 -x265-params crf=28 -vf scale=<target> -c:a copy Output/out.mp4'
    },
    {
        'id': 2,
        'cmd': 'ffmpeg -loglevel error -i <input> -c:v libx265 -preset ultrafast -x265-params crf=28 -vf scale=<target> -c:a copy Output/out.mp4'
    },
    {
        'id': 3,
        'cmd': 'ffmpeg -loglevel error -i <input> -c:v libx265 -preset ultrafast -x265-params frame-threads=1:pools="none":crf=28 -vf scale=<target> -c:a copy Output/out.mp4'
    },
    {
        'id': 4,
        'cmd': 'ffmpeg -loglevel error -i <input> -c:v libx265 -preset ultrafast -x265-params frame-threads=0:pools="*":crf=28 -vf scale=<target> -c:a copy Output/out.mp4'
    },
    {
        'id': 5,
        'cmd': 'ffmpeg -loglevel error -i <input> -c:v libx265 -preset ultrafast -x265-params frame-threads=0:pools="none":crf=28 -vf scale=<target> -c:a copy Output/out.mp4'
    },
    {
        'id': 6,
        'cmd': 'ffmpeg -loglevel error -i <input> -c:v libx265 -preset ultrafast -x265-params frame-threads=1:pools="*":crf=28 -vf scale=<target> -c:a copy Output/out.mp4'
    },
    {
        'id': 7,
        'cmd': 'ffmpeg -loglevel error -i <input> -c:v libx265 -preset ultrafast -x265-params frame-threads=1:pools="*":lookahead-slices=0:crf=28 -vf scale=<target> -c:a copy Output/out.mp4'
    },
    {
        'id': 8,
        'cmd': 'ffmpeg -loglevel error -i <input> -c:v libx265 -preset ultrafast -x265-params frame-threads=1:pools="*":wpp=0:crf=28 -vf scale=<target> -c:a copy Output/out.mp4'
    },
    {
        'id': 9,
        'cmd': 'ffmpeg -loglevel error -i <input> -c:v libx265 -preset ultrafast -x265-params frame-threads=0:pools="*":lookahead-slices=0:crf=28 -vf scale=<target> -c:a copy Output/out.mp4'
    },
    {
        'id': 10,
        'cmd': 'ffmpeg -loglevel error -i <input> -c:v libx265 -preset ultrafast -x265-params frame-threads=1:pools="*":slices=2:crf=28 -vf scale=<target> -c:a copy Output/out.mp4'
    },
    {
        'id': 11,
        'cmd': 'ffmpeg -loglevel error -i <input> -c:v libx265 -preset ultrafast -x265-params frame-threads=0:pools="*":slices=2:crf=28 -vf scale=<target> -c:a copy Output/out.mp4'
    },
    {
        'id': 12,
        'cmd': 'ffmpeg -loglevel error -i <input> -c:v libx265 -preset ultrafast -x265-params frame-threads=1:pools="*":lookahead-slices=0:slices=2:crf=28 -vf scale=<target> -c:a copy Output/out.mp4'
    },
    {
        'id': 13,
        'cmd': 'ffmpeg -loglevel error -i <input> -c:v libx265 -preset ultrafast -x265-params frame-threads=0:pools="+,-":crf=28 -vf scale=<target> -c:a copy Output/out.mp4'
    }
]

#add a new results file
writeResult('id', 'command', 'duration')

#get the segment list 
segments = getVideoList(stopIndex)

ffmpegTranscode(segments)



    
