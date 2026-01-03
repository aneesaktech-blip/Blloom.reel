from moviepy.editor import *

W, H = 1080, 1920

bg = ColorClip((W, H), color=(0, 0, 0), duration=10)

lines = open("text.txt").read().strip().split("\n")

clips = []
t = 0

for line in lines[:-2]:
    txt = TextClip(
        line,
        fontsize=60,
        color="white",
        method="caption",
        size=(900, None)
    ).set_position("center").set_start(t).set_duration(2).fadein(0.5).fadeout(0.5)
    clips.append(txt)
    t += 2

hoodie = (
    ImageClip("hoodie.jpg")
    .resize(width=900)
    .set_position("center")
    .set_start(t)
    .set_duration(2)
    .fadein(0.5)
)
clips.append(hoodie)
t += 2

brand = TextClip(
    "BLLOOM\nwear your silence.",
    fontsize=72,
    align="center",
    color="white"
).set_position("center").set_start(t).set_duration(2)

final = CompositeVideoClip([bg] + clips, size=(W, H))
final.write_videofile("blloom_reel.mp4", fps=30, codec="libx264", audio=False)
