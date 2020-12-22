# -*- coding: utf-8 -*-# 
# filename: handle.py
import hashlib
import reply
import receive
import web
class Handle(object):
    def POST(self):
        try:
            webData = web.data()
            webData = webData.decode()
            print("Handle Post webdata is ", webData)
            #后台打日志
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg):
                fromUser = recMsg.FromUserName
                toUser = recMsg.ToUserName
                textContent = recMsg.Content
                textContent = textContent.decode()
                if recMsg.MsgType == 'text':
                    if fromUser == 'oi8ob1S7zabQTx3LJUk6FUUtJCj4':
                        replyMsg = reply.PunchTheClock(fromUser, toUser, textContent)
                    else:
                        content = "http://www.kareza.cn/jetbrain-activate-code.html"
                        replyMsg = reply.TextMsg(fromUser, toUser, content)
                    return replyMsg.send()
                if recMsg.MsgType == 'image':
                    mediaId = recMsg.MediaId
                    replyMsg = reply.ImageMsg(fromUser, toUser, mediaId)
                    return replyMsg.send()
                else:
                    return reply.Msg().send()
            else:
                print("暂且不处理")
                return "success"
        except(Exception) as Argment:
            return Argment
