import mildom_comment_viewer
import sys

room_id = input("ルームIDを入力してください: ")

mcv = mildom_comment_viewer.MildomCommentViewer(room_id)
mcv.start()