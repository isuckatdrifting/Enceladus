# Enceladus
Get NetEase music lyrics with Python3

Usage: `lyric.py [-h] id format`
positional arguments:
  id          id of the music
  format      choose the format of the output: orig/trans/merge

optional arguments:
  -h, --help  show this help message and exit

orig: original lyrics
trans: translated lyrics
merge: lyrics in "[original]/[translated]" type

---

For example: `python3 lyric.py 533943763 merge`

This would generate a txt lyric that meets the `lrc` file standard under the script executing folder.
You may change the extension from `*.txt` to `*.lrc` manually if you wanna import it in other apps.

If this program helps with your MAD/AMV production, please do not hesitate to give me stars. :smile:

<p align="center">
  <img src="https://github.com/GeraltShi/Enceladus/blob/master/snapshot.png" width="550" alt="snapshot">
</p>