import os, subprocess, time

from weather import weather_api
from news import news_api
from cricket import cricket_api
from yowsup.layers                                     import YowLayer
from yowsup.layers.interface                           import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities  import TextMessageProtocolEntity
from yowsup.layers.protocol_receipts.protocolentities  import OutgoingReceiptProtocolEntity
from yowsup.layers.protocol_acks.protocolentities      import OutgoingAckProtocolEntity
from xkcd_fetch import xkcd_api
from cyhap import cyhap_api
from peanuts import peanuts_api
from calvin import calvin_api
from cafeteria import cafeteria_api
from youtubedownloader import song_api

song=song_api()
w=weather_api()
n=news_api()
c=cricket_api()
x=xkcd_api()
ch = cyhap_api()
ca = calvin_api()
pn = peanuts_api()
cafe=cafeteria_api()

class EchoLayer(YowInterfaceLayer):
    prev_msg=''

    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):
        state = False

        if True:
            receipt = OutgoingReceiptProtocolEntity(messageProtocolEntity.getId(), messageProtocolEntity.getFrom(), 'read', messageProtocolEntity.getParticipant())
            t = messageProtocolEntity.getBody().lower();
            temp=t.split(' ')
            print "New Message Received from ", messageProtocolEntity.getFrom()

            if('song' in t):
                state=True
                t1=''
                for i in xrange(1,len(temp)-1):
                    t1=t1+temp[i]+' '
                t1=t1+temp[-1]
                print t1
                r = song.download(t1,'3gp','./videosongs/')
                if r != 0:
                    outgoingMessageProtocolEntity = TextMessageProtocolEntity(
                    "Oops. The song could not be located",
                    to = messageProtocolEntity.getFrom())
                    self.toLower(receipt)
                    self.toLower(outgoingMessageProtocolEntity)
                    self.prev_msg=messageProtocolEntity.getBody()

                song.send_song(messageProtocolEntity.getFrom().split('@')[0])

            if('cafe' in t):
                state=True
                menus=cafe.get_menus()
                outgoingMessageProtocolEntity = TextMessageProtocolEntity(
                    menus,
                    to = messageProtocolEntity.getFrom())  
                self.toLower(receipt)
                self.toLower(outgoingMessageProtocolEntity)
                self.prev_msg=messageProtocolEntity.getBody()

            if(temp[0].lower()=='news'):
                state = True
                if(len(temp)==1):
                    outgoingMessageProtocolEntity = TextMessageProtocolEntity(
                    "Usage: \nnews {keyword}",
                    to = messageProtocolEntity.getFrom())
                
                else:      
                    t1=''
                    for i in xrange(1,len(temp)-1):
                        t1=t1+temp[i]+' '
                    t1=t1+temp[-1]
                    print t1
                    temp1=unicode(n.get_news(t1)).encode(encoding='utf-8')
                    outgoingMessageProtocolEntity = TextMessageProtocolEntity(
                    temp1,
                    to = messageProtocolEntity.getFrom())  
                self.toLower(receipt)
                self.toLower(outgoingMessageProtocolEntity)
                self.prev_msg=messageProtocolEntity.getBody()

            if(temp[0].lower()=='weather'):
                state=True
                if(len(temp)==1):
                    outgoingMessageProtocolEntity = TextMessageProtocolEntity(
                    "Usage: \nweather {city_name}",
                    to = messageProtocolEntity.getFrom())
                else:      
                    t1=''
                    for i in xrange(1,len(temp)-1):
                        t1=t1+temp[i]+' '
                    t1=t1+temp[-1]
                    print t1
                    outgoingMessageProtocolEntity = TextMessageProtocolEntity(
                    w.get_weather(t1),
                    to = messageProtocolEntity.getFrom())  
                self.toLower(receipt)
                self.toLower(outgoingMessageProtocolEntity)
                self.prev_msg=messageProtocolEntity.getBody()

            if(temp[0].lower()=='cricket' or self.prev_msg.lower()=='cricket'):
                state = True
                try:
                    int(messageProtocolEntity.getBody())
                    data=c.get_single_score(int(messageProtocolEntity.getBody()))
                    outgoingMessageProtocolEntity = TextMessageProtocolEntity(
                    data,
                    to = messageProtocolEntity.getFrom())
                    self.toLower(receipt)
                    self.toLower(outgoingMessageProtocolEntity)
                    self.prev_msg=messageProtocolEntity.getBody()
                except Exception as e:
                    print e
                    data=c.get_all_score()+"\n"+"Enter your choice:"
                    outgoingMessageProtocolEntity = TextMessageProtocolEntity(
                        data,
                        to = messageProtocolEntity.getFrom())
                    self.toLower(receipt)
                    self.toLower(outgoingMessageProtocolEntity)
                    self.prev_msg=messageProtocolEntity.getBody()

            if('xkcd' in t):
                state = True
                x.get_xkcd(messageProtocolEntity.getFrom())
                print "API returned"

            if('cyhap' in t or 'cyanide' in t):
                state = True
                ch.get_cyhap(messageProtocolEntity.getFrom())
                print "API returned"

            if('calvin' in t or 'hobbes' in t):
                state = True
                ca.get_calvin(messageProtocolEntity.getFrom())
                print "API returned"

            if('peanuts' in t):
                state = True
                pn.get_peanuts(messageProtocolEntity.getFrom())
                print "API returned"

            if state == False:  
                outgoingMessageProtocolEntity = TextMessageProtocolEntity(
                    messageProtocolEntity.getBody(),
                    to = messageProtocolEntity.getFrom())
                self.toLower(receipt)
                self.toLower(outgoingMessageProtocolEntity)
                self.prev_msg=messageProtocolEntity.getBody()
            

    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        ack = OutgoingAckProtocolEntity(entity.getId(), "receipt", entity.getType(), entity.getFrom())
        self.toLower(ack)