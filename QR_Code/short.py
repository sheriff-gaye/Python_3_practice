
import pyshorteners

link="https://www.facebook.com/107322065361688/posts/pfbid0VRWb1xw3oYtdTHd12odtB18BtFG8VSatTwuz8g2LkNebmTUxB7srt2eGC5z6CT2vl/?d=n"

shot=pyshorteners.Shortener()
res=shot.tinyurl.short(link)

print(res)