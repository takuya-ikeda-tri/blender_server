import os

for k in range(3):
    os.system("ffmpeg -y -r 20 -i /tmp/manipulation_station_ycb/%02d_%08d.jpg manipulation_station_ycb_render_realtime_%02d.mp4" % (k, k))

#for k in range(25):
#    os.system("ffmpeg -y -r 30 -i /tmp/ycb_scene_%03d/00_%%8d.jpg /tmp/ycb_scene_%03d/render_halftime.mp4" % (k, k))
#    os.system("ffmpeg -y -r 60 -i /tmp/ycb_scene_%03d/00_%%8d.jpg /tmp/ycb_scene_%03d/render_realtime.mp4" % (k, k))
