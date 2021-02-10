import websocket
import json
import time
import _thread
import datetime
import os

class MildomCommentViewer:
    
    def __init__(self, room_id):
        self.room_id = room_id
        self.web_socket_url = "wss://jp-room1.mildom.com/?roomId=" + room_id
        self.my_info_json = r'{"userId":0,"level":1,"userName":"guest125565","guestId":"pc-gp-aaaaaa-1111-1111-1111-aaaaaaaaaaaa","nonopara":"fr=web`sfr=pc`devi=Windows 10 64-bit`la=ja`gid=pc-gp-aaaaaaaa-0000-0000-0000-000000000000`na=Japan`loc=Japan|Tokyo`clu=aws_japan`wh=100*1000`rtm=2020-05-26T09:59:05.363Z`ua=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Mobile Safari/537.36`aid=' + room_id + r'`live_type=2`live_subtype=2`game_key=Minecraft_DUNGEONS`game_type=pc`host_official_type=official_game`isHomePage=false","roomId":' + room_id + r',"cmd":"enterRoom","reConnect":0,"nobleLevel":0,"avatarDecortaion":0,"enterroomEffect":0,"nobleClose":0,"nobleSeatClose":0,"invisible":1,"reqId":1}'
        self.today = (datetime.date.today()).strftime('%Y%m%d')
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.out_path = self.base_dir + '\chatdata\chatdata_' + self.room_id + '_' + self.today + '.log'

    def start(self):
        def on_message(socket, message):
            comment = json.loads(message)
            time = int(comment['time'])
            user_name = comment['userName']
            msg = comment['msg']
            if comment['cmd'] == 'onChat':
                f = open(self.out_path, 'a')
                print('{},{},{}'.format(datetime.datetime.fromtimestamp(time/1000), user_name, msg))
                print('{},{},{}'.format(datetime.datetime.fromtimestamp(time/1000), user_name, msg), file=f)
                f.close()

        def on_open(socket):
            def run(*args):
                socket.send(self.my_info_json)
            _thread.start_new_thread(run, ())

        websocket.enableTrace(False)
        socket = websocket.WebSocketApp(
            self.web_socket_url,
            on_message = on_message,
        )

        socket.on_open = on_open
        socket.run_forever()