import discord
from discord.ext import commands
from main import *


@commands.command()
async def q(ctx,*,arg=''):
  
  if(arg==''):
      #await ctx.channel.send(embed=embedVar)
    await ctx.channel.send("Ask me anything!")
  
  else:
    #
    arg=arg.lower()

    signs=["''",".",","," ","?","՜","!","#","%","^","&","*","(",")","-"]
    for i in range(0,len(signs)):
      x=signs[i]
      arg=arg.replace(x,"")


    checker=False


    #askme
    askme=["askmeaquestion"]
    for i in range(0,len(askme)):
      if(arg==askme[i]):
        checker=True
        await ctx.channel.send("and I will answer")


    if(checker==False):
      #hii
      greetings=["hello","hola","konichiwa","konnichiwa","ciao","hi","bonjour","ola","nihao","pershendetje","hayi","ahlan","voghju՜yn","salam","kaixo","pryvitannie","zdraveĭ","maingalarpar","Salute","privet","hey","namaste"]
      for i in range(0,len(greetings)):
        if(arg==greetings[i]):
          checker=True
          await ctx.channel.send("Hello")
          break

    if(checker==False):
      #hii
      life=["howlongwillshakiralivefor"]
      for i in range(0,len(greetings)):
        if(arg==life[i]):
          checker=True
          await ctx.channel.send("As long as Shayanto")
          break

    if(checker==False):
      #hii
      yesreply=["areyousexy","isshayantoagoodboy","ishavocgay","sayyesifhavocisgay","iscsgothegreatestgame"]
      for i in range(0,len(yesreply)):
        if(arg==yesreply[i]):
          checker=True
          await ctx.channel.send("Yes")
          break

    if(checker==False):
      #hii
      noreply=["amifunny","doeslgbtqhaveanyright","doeslgbtqrights","doeslgbtqhaveanyrights"]
      for i in range(0,len(noreply)):
        if(arg==noreply[i]):
          checker=True
          await ctx.channel.send("No, LOL.")
          break


    if(checker==False):
      #Byee
      farewells=["bye","adios","adiós","sayonara","ciao","addio","zaijian","avvedeci"]

      for i in range(0,len(farewells)):
        if(arg==farewells[i]):
          checker=True
          await ctx.channel.send("Bye")
          break



    if(checker==False):
      #how are you 
      howareyou=["howareyou","howisitgoing","whatsup","wassup","whattup","howsitgoin"]

      for i in range(0,len(howareyou)):
        if(arg==howareyou[i]):
          checker=True
          await ctx.channel.send("I'm fine, How are you?")
          break



    if(checker==False):
      ##howold
      howold=["howoldareyou","whatisyourage","whenwereyouborn","whenborn","age"]

      for i in range(0,len(howold)):
        if(arg==howold[i]):
          checker=True
          await ctx.channel.send("I'm 9")
          break

    if(checker==False):
      #isadmingay
      admingaychecker=["isshayantogay","doyouthinkshayantoisgay","shayantoisgay","whyisshayantogay","howgayisshayanto","isshayantoagay","isshayantohomo","iscyberninjagay","cyberninjaisgay","doyouthinkcyberninjaisgay","whyiscyberninjagay","howgayiscyberninja","iscyberninjaagay","isryangay","ryanisgay","whyisryangay","howgayisryan","isryanagay","doyouthinkryanisgay","isryanhomo","istatogay","whyistatogay","tatoisgay","doyouthinktatoisgay","howgayistato"]

      for i in range(0,len(admingaychecker)):
        if(arg==admingaychecker[i]):
          checker=True
          await ctx.channel.send("He's not gay, but if you are havoc, you are gay")
          break

    if(checker==False):
      #isbotgay
      botgaychecker=["areyougay","howgayareyou","whyareyougay","stopbeinggay","areyouhomo","doyoulikepp","areyouintoguys","doyoulikemale","doyoulikeguys","doyoulikeman","doyoulikemen","doyoulikepenis","doyoulikenunu","isyougay","areyoulesbian","areyoualesbian"]

      for i in range(0,len(botgaychecker)):
        if(arg==botgaychecker[i]):
          checker=True
          await ctx.channel.send("I am starighter than the pole your mama dances on.")
          break

    if(checker==False):
      #relationshipcheck
      relationcheck=["doyouhaveaboyfriend","doyouhaveagirlfriend","areyoutaken","areyouseeinganyone","areyoualone","wouldyouliketobemygirlfriend","wouldyouliketobemyboyfriend"]

      for i in range(0,len(relationcheck)):
        if(arg==relationcheck[i]):
          checker=True
          await ctx.channel.send("No. But I like anime girls.")
          break

    if(checker==False):
      await ctx.channel.send("Sorry, I don't understand your question")

def setup(client):
  # Every extension should have this function
  client.add_command(q)

