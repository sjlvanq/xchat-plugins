#-*- coding: utf-8 -*-
__module_name__ = "RSS Foros de Huayra GNU/Linux" 
__module_version__ = "0.1"
__module_description__ = "Comunica en el canal IRC #huayragnulinux de Freenode la publicación de nuevos posts en los foros de Huayra GNU/Linux (oficial y comunidad de usuarios)" 

import xchat
import feedparser
import time

print __module_name__+"| Cargado! "

#ToDo: Manejo de errores!

interval = 30000

class rss_notificador:
    def __init__(self, feed_url, channel="#huayragnulinux"):
        self.feed_url = feed_url
        self.channel = channel
        self.last_entry_published = None
        self.update()
    def update(self):
        try:
            parsed_rss = feedparser.parse(self.feed_url)
            if parsed_rss.entries == []: exit()
            if self.last_entry_published == None:
                self.last_entry_published = parsed_rss.entries[0].published_parsed
            cntx_channel = xchat.find_context(channel=self.channel)
            #ToDo: if cntx_channel == None: #/server?; /join.......
            i=0
            while parsed_rss.entries[i].published_parsed > self.last_entry_published:
                cntx_channel.command("say "+parsed_rss.feed.title+" | Nuevo mensaje ["+parsed_rss.entries[i].published+"] | "+parsed_rss.entries[i].title+" ("+parsed_rss.entries[i].link+")")
                i+=1
            self.last_entry_published = parsed_rss.entries[0].published_parsed
        except:
            exit()

#Unload Callback
def unload_cb(arg):
    global myhook 
    if myhook is not None: 
        xchat.unhook(myhook) 
        myhook = None
 
#Interval Callback
def interval_cb(arg):
    global notificadores
    for n in notificadores:
        n.update()
    return 1

notificadores = [
rss_notificador('http://huayra.conectarigualdad.gob.ar/foro/index.php?action=.xml;sa=recent;type=rss',"#huayragnulinux"),
rss_notificador('http://foros.comunidadhuayra.org/index.php?action=.xml;sa=recent;type=rss',"#huayragnulinux")
]

myhook = xchat.hook_timer(interval, interval_cb)
xchat.hook_unload(unload_cb)

