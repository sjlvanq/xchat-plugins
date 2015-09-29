#-*- coding: utf-8 -*-
__module_name__ = "asciihuayra" 
__module_version__ = "0.1" 
__module_description__ = "Ascii Art de vacas y panaderos" 
 
import xchat
print "ASCII-HUAYRA cargado! no abuse del mismo o será expulsado del canal"

def error():
	print ":/ Ocurrió un error con el plugin ASCII-HUAYRA"

def dispatch(argv, arg_to_eol, c):
	if len(argv) == 1:
		return xchat.EAT_XCHAT
	try:
		destination = xchat.get_context()
		#print destination
		for line in ascii[argv[1]]:
			destination.command("me "+line)
	except:
		error()
	return xchat.EAT_XCHAT

def unload_ah(userdata): 
    xchat.command("MENU DEL Huayra") 

ascii= {}
ascii["panadero1"]	=["  \\'/,"," - @ --   Huayra GNU/Linux"]
ascii["panadero2"]	=[" _\\!/_    Huayra GNU/Linux"]
ascii["netbook"]	=["  __"," |__|"," \\__\\~D"]
ascii["vaquita"]	=["     (_)","  /---V"," * |--|"]
ascii["inexpresiva"]=["   (__)","   (oo)","    \\/"]
ascii["hipnotizada"]=["   (__)","   (@@)","    \\/"]
ascii["muerta"]		=["   (__)","   (##)","    \\/"]
ascii["sarcastica"]	=["   (__)","   (~~)","    \\/"]
ascii["incredula"]	=["   (__)","   (Oo)","    \\/"]
ascii["furiosa"]	=["   (__)","   (\\/)","    \\/"]
ascii["ambiciosa"]	=["   (__)","   ($$)","    \\/"]
ascii["aburrida"]	=["   (__)","   (--)","    \\/"]
ascii["guerrilla"]	=["   (__)","   (oo)","  / \\/ \\"," D===b=-----"]
ascii["flaca"]		=[" _(~)_","  )\"("," (@_@)","  ) (  autor:hjw"]
ascii["rellenita"]	=["  _ (.\".) _"," '-'/. .\\'-'","   ( o o )","    `\"-\"`   autor:jgs"]

xchat.command("MENU -p5 ADD Huayra")
xchat.command("MENU ADD Huayra/AsciiArt")
xchat.command("MENU ADD Huayra/AsciiArt/Panadero1 \".asciihuayra panadero1\"")
xchat.command("MENU ADD Huayra/AsciiArt/Panadero2 \".asciihuayra panadero2\"")
xchat.command("MENU ADD Huayra/AsciiArt/Netbook \".asciihuayra netbook\"")
xchat.command("MENU ADD Huayra/AsciiArt/Vaquita \".asciihuayra vaquita\"")
xchat.command("MENU ADD Huayra/AsciiArt/Emotica")
xchat.command("MENU ADD Huayra/AsciiArt/Emotica/Inexpresiva \".asciihuayra inexpresiva\"")
xchat.command("MENU ADD Huayra/AsciiArt/Emotica/Hipnotizada \".asciihuayra hipnotizada\"")
xchat.command("MENU ADD Huayra/AsciiArt/Emotica/Muerta \".asciihuayra muerta\"")
xchat.command("MENU ADD Huayra/AsciiArt/Emotica/Sarcástica \".asciihuayra sarcastica\"")
xchat.command("MENU ADD Huayra/AsciiArt/Emotica/Incredula \".asciihuayra incredula\"")
xchat.command("MENU ADD Huayra/AsciiArt/Emotica/Furiosa \".asciihuayra furiosa\"")
xchat.command("MENU ADD Huayra/AsciiArt/Emotica/Ambiciosa \".asciihuayra ambiciosa\"")
xchat.command("MENU ADD Huayra/AsciiArt/Emotica/Aburrida \".asciihuayra aburrida\"")
xchat.command("MENU ADD Huayra/AsciiArt/Emotica/Guerrilla \".asciihuayra guerrilla\"")
xchat.command("MENU ADD Huayra/AsciiArt/Emotica/Estilizadas")
xchat.command("MENU ADD Huayra/AsciiArt/Emotica/Estilizadas/Flaca \".asciihuayra flaca\"")
xchat.command("MENU ADD Huayra/AsciiArt/Emotica/Estilizadas/Rellenita \".asciihuayra rellenita\"")

__unhook__ = xchat.hook_command(".asciihuayra",dispatch,help="Ascii Art de vacas y panaderos.")

xchat.hook_unload(unload_ah)
