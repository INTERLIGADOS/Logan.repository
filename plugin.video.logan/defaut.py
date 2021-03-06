#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


##############BIBLIOTECAS A IMPORTAR E DEFINICOES####################

import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmc,xbmcaddon,HTMLParser,base64,xmltosrt,os
from BeautifulSoup import BeautifulSoup
h = HTMLParser.HTMLParser()


versao = '1.1.9'
addon_id = 'plugin.video.logan'
selfAddon = xbmcaddon.Addon(id=addon_id)
addonfolder = selfAddon.getAddonInfo('path')
artfolder = addonfolder + '/resources/img/'
fanart = addonfolder + '/fanart.png'
 

###################################################MENUS############################################

	
def  menus():        		
	dialog = xbmcgui.Dialog()
	addDir('TV Online','-',13,'http://i.imgur.com/y22MB94.jpg')
	addDir('Armagedon','-',19,'http://3.bp.blogspot.com/-PCiABMvpL1E/UDkAFJGmekI/AAAAAAAAADk/D0ZEDxCY0Ck/s1600/188103_197123240344214_819072657_n.jpg')
	addDir('Megafilmes','-',23,'http://i.imgur.com/y22MB94.jpg')
	
	
	

def  categorias():
	addDir('Tv Aberta','https://copy.com/Nlyj6xxWlRFKdinh?download=1',16,'https://copy.com/JvvK4Iw39ofK1rPF')
	addDir('FUTEBOL AO VIVO','https://copy.com/xUo6eMRYOiVevL2h?download=1',16,'https://copy.com/NPRaZORymdG0FxJ1')
	addDir('TV PAGA BRASIL','-',15,'https://copy.com/VVF8ouCl1Ghkjum8')
	addDir('STREAMS DO YOUTUBE','https://copy.com/8QZD9AQuv4Lchd2M?download=1',17,'http://i.imgur.com/fKCIAxx.jpg')
	addDir('SÉRIES E DESENHOS 24 HORAS','https://copy.com/nEagWXhOC1s7dlyO?download=1',16,'https://copy.com/SzKOJlBKxIfEuHnp')
	addDir('CANAIS LATINOS','https://copy.com/tapliy8nIaKSLDQq?download=1',16,'https://copy.com/wPVtPygtxuY0P1xl')
	addDir('CANAIS DE PORTUGAL','https://copy.com/unoGFK2bL8ZJ0iHD?download=1',16,'https://copy.com/HwP6Xpia6GNQvWsi')
	addDir('WEBCAMS','https://copy.com/Ywh4MnZQqy2R7M8P?download=1',16,'https://copy.com/dPj2J9AzaExumsnE')
	addDir('CANAIS HD','https://copy.com/VMoOgU8UDvAgfjv0?download=1',16,'https://copy.com/WB68NrrmvjxdH1pJ')
	addDir('MÚSICAS E VIDEOCLIPES','https://copy.com/1cvRyOdMSOCSBH70?download=1',16,'https://copy.com/stpjErgehf9hPtwW')
	addDir('ESPORTES INTERNACIONAIS','https://copy.com/bIIpBHwFbXMXOBBB?download=1',16,'https://copy.com/pUGvpVMDpoY09PcA')
	addDir('RÁDIOS','https://copy.com/znUclLey0qF30gSd?download=1',16,'https://copy.com/fuDnLrM1Am7VNtmT')
	
	


def  categorias_tv_paga_brasil():
	addDir('DOCUMENTÁRIOS','https://copy.com/u3fZuJaCSqXQUNuk?download=1',16,'https://copy.com/9KLabSgitalsvYkg')
	addDir('ESPORTES','https://copy.com/342Ys8apG9i2Ar9J?download=1',16,'https://copy.com/qJfijQo0kIyxhgsc')	
	addDir('FILMES E SÉRIES','https://copy.com/qaC2wr0YHQ3cWgN3?download=1',16,'https://copy.com/9b1kFz9GVNs2CVEg')
	addDir('INFANTIL','https://copy.com/FH28QXuLwrJY9cXS?download=1',16,'https://copy.com/AAJrU1yDtryoKeqt')	
	addDir('NOTÍCIAS','https://copy.com/r19WdvfFW4xP7h7Q?download=1',16,'https://copy.com/9wy1vGvZAAbP2Gus')
	addDir('RELIGIOSOS','https://copy.com/S6Jm2vh2DYJDTEwJ?download=1',16,'https://copy.com/uzJEAXOCWzCUv2up')
	addDir('VARIEDADES','https://copy.com/DUKhtoZqYdjklcOa?download=1',16,'https://copy.com/pqAXz2FWGHwAIAfU')	
	
	##########################################ARMAGEDON#########################################
#FUNCOES
	
	
def CATEGORIES():
	#dialog = xbmcgui.Dialog()
	#dialog.ok("Atualizado", "Addon atualizado por gutoakashi1.\nFaça sua doação para manter o addon sempre atualizado. Mande um email para akx.kodi@bol.com.br para mais informações")
	#dialog = xbmcgui.Dialog()
	#dialog.ok("Doações", "Quem fizer a doação mandarei por email o addon atualizado do cinefilmeshd e do megafilmesonline(em breve).\nMande um email para akx.kodi@bol.com.br")
	addDir('Categorias','-',21,artfolder + 'categorias.jpg')
	addDir('Lançamentos','http://www.armagedomfilmes.biz/?cat=3236',2,artfolder + 'lancamentos.jpg')
	addDir('Séries','http://www.armagedomfilmes.biz/?cat=21|1',6,artfolder + 'series.jpg')
	addDir('Pesquisar Filmes','-',3,artfolder + 'pesquisa.jpg')
	addDir('Pesquisar Series','-',8,artfolder + 'pesquisa.jpg')	
	
def categorias_Armagedon():
	addDir('BLURAY','http://www.armagedomfilmes.biz/?cat=5529',2,artfolder + 'bluray.jpg')
	addDir('LEGENDADOS','http://www.armagedomfilmes.biz/?s=legendado',2,artfolder + 'legendados.jpg')
	addDir('ANIMES','http://www.armagedomfilmes.biz/?cat=36',9,artfolder + 'animes.jpg')
	addDir('ACAO','http://www.armagedomfilmes.biz/?cat=3227',2,artfolder + 'acao.jpg')
	addDir('ANIMACAO','http://www.armagedomfilmes.biz/?cat=3228',2,artfolder + 'animacao.jpg')
	addDir('AVENTURA','http://www.armagedomfilmes.biz/?cat=3230',2,artfolder + 'aventura.jpg')
	addDir('COMEDIA ','http://www.armagedomfilmes.biz/?cat=3229',2,artfolder + 'comedia.jpg')
	addDir('COMEDIA ROMANTICA','http://www.armagedomfilmes.biz/?cat=3231',2,artfolder + 'comediaro.jpg')
	addDir('DRAMA','http://www.armagedomfilmes.biz/?cat=3233',2,artfolder + 'drama.jpg')
	addDir('FAROESTE','http://www.armagedomfilmes.biz/?cat=18',2,artfolder + 'faroeste.jpg')
	addDir('FICCAO CIENTIFICA','http://www.armagedomfilmes.biz/?cat=3235',2,artfolder + 'ficcao.jpg')
	addDir('LUTAS UFC','http://www.armagedomfilmes.biz/?cat=3394',2,artfolder + 'lutas.jpg')
	addDir('NACIONAL','http://www.armagedomfilmes.biz/?cat=3226',2,artfolder + 'nacional.jpg')
	addDir('POLICIAL','http://www.armagedomfilmes.biz/?cat=72',2,artfolder + 'policial.jpg')
	addDir('RELIGIOSO','http://www.armagedomfilmes.biz/?cat=20',2,artfolder + 'religioso.jpg')
	addDir('ROMANCE','http://www.armagedomfilmes.biz/?cat=3232',2,artfolder + 'romance.jpg')
	addDir('SHOWS','http://www.armagedomfilmes.biz/?cat=30',2,artfolder + 'shows.jpg')
	addDir('SUSPENSE','http://www.armagedomfilmes.biz/?cat=3239',2,artfolder + 'suspense.jpg')
	addDir('TERROR','http://www.armagedomfilmes.biz/?cat=3238',2,artfolder + 'terror.jpg')
	addDir('THRILLER','http://www.armagedomfilmes.biz/?cat=30',2,artfolder + 'thr.jpg')
	
def categorias_2():
	
	addDir('Categorias2','-',24,artfolder + 'categorias.jpg')
	addDir('Lançamentos','http://www.armagedomfilmes.biz/?cat=3236',2,artfolder + 'lancamentos.jpg')
	addDir('Séries','http://www.armagedomfilmes.biz/?cat=21|1',6,artfolder + 'series.jpg')
	addDir('Pesquisar Filmes','-',3,artfolder + 'pesquisa.jpg')
	addDir('Pesquisar Series','-',8,artfolder + 'pesquisa.jpg')	
	
def categorias_Armagedon2():
	addDir('BLURAY','http://www.filmesonline2.com/category/animacao-2/',2,artfolder + 'bluray.jpg')
	addDir('LEGENDADOS','http://www.armagedomfilmes.biz/?s=legendado',2,artfolder + 'legendados.jpg')
	
		
	
def listar_videos(url):
	codigo_fonte = abrir_url(url)
	soup = BeautifulSoup(abrir_url(url))
	content = BeautifulSoup(soup.find("div", { "class" : "bic-miniaturas" }).prettify())
	filmes = content("div", { "class" : "bic-miniatura" })
	for filme in filmes:
		titulo = filme.a["title"].replace('Assistir ','')
		url = filme.a["href"]
		img = filme.img["src"]
		addDir(titulo.encode('utf8'),url,4,img,False,len(filmes)) 

	pagenavi = BeautifulSoup(soup.find('div', { "class" : "wp-pagenavi" }).prettify())("a", { "class" : "nextpostslink" })[0]["href"]
	addDir('Página Seguinte >>',pagenavi,2,artfolder + 'prox.png')

	xbmcplugin.setContent(int(sys.argv[1]), 'movies')
	xbmc.executebuiltin('Container.SetViewMode(503)')	
	
	
	
	
	
def listar_videos(url):
	codigo_fonte = abrir_url(url)
	soup = BeautifulSoup(abrir_url(url))
	content = BeautifulSoup(soup.find("div", { "class" : "bic-miniaturas" }).prettify())
	filmes = content("div", { "class" : "bic-miniatura" })
	for filme in filmes:
		titulo = filme.a["title"].replace('Assistir ','')
		url = filme.a["href"]
		img = filme.img["src"]
		addDir(titulo.encode('utf8'),url,4,img,False,len(filmes)) 

	pagenavi = BeautifulSoup(soup.find('div', { "class" : "wp-pagenavi" }).prettify())("a", { "class" : "nextpostslink" })[0]["href"]
	addDir('Página Seguinte >>',pagenavi,2,artfolder + 'prox.png')

	xbmcplugin.setContent(int(sys.argv[1]), 'movies')
	xbmc.executebuiltin('Container.SetViewMode(503)')
	
def listar_series(url):
	pagina = str(int(url.split('|')[1])+1)
	url = url.split('|')[0]

	soup = BeautifulSoup(abrir_url(url))
	content = BeautifulSoup(soup.find("div", { "class" : "bic-miniaturas" }).prettify())
	series = content("div", { "class" : "bic-miniatura" })
	codigo_fonte = abrir_url(url)
	
	total = len(series)
	for serie in series:
		titulo = serie.a['title']
		titulo = titulo.replace('&#8211;',"-").replace('&#8217;',"'").replace('Assistir ','')
		try:
			addDir(titulo.encode('utf-8'),serie.a['href'],12,serie.img['src'],True,total)
		except:
			pass

	addDir('Página Seguinte >>','http://www.armagedomfilmes.biz/?cat=21&paged='+pagina+'|'+pagina,6,artfolder + 'prox.png')
	
def listar_animes(url):

	soup = BeautifulSoup(abrir_url(url))
	content = BeautifulSoup(soup.find("div", { "class" : "bic-miniaturas" }).prettify())
	series = content("div", { "class" : "bic-miniatura" })
	codigo_fonte = abrir_url(url)
	
	total = len(series)
	for serie in series:
		titulo = serie.a['title']
		titulo = titulo.replace('&#8211;',"-").replace('&#8217;',"'").replace('Assistir ','')
		try:
			addDir(titulo.encode('utf-8'),serie.a['href'],12,serie.img['src'],True,total)
		except:
			pass
		
	pagenavi = BeautifulSoup(soup.find('div', { "class" : "wp-pagenavi" }).prettify())("a", { "class" : "nextpostslink" })[0]["href"]
	addDir('Página Seguinte >>',pagenavi,2,artfolder + 'prox.png')

	xbmcplugin.setContent(int(sys.argv[1]), 'movies')
	xbmc.executebuiltin('Container.SetViewMode(503)')		
	
	
def listar_temporadas(url):

	codigo_fonte = abrir_url(url)
	soup = BeautifulSoup(abrir_url(url))
	conteudo = BeautifulSoup(soup.find("ul", { "class" : "bp-series" }).prettify())
	temporadas = conteudo("li")
	
	total = len(temporadas)
	i=1
	print total
	
	while i <= total:
		temporada = conteudo("li", { "class" : "serie"+str(i)+"-code"})
		for temp in temporada:
			img = temp.img["src"]
			titulo = str(i)+" temporada"
			try:
				addDir(titulo,url,7,img,True,total)
			except:
				pass
		i=i+1
		
		

def listar_series_f2(name,url):

	n = name.replace(' temporada','')
	
	soup = BeautifulSoup(abrir_url(url))
	content = BeautifulSoup(soup.find("li", { "class" : "serie"+n+"-code" }).prettify())
	episodios = content.findAll("a")
	print episodios[0]
	
	a = [] # url titulo img
	for episodio in episodios:
		try:
			xml = BeautifulSoup(abrir_url(episodio["href"]+'/feed'))
			title = xml.title.string.encode('utf-8').replace('Comentários sobre: Assistir ','')
			try:
				if "html" in os.path.basename(episodio["href"]):
					temp = [episodio["href"],title]
					a.append(temp)
			except:
				pass
		except:
			pass

	total = len(a)
	for url2, titulo, in a:
		titulo = titulo.replace('&#8211;',"-").replace('&#8217;',"'").replace('Assistir ','')
		addDir(titulo,url2,4,'',False,total) 

def obtem_url_dropvideo(url):
	codigo_fonte = abrir_url(url)
	try:
		soup = BeautifulSoup(codigo_fonte)
		lista = soup.findAll('script')
		js = str(lista[9]).replace('<script>',"").replace('</script>',"")
		sUnpacked = jsunpack.unpack(js)
		print sUnpacked
		url_video = re.findall(r'var vurl2="(.*?)";', sUnpacked)
		url_video = str(url_video).replace("['","").replace("']","")
		return [url_video,"-"]
	except:
		pass	
	
def obtem_videobis(url):
	codigo_fonte = abrir_url(url)
	
	try:
		url_video = re.findall(r'file: "(.*?)"',codigo_fonte)[1]
		return [url_video,"-"]
	except:
		return ["-","-"]
		
def obtem_neodrive(url):
	codigo_fonte = abrir_url(url)
	
	try:
		url_video = re.findall(r'vurl.=."(.*?)";',codigo_fonte)[0]
		return [url_video,"-"]
	except:
		return ["-","-"]

def obtem_videopw(url):
	codigo_fonte = abrir_url(url)
	
	try:
		url_video = re.findall(r'var vurl2 = "(.*?)";',codigo_fonte)[0]
		return [url_video,"-"]
	except:
		return ["-","-"]		
	
def obtem_cloudzilla(url):
	codigo_fonte = abrir_url(url)
	
	try:
		url_video = re.findall(r'vurl.=."(.*?)";',codigo_fonte)[0]
		return [url_video,"-"]
	except:
		return ["-","-"]

def player(name,url,iconimage):
	
	try:
		dropvideo = r'src="(.*?dropvideo.*?/embed.*?)"'
		dropmega = r'src=".*?drop.*?id=(.*?)"'
		neodrive = r'src="(.*?neodrive.*?/embed.*?)"'
		neomega = r'src=".*?neodrive.*?id=(.*?)"'
		videobis = r'SRC="(.*?videobis.*?/embed.*?)"'
		videopw = r'src=".*?videopw.*?id=(.*?)"'
		cloudzilla = r'cloudzilla.php.id=(.*?)"'
		cloudzilla_f = r'http://www.cloudzilla.to/share/file/(.*?)"'
		
		mensagemprogresso = xbmcgui.DialogProgress()
		mensagemprogresso.create('ArmagedonFilmes', 'A resolver link','Por favor aguarde...')
		mensagemprogresso.update(33)
		links = []
		hosts = []
		matriz = []
		codigo_fonte = abrir_url(url)
		
		try:
			links.append(re.findall(dropvideo, codigo_fonte)[0])
			hosts.append('Dropvideo')
		except:
			pass
		
		try:
			links.append('http://www.dropvideo.com/embed/'+re.findall(dropmega, codigo_fonte)[0])
			hosts.append('Dropvideo')
		except:
			pass
		
		try:
			links.append('http://videopw.com/e/'+re.findall(videopw, codigo_fonte)[0])
			hosts.append('Videopw')
		except:
			pass
			
		try:
			links.append(re.findall(videobis, codigo_fonte)[0])
			hosts.append('Videobis')
		except:
			pass
		
		try:
			links.append(re.findall(neodrive, codigo_fonte)[0])
			hosts.append('Neodrive')
		except:
			pass
		
		try:
			links.append('http://neodrive.co/embed/'+re.findall(neomega, codigo_fonte)[0])
			hosts.append('Neodrive')
		except:
			pass	
			
		try:
			links.append('http://www.cloudzilla.to/embed/'+re.findall(cloudzilla,codigo_fonte)[0])
			hosts.append('CloudZilla')
		except:
			pass
		
		try:
			links.append('http://www.cloudzilla.to/embed/'+re.findall(cloudzilla_t,codigo_fonte)[0])
			hosts.append('CloudZilla(Legendado)')
		except:
			pass
			
		if not hosts:
			return
		
		index = xbmcgui.Dialog().select('Selecione um dos hosts suportados :', hosts)
		
		if index == -1:
			return
		
		url_video = links[index]
		mensagemprogresso.update(66)
		
		print 'Player url: %s' % url_video
		if 'dropvideo.com/embed' in url_video:
			matriz = obtem_url_dropvideo(url_video)  
		elif 'cloudzilla' in url_video:
			matriz = obtem_cloudzilla(url_video)
		elif 'videobis' in url_video:
			matriz = obtem_videobis(url_video)
		elif 'neodrive' in url_video:
			matriz = obtem_neodrive(url_video)
		elif 'videopw' in url_video:
			matriz = obtem_videopw(url_video)			
		else:
			print "Falha: " + str(url_video)
		print matriz
		url = matriz[0]
		print url
		if url=='-': return
		legendas = matriz[1]
		print "Url do gdrive: " + str(url_video)
		print "Legendas: " + str(legendas)
		
		mensagemprogresso.update(100)
		mensagemprogresso.close()
		
		listitem = xbmcgui.ListItem() # name, iconImage="DefaultVideo.png", thumbnailImage="DefaultVideo.png"
		listitem.setPath(url)
		listitem.setProperty('mimetype','video/mp4')
		listitem.setProperty('IsPlayable', 'true')
		#try:
		xbmcPlayer = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
		xbmcPlayer.play(url)
		if legendas != '-':
			if 'timedtext' in legendas:
				#legenda = xmltosrt.convert(legendas)
				#try:
					import os.path
					sfile = os.path.join(xbmc.translatePath("special://temp"),'sub.srt')
					sfile_xml = os.path.join(xbmc.translatePath("special://temp"),'sub.xml')#timedtext
					sub_file_xml = open(sfile_xml,'w')
					sub_file_xml.write(urllib2.urlopen(legendas).read())
					sub_file_xml.close()
					print "Sfile.srt : " + sfile_xml
					xmltosrt.main(sfile_xml)
					xbmcPlayer.setSubtitles(sfile)
				#except:
				#	pass
			else:
				xbmcPlayer.setSubtitles(legendas)
		#except:
		#	dialog = xbmcgui.Dialog()
		#	dialog.ok(" Erro:", " Impossível abrir vídeo! ")
		#	pass
	except:
		print "erro ao abrir o video"
		print url_video
		pass
	
def pesquisa_filme():
	keyb = xbmc.Keyboard('', 'faca a procura') #Chama o keyboard do XBMC com a frase indicada
	keyb.doModal() #Espera ate que seja confirmada uma determinada string
	if (keyb.isConfirmed()): #Se a entrada estiver confirmada (isto e, se carregar no OK)
		search = keyb.getText() #Variavel search fica definida com o conteudo do formulario
		parametro_pesquisa=urllib.quote(search) #parametro_pesquisa faz o quote da expressao search, isto Ã©, escapa os parametros necessarios para ser incorporado num endereÃ§o url
		url = 'http://www.armagedomfilmes.biz/?s=%s&s-btn=buscar' % str(parametro_pesquisa) #nova definicao de url. str forÃ§a o parametro de pesquisa a ser uma string
		print url
		soup = BeautifulSoup(abrir_url(url))
		content = BeautifulSoup(soup.find("div", { "class" : "bic-miniaturas" }).prettify())
		filmes = content("div", { "class" : "bic-miniatura" })
		print filmes[0]
		for filme in filmes:
			titulo = filme.a["title"].replace('Assistir ','')
			url = filme.a["href"]
			img = filme.img["src"]
			addDir(titulo.encode('utf8'),url,4,img,False,len(filmes))

def pesquisa_serie():
	keyb = xbmc.Keyboard('', 'faca a procura') #Chama o keyboard do XBMC com a frase indicada
	keyb.doModal() #Espera ate que seja confirmada uma determinada string
	if (keyb.isConfirmed()): #Se a entrada estiver confirmada (isto e, se carregar no OK)
		search = keyb.getText() #Variavel search fica definida com o conteudo do formulario
		parametro_pesquisa=urllib.quote(search) #parametro_pesquisa faz o quote da expressao search, isto Ã©, escapa os parametros necessarios para ser incorporado num endereÃ§o url
		url = 'http://www.armagedomfilmes.biz/?s=%s&s-btn=buscar' % str(parametro_pesquisa) #nova definicao de url. str forÃ§a o parametro de pesquisa a ser uma string
		print url
		soup = BeautifulSoup(abrir_url(url))
		content = BeautifulSoup(soup.find("div", { "class" : "bic-miniaturas" }).prettify())
		series = content("div", { "class" : "bic-miniatura" })
		codigo_fonte = abrir_url(url)

		total = len(series)
		for serie in series:
			titulo = serie.a['title']
			titulo = titulo.replace('&#8211;',"-").replace('&#8217;',"'").replace('Assistir ','')
			try:
				addDir(titulo.encode('utf-8'),serie.a['href'],12,serie.img['src'],True,total)
			except:
				pass			
	
		###################################################################################


def abrir_url(url):
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	response = urllib2.urlopen(req)
	link=response.read()
	response.close()
	return link

def addLink(name,url,iconimage):
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
	liz.setProperty('fanart_image', fanart)
	liz.setInfo( type="Video", infoLabels={ "Title": name } )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
	return ok

def addDir(name,url,mode,iconimage,pasta=True,total=1):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setProperty('fanart_image', fanart)
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=pasta,totalItems=total)
	return ok
	
	############Fim armagedon
	
	
###############################################################FKav####################################################
def gethtml(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link = response.read()
    soup = BeautifulSoup(link)
    return soup

def player_youtube(url):
    #mera correção feita por Cleiton Leonel Creton!!!
	xbmcPlayer = xbmc.Player()
        xbmcPlayer.play('plugin://plugin.video.youtube/play/?video_id=' +url)
		
def listar_videostxt(url):
      for line in urllib2.urlopen(url).readlines():
            params = line.split(',')
            try:
                  nome = params[0]
                  print 'Nome: ' + nome
                  img = params[1].replace(' http','http')
                  print 'Img: ' + img
                  rtmp = params[2]
                  print 'Link: ' + rtmp
                  addDir(nome,rtmp,11,img,False)
            except:
                  pass
      xbmc.executebuiltin("Container.SetViewMode(500)")
		
##########################################################################################################################	
	
def listar_canais(url):
      for line in urllib2.urlopen(url).readlines():
            params = line.split(',')
            try:
                  nome = params[0]
                  print 'Nome: ' + nome
                  img = params[1].replace(' rtmp','rtmp').replace(' rtsp','rtsp').replace(' http','http')
                  print 'Img: ' + img
                  rtmp = params[2].replace(' rtmp','rtmp').replace(' rtsp','rtsp').replace(' http','http')
                  print 'Link: ' + rtmp
                  addLink(nome,rtmp,img)
            except:
                  pass
      xbmc.executebuiltin("Container.SetViewMode(500)")
	  
	  
def abrir_url(url):
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	response = urllib2.urlopen(req)
	link=response.read()
	response.close()
	return link

def real_url(url):
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	response = urllib2.urlopen(req)
	link=response.geturl()
	response.close()
	return link

def addLink(name,url,iconimage):
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
	liz.setProperty('fanart_image', fanart)
	liz.setInfo( type="Video", infoLabels={ "Title": name } )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
	return ok

def addDir(name,url,mode,iconimage,pasta=True,total=1):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setProperty('fanart_image', fanart)
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=pasta,totalItems=total)
	return ok

	
############################################################################################################
#                                               GET PARAMS                                                 #
############################################################################################################

              
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param

      
params=get_params()
url=None
name=None
mode=None
iconimage=None


try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass

try:        
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass


print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "Iconimage: "+str(iconimage)


###############################################################################################################
#                                                   MODOS                                                     #
###############################################################################################################

   ##### Tv Online
if mode==None or url==None or len(url)<1:
    print ""
    menus()
	
elif mode==13:
	print ""
	categorias()

elif mode==15:
	print ""
	categorias_tv_paga_brasil()	
	
elif mode==16: 
	print ""
	listar_canais(url)

elif mode==17: 
	listar_videostxt(url)
elif mode==18:
	player_youtube(url)	
                             #### Fim TV Online
							 
							 ######################   Armagedon   ############
elif mode==2:
	print ""
	listar_videos(url)
	
elif mode==3:
	print ""
	pesquisa_filme()

elif mode==4:
	print ""
	player(name,url,iconimage)
	
elif mode==5:
	print ""
	listar_videos_M18(url)
	
elif mode==6:
	listar_series(url)
	
elif mode==7:
	print ""
	listar_series_f2(name,url)	
	
elif mode==8:
	print ""
	pesquisa_serie()
	
elif mode==9:
	print ""
	listar_animes(url)	
	
elif mode==12:
	print "Mode 12"
	listar_temporadas(url)
	
elif mode==19:
	print ""
	CATEGORIES()
	

	

elif mode==21:
	print ""
	categorias_Armagedon()
	
	                                   ####### Fim Armagedon
									   
elif mode==23:
	print ""
	categorias_2()	

elif mode==24:
	print ""
	categorias_Armagedon2()

	
elif mode==25:
	print ""
	listar_videos(url)
						   

						   
									   
									   
	
xbmcplugin.endOfDirectory(int(sys.argv[1]))



	

