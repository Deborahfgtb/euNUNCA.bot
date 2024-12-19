import asyncio, random
import os
import importlib.util
from highrise import*
from highrise import BaseBot,User,CurrencyItem,GetMessagesRequest,Item,Position
from highrise.models import SessionMetadata

moderators = ["iMooseMoo","Miwiii","@___Deborah____“,“@GDARKYO"]

cara = ["😢caiu coroa mais sorte na proxima...","parabens você ganhou caiu cara..."]

coroa = ["😢caiu cara mais sorte na proxima...","parabens você ganhou caiu coroa..."]

tarot4 = ["A Força: tem relação com a busca de autocontrole em paixões","A Morte: designa términos e soluções para ocorrer renovação","O Mundo: carta da fama, da projeção e das vantagens","O Julgamento: é a carta da cura e da transformação eficaz das situações","O Sol: significa lucidez e harmonia","A Lua: revela medos, ilusões, fantasias e perigos","A Estrela: simboliza iluminação em meio às trevas","A Torre: indica falsas estruturas, livramento das ilusões","O Diabo: é a carta do instinto e das dependências","A Temperança: aponta o tédio e exige perseverança","O Pendurado: revela a dedicação e dificuldades por causas maiores","O Louco: representa situações caóticas","Mago: indica domínio das situações","A Sacerdotisa: representa mistério e reflexão","A Imperatriz: indica frutificação do que foi plantado","O Sacerdote: significa confiança e compromisso com o próximo","O Imperador: simboliza força e poder","Os Enamorados: representa desejos e confusões mentais","O Carro: indica vitória","A Justiça: significa necessidade de equilíbrio interior","O Eremita: revela o que é essencial para criar maturidade","A Roda da Fortuna: simboliza mudanças"]

tarot3 = ["A Força: tem relação com a busca de autocontrole em paixões","A Morte: designa términos e soluções para ocorrer renovação","O Mundo: carta da fama, da projeção e das vantagens","O Julgamento: é a carta da cura e da transformação eficaz das situações","O Sol: significa lucidez e harmonia","A Lua: revela medos, ilusões, fantasias e perigos","A Estrela: simboliza iluminação em meio às trevas","A Torre: indica falsas estruturas, livramento das ilusões","O Diabo: é a carta do instinto e das dependências","A Temperança: aponta o tédio e exige perseverança","O Pendurado: revela a dedicação e dificuldades por causas maiores","O Louco: representa situações caóticas","Mago: indica domínio das situações","A Sacerdotisa: representa mistério e reflexão","A Imperatriz: indica frutificação do que foi plantado","O Sacerdote: significa confiança e compromisso com o próximo","O Imperador: simboliza força e poder","Os Enamorados: representa desejos e confusões mentais","O Carro: indica vitória","A Justiça: significa necessidade de equilíbrio interior","O Eremita: revela o que é essencial para criar maturidade","A Roda da Fortuna: simboliza mudanças"]

tarot2 = ["A Força: tem relação com a busca de autocontrole em paixões","A Morte: designa términos e soluções para ocorrer renovação","O Mundo: carta da fama, da projeção e das vantagens","O Julgamento: é a carta da cura e da transformação eficaz das situações","O Sol: significa lucidez e harmonia","A Lua: revela medos, ilusões, fantasias e perigos","A Estrela: simboliza iluminação em meio às trevas","A Torre: indica falsas estruturas, livramento das ilusões","O Diabo: é a carta do instinto e das dependências","A Temperança: aponta o tédio e exige perseverança","O Pendurado: revela a dedicação e dificuldades por causas maiores","O Louco: representa situações caóticas","Mago: indica domínio das situações","A Sacerdotisa: representa mistério e reflexão","A Imperatriz: indica frutificação do que foi plantado","O Sacerdote: significa confiança e compromisso com o próximo","O Imperador: simboliza força e poder","Os Enamorados: representa desejos e confusões mentais","O Carro: indica vitória","A Justiça: significa necessidade de equilíbrio interior","O Eremita: revela o que é essencial para criar maturidade","A Roda da Fortuna: simboliza mudanças"]

tarot1 = ["A Força: tem relação com a busca de autocontrole em paixões","A Morte: designa términos e soluções para ocorrer renovação","O Mundo: carta da fama, da projeção e das vantagens","O Julgamento: é a carta da cura e da transformação eficaz das situações","O Sol: significa lucidez e harmonia","A Lua: revela medos, ilusões, fantasias e perigos","A Estrela: simboliza iluminação em meio às trevas","A Torre: indica falsas estruturas, livramento das ilusões","O Diabo: é a carta do instinto e das dependências","A Temperança: aponta o tédio e exige perseverança","O Pendurado: revela a dedicação e dificuldades por causas maiores","O Louco: representa situações caóticas","Mago: indica domínio das situações","A Sacerdotisa: representa mistério e reflexão","A Imperatriz: indica frutificação do que foi plantado","O Sacerdote: significa confiança e compromisso com o próximo","O Imperador: simboliza força e poder","Os Enamorados: representa desejos e confusões mentais","O Carro: indica vitória","A Justiça: significa necessidade de equilíbrio interior","O Eremita: revela o que é essencial para criar maturidade","A Roda da Fortuna: simboliza mudanças"]

ff = ["sim","não","provavelmente sim","talvez","não sei","talvez sim","talvez não","provavelmente não","completamente sim","completamente não"]

coco = ["seu coco veio com milho 🌽","você cagou um tronco","seu coco está mole 🌊"]

louca = ["🤪Seu Livel De Loucura é de : 100%","🤪Seu Livel De Loucura é de : 99%","🤪Seu Livel De Loucura é de : 50%","🤪Seu Livel De Loucura é de : 0%","🤪Seu Livel De Loucura é de : 1%","🤪Seu Livel De Loucura é de : 2%","🤪Seu Livel De Loucura é de : 64%","🤪Seu Livel De Loucura é de : 22%","🤪Seu Livel De Loucura é de : 19%","🤪Seu Livel De Loucura é de : 88%","🤪Seu Livel De Loucura é de : 39%","🤪Seu Livel De Loucura é de : 40%","🤪Seu Livel De Loucura é de : 92%","🤪Seu Livel De Loucura é de : 74%","🤪Seu Livel De Loucura é de : 10%","🤪Seu Livel De Loucura é de : 9%","🤪Seu Livel De Loucura é de : 77%","🤪Seu Livel De Loucura é de : 82%","🤪Seu Livel De Loucura é de : 66%","🤪Seu Livel De Loucura é de : 11%","🤪Seu Livel De Loucura é de : 15%"]
        
casa = ["Eu Caso Com Você 💍","Claro Que sim 💍❤️","Não Quero 💍💔","Claro Que Não 💍💔","Eu Te Amo Claro Que Eu Caso Com Você 💍"]


curativo = ["🔴Você Usou o Curativo Sua Vida Está em : 100%🔴","🔴Você Usou o Curativo Sua Vida Está em : 50%🔴","🔴Você Usou o Curativo Sua Vida Está em : 60%🔴","🔴Você Usou o Curativo Sua Vida Está em : 75%🔴","🔴Você Usou o Curativo Sua Vida Está em : 85%🔴","🔴Você Usou o Curativo Sua Vida Está em : 80%🔴","🔴Você Usou o Curativo Sua Vida Está em : 90%🔴","🔴Você Usou o Curativo Sua Vida Está em : 95%🔴","🔴Você Usou o Curativo Sua Vida Está em : 99%🔴","🔴Você Usou o Curativo Sua Vida Está em : 91%🔴"]
         
bomba = ["💣🧟‍♂️ Você Jogou Uma Bomba em 1x Boss Zombie 🧟‍♀️💣","💣🧟 Você Jogou Uma Bomba em 3x Boss Zombie 🧟💣","💣🧟‍♂️ Você Jogou Uma Bomba em 2x Boss Zombie 💣🧟‍♀️","💣🧟‍♂️ Você Jogou Uma Bomba em 7x Boss Zombie 💣🧟‍♂️","💣🧟 Você Jogou Uma Bomba em 4x Boss Zombie 🧟💣"]

facada = ["🧟🔪 Você Esfaqueou 1x Zombie 🔪🧟","🧟🔪 Você Esfaqueou 6x Zombie 🔪🧟","🧟🔪 Você Esfaqueou 7x Zombie 🔪🧟","🧟‍♂️🔪🧟‍♂️ Você Esfaqueou  8x Zombie 🔪🧟‍♂️","🧟🔪 Você Esfaqueou  10x Zombie 🔪🧟","🧟🔪 Você Esfaqueou  9x Zombie 🔪🧟","🧟‍♀️🔪🧟‍♂️ Você Esfaqueou  3x Zombie 🧟‍♂️🔪🧟‍♀️"]

atirar = ["🧟Você Atirou em 5x Zombie🧟","🧟Você Atirou em 1x Zombie🧟","🧟Você Atirou em 8x Zombie🧟","🧟Você Atirou em 3x Zombie🧟","🧟‍♂️Você Atirou em 5x Zombie🧟‍♂️","🧟‍♀️Você Atirou em 10x Zombie🧟‍♀️","🧟🧟‍♀️Você Atirou em 9x Zombie🧟🧟‍♀️"]

play = ["🔴Sua Vida Está em 50% use : /curativo","🔴Sua Vida Está em 20% use : /curativo","🔴Sua Vida Está em 40% use : /curativo","🧟Os Zombies Estão Vindo Use : /facada ou /atirar","🧟🧟‍♂️ Tem Muitos Zombies 🧟‍♀️🧟 🛡 Use : /escudo 🛡","🧟O Zombie Boss Esta  Vindo Use : /bomba ","🧟Os Zombies Estão Vindo Use : /facada ou /atirar","🧟🧟‍♂️ Tem Muitos Zombies 🧟‍♀️🧟 🛡 Use : /escudo 🛡","🔴Sua Vida Está em 60% use : /curativo","🔴Sua Vida Está em 10% use : /curativo","🧟Os Zombies Estão Vindo Use : /facada ou /atirar"
      ,"🧟Os Zombies Estão Vindo Use : /facada ou /atirar","🧟Os Zombies Estão Vindo Use : /facada ou /atirar","🧟Os Zombies Estão Vindo Use : /facada ou /atirar","🧟Os Zombies Estão Vindo Use : /facada ou /atirar","🧟Os Zombies Estão Vindo Use : /facada ou /atirar"]

pescar = ["🥈VOCÊ GANHOU A MEDALHA : PESCADOR PRATA🥈","🥉VOCÊ GANHOU A MEDALHA : PESCADOR BRONZE🥉","🥉VOCÊ GANHOU A MEDALHA : PESCADOR BRONZE🥉","🥉VOCÊ GANHOU A MEDALHA : PESCADOR BRONZE🥉","🥉VOCÊ GANHOU A MEDALHA : PESCADOR BRONZE🥉","🟡Evento :  /carpa 🟡","⚫️Você Pescou 3x Lua Da Noite⚫️(+150 PONTOS)","⚫️Você Pescou 2x Lua Da Noite⚫️(+100 PONTOS)","⚫️Você Pescou 1x Lua Da Noite⚫️(+50 PONTOS)","🟡Você Pescou 1x Camarão Dourado 🟡 (MULTIPLO PONTO)","🟡Você Pescou 1x Linguado Dourado🟡 (MULTIPLO PONTO)","🪼🌈Você Pescou 1x Polvo Arco-iris🪼🌈 (EXTRA PONTOS)","🐢Você Pescou 3x  Tartaruga 🐢 (PERDA DE PONTOS)","🦑Você Pescou 1x  Lula Gigante 🦑 (LEGENDARIO)","🦀Você Pescou 6x  Carangueijo 🦀 (COMUM)","🦀Você Pescou 2x  Carangueijo 🦀 (COMUM)","🦀Você Pescou 8x  Carangueijo 🦀 (COMUM)","🪼Você Pescou 1x Polvo Do Mar🪼(EPICO)","🦈Você Pescou 2x Tubarão🦈 (EPICO)","🦈Você Pescou 5x Tubarão🦈 (EPICO)","🦈Você Pescou 8x Tubarão🦈 (EPICO)","🦈Você Pescou 1x Tubarão🦈 (EPICO)","🐠Você Pescou 1x Tuna Do Mar🐠 (LEGENDARIO)","🐠Você Pescou 3x Peixe Palhaço🐠 (LEGENDARIO)","🐠Você Pescou 3x Tuna Do Mar🐠 (LEGENDARIO)","🐠Você Pescou 1x Peixe Palhaço🐠 (LEGENDARIO)","🐠Você Pescou 8x Peixe Palhaço🐠 (LEGENDARIO)","🐠Você Pescou 10x Peixe Palhaço🐠 (LEGENDARIO)","🐟Você Pescou 1x Salmão🐟 (RARE)","🧜🏼‍♀️Você Pescou 5x Sereia🧜🏼‍♀️(EPICO)","🧜🏼‍♀️Você Pescou 2x Sereia🧜🏼‍♀️(EPICO)","🧜🏼‍♀️Você Pescou 1x Sereia🧜🏼‍♀️(EPICO)","🐟Você Pescou 3x Salmão🐟 (RARE)","🟡Você Pescou 1x Tilapia Dourada🟡 (MULTIPLO PONTO)","☠️🐋Você Pescou 3x Baleia Morta☠️🐋 (PERDA DE PONTOS)","🐋Você Pescou 11x Baleia Do Mar🐋(COMUM)","🐋🌈Você Pescou 1x Baleia Arco-iris🌈🐋 (EXTRA PONTOS)","🥈VOCÊ GANHOU A MEDALHA : PESCADOR PRATA🥈","🥇VOCÊ GANHOU A MEDALHA : PESCADOR OURO🥇","🏅VOCÊ GANHOU A MEDALHA : ESTRELA PESCADOR🏅","💎Evento : /camarão💎"]

cantada = ["Posso tirar uma foto sua? É para mostrar ao Papai Noel o que eu quero de presente.","Se preto fosse paixão e branco fosse carinho, o que eu sinto por você seria xadrezinho.","Qual é o número da polícia? Infelizmente, terei que te denunciar por roubar meu coração.","Meus amigos apostaram comigo que eu não conseguiria iniciar uma conversa com a pessoa mais bonita daqui. Como devemos gastar o dinheiro deles?","Prazer, eu sou um ladrão/uma ladra. Estou aqui para roubar o seu coração.","Pesquisas apontam que agente junto é erro de gramática, mas a gente separado é erro do destino.","Se nada dura para sempre, quer ser o meu nada?","Seu nome é Wi-Fi? Porque eu estou sentindo uma conexão aqui.","Está vendo aquela estrela ali? Mandei pendurar para você.","Então, além de me deixar sem ar, o que mais você faz?","Nossa, estou sentindo uma dor no peito! Espero que seja amor, porque se for infarto, eu nunca mais te verei!","As rosas são vermelhas, violetas são azuis, eu não sei rimar, mas posso namorar você?","Você foi feita(o) com velas, mel, fitinhas vermelhas e rosas? Porque te achei uma simpatia."]

piada = ["Qual é o prato preferido do Thor? Thorresmo","O que o cavalo foi fazer no orelhão? Passar trote","Qual é o rio mais azedo do mundo? O Rio Solimões","Qual é o lugar mais certo do Brasil? O sertão.","Qual é o vinho que não tem álcool? Ovinho de codorna"]

hate = ["As pessoas te odeiam 0%","As pessoas te odeiam 20%","As pessoas te odeiam 100%","As pessoas te odeiam 50%","As pessoas te odeiam 45%","As pessoas te odeiam 99%","As pessoas te odeiam 95%","As pessoas te odeiam 34%","As pessoas te odeiam 77%","As pessoas te odeiam 80%","As pessoas te odeiam 66%","As pessoas te odeiam 39%","As pessoas te odeiam 20%","As pessoas te odeiam 22%","As pessoas te odeiam 49%"]

amor = ["As pessoas te amam 0%❤️","As pessoas te amam 20%❤️","As pessoas te amam 100%❤️","As pessoas te amam 50%❤️","As pessoas te amam 45%❤️","As pessoas te amam 99%❤️","As pessoas te amam 95%❤️","As pessoas te amam 34%❤️","As pessoas te amam 77%❤️","As pessoas te amam 80%❤️","As pessoas te amam 66%❤️","As pessoas te amam 39%❤️","As pessoas te amam 20%❤️","As pessoas te amam 22%❤️","As pessoas te amam 49%❤️"]

emote = ["hcc-jetpack","emote-looping","idle-floating","emote-launch","emote-kissing-bound","dance-tiktok11","emote-salute","emote-cutesalute","dance-employee","emote-gift","dance-touch","dance-kawai","sit-relaxed","emote-pose6","emote-sleigh","emote-hyped","dance-jinglebell","idle-toilet","emote-timejump","idle-nervous","idle-wild","emote-iceskating","emote-celebrate","emote-pose10","emote-shy2","emote-headblowup","emote-creepycute","dance-creepypuppet","dance-anime","emote-astronaut","dance-pinguin","idle-guitar","emote-boxer","emote-pose9","emote-stargazer","idle-dance-tiktok4","idle-uwu","dance-tiktok9","dance-tiktok8","dance-weird","dance-macarena","emote-swordfight","idle-loop-sitfloor","emote-zombierun","emoji-angry","emoji-thumbsup","emoji-cursing","emote-punkguitar","emoji-flex","emoji-gagging","emoji-celebrate","dance-blackpink","dance-tiktok2","dance-pennywise","dance-russian","dance-shoppingcart","idle-enthusiastic","idle_singing","dance-tiktok10","emote-cutey","emote-pose5","emote-pose1","emote-pose3","emote-pose8","emote-pose7","emote-cute","emote-superpose","emote-frog","dance-wrong","emote-gravity","emote-fashionista","dance-icecream","idle-dance-casual","emote-kiss","emote-sad","emote-yes","emote-laughing","emote-hello","emote-wave","emote-no","emote-tired","emote-lust","emote-shy","emote-greedy","emote-model","emote-bow","emote-hot","emote-snowball","emote-curtsy","emote-charging","emote-confused","emote-snowangel","emote-telekinesis","emote-float","emote-teleporting","emote-maniac","emote-energyball","emote-snake"]

react = ["wave","wink","thumbs","heart","clap"]

class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("funcionando")  
        await self.highrise.walk_to(Position(3.5 , 0.5 ,0.5 , "FrontRight"))
    async def on_user_join(self, user: User, position: Position | AnchorPosition) -> None:
        print(f"{user.username} entrou na sala") 
        if user.username in moderators:
         await self.highrise.chat(f"🚫{user.username} Moderador(a) da sala\n[Entrou na sala]")
         
        await self.highrise.send_whisper(user.id,f"🎀 Seija bem vindo(a)🎀")

        await self.highrise.send_emote(random.choice(emote))
        await self.highrise.send_emote(random.choice(emote),user.id)
        
    async def on_chat(self, user: User, message: str) -> None:
        print(f"{user.username}: {message}") 

        if                   message.startswith("!love"):
           target_username = message.split("@")[-1].strip()
           await self.highrise.chat(f"@{target_username} love 40% {user.username}")

        if                message.startswith("!match"):
          target_username = message.split("@")[-1].strip()
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)        # Select the first three users
          selected_users = roomUsers[:1]
          for roomUser, _ in selected_users:
           await self.highrise.chat(f"Casamenteiro: @{roomUser.username} & @{target_username} são um par! ❤️")
              
        if                message.startswith("!match"):
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)        # Select the first three users
          selected_users = roomUsers[:1]
          for roomUser, _ in selected_users:
           await self.highrise.chat(f"Casamenteiro: @{roomUser.username} e @{user.username} são um par! ❤️")
            
        if message.lower().startswith(("!cagar","/cagar")):
            await self.highrise.send_emote("idle-loop-sitfloor",user.id)
            await self.highrise.send_whisper(user.id,f"💩{user.username} você começou a cagar...")
            await asyncio.sleep(1)
            await self.highrise.send_whisper(user.id,f"💩Você está cagando...")
            await asyncio.sleep(1)
            await self.highrise.send_whisper(user.id,f"💩Você está cagando...")
            await asyncio.sleep(1)
            await self.highrise.send_whisper(user.id,f"💩Você está cagando...")
            await asyncio.sleep(2)
            await self.highrise.send_whisper(user.id,f"💩{user.username} {random.choice(coco)}..")

        if message.lower().startswith(("!ask","/ask")):
            await self.highrise.send_whisper(user.id,f"\n🧠Eu estou pensando...")
            await asyncio.sleep(1)
            await self.highrise.send_whisper(user.id,f"\n🧠Eu estou pensando...")
            await asyncio.sleep(1)
            await self.highrise.send_whisper(user.id,f"\n🧠Eu estou pensando...")
            await asyncio.sleep(2)
            await self.highrise.send_whisper(user.id,f"\n{user.username}\n{random.choice(ff)}")
            
        if message.lower().startswith(("!tarot","/tarot")):
            await self.highrise.send_whisper(user.id,f"\n🃏{user.username} 4 Cartas serão em-baralhadas e retiradas com seus significados...\n\n🃏Não leve essa tiragem a serio, ou leve caso acreditar em sinais...")
            await asyncio.sleep(1)
            await self.highrise.send_whisper(user.id,f"\n🃏Carregando as cartas...")
            await asyncio.sleep(1)
            await self.highrise.send_whisper(user.id,f"\n🃏Carregando as cartas...")
            await asyncio.sleep(1)
            await self.highrise.send_whisper(user.id,f"\n🃏Carregando as cartas...")
            await asyncio.sleep(2)
            await self.highrise.send_whisper(user.id,f"\n🃏{user.username} As 4 Cartas Retiradas Foram:\n1°{random.choice(tarot1)}\n2°{random.choice(tarot2)}")
            await self.highrise.send_whisper(user.id,f"\n3°{random.choice(tarot3)}\n4°{random.choice(tarot4)}")
            
        if message.lower().startswith(("!moeda cara","/moeda cara")):
            await self.highrise.send_emote("fishing-cast",user.id)
            await self.highrise.send_whisper(user.id,f"{user.username} você jogou a moeda...")
            await asyncio.sleep(1)
            await self.highrise.send_whisper(user.id,f"🌀A moeda está girando...")
            await asyncio.sleep(1)
            await self.highrise.send_whisper(user.id,f"🌀A moeda está girando...")
            await asyncio.sleep(1)
            await self.highrise.send_whisper(user.id,f"🌀A moeda está girando...")
            await asyncio.sleep(2)
            await self.highrise.send_emote("emoji-flex",user.id)
            await self.highrise.send_whisper(user.id,f"{user.username} {random.choice(cara)} 🪙")
            
        if message.lower().startswith(("!moeda coroa","/moeda coroa")):
            await self.highrise.send_emote("fishing-cast",user.id)
            await self.highrise.send_whisper(user.id,f"{user.username} você jogou a moeda...")
            await asyncio.sleep(1)
            await self.highrise.send_whisper(user.id,f"🌀A moeda está girando...")
            await asyncio.sleep(1)
            await self.highrise.send_whisper(user.id,f"🌀A moeda está girando...")
            await asyncio.sleep(1)
            await self.highrise.send_whisper(user.id,f"🌀A moeda está girando...")
            await asyncio.sleep(2)
            await self.highrise.send_emote("emoji-flex",user.id)
            await self.highrise.send_whisper(user.id,f"{user.username} {random.choice(coroa)} 🪙")
                
        if message.lower().startswith(("!jogar","/jogar","/rps","!rps")):
          choices = ['pedra', 'papel', 'tesoura']
          client_chosen = random.choice(choices)
          option = message[5:].strip().lower()

          text_to_emoji = {"pedra": "✊", "papel": "✋", "tesoura": "✌️"}

          if option not in choices:
              response = f"Uso de comando inválido :\nExemplo: !rps <{client_chosen}>\nOpções disponíveis:\n{', '.join(choices)}"
              await self.highrise.send_whisper(user.id, response)
              return
          elif option == client_chosen:
              response = "Ninguém ganhou, é um empate. 🤝"
          elif (option == "pedra" and client_chosen == "tesoura") or (option == "papel" and client_chosen == "pedra") or (option == "tesoura" and client_chosen == "papel"):
              response = f"\nParabéns, você venceu! 🎉\nvocê: {text_to_emoji[option]}\nBot: {text_to_emoji[client_chosen]}"
          else:
              response = f"\nVocê perdeu. 😢\nVocê: {text_to_emoji[option]}\nBot: {text_to_emoji[client_chosen]}"

          await self.highrise.chat(response)

        if message.lower().startswith("!tip ") and user.username in moderators:
                    parts = message.split(" ", 2)
                    if len(parts) != 3:
                        await self.highrise.send_whisper(user.id, "Invalid command")
                        return

                    username = parts[1].strip("<>@")
                    try:
                        amount = int(parts[2])
                    except ValueError:
                        await self.highrise.send_whisper(user.id, "Invalid amount")
                        return

                    
                    bot_wallet = await self.highrise.get_wallet()
                    bot_amount = bot_wallet.content[0].amount

                    
                    if bot_amount <= amount:
                        await self.highrise.send_whisper(user.id, "Not enough funds")
                        return

                    
                    bars_dictionary = {
                        10000: "gold_bar_10k", 
                        5000: "gold_bar_5000",
                        1000: "gold_bar_1k",
                        500: "gold_bar_500",
                        100: "gold_bar_100",
                        50: "gold_bar_50",
                        10: "gold_bar_10",
                        5: "gold_bar_5",
                        1: "gold_bar_1"
                    }
                    fees_dictionary = {
                        10000: 1000,
                        5000: 500,
                        1000: 100,
                        500: 50,
                        100: 10,
                        50: 5,
                        10: 1,
                        5: 1,
                        1: 1
                    }

                    
                    tip = []
                    total = 0
                    for bar in sorted(bars_dictionary.keys(), reverse=True):
                        if amount >= bar:
                            bar_amount = amount // bar
                            amount = amount % bar
                            for _ in range(bar_amount):
                                tip.append(bars_dictionary[bar])
                                total += bar + fees_dictionary[bar]

                    
                    if total > bot_amount:
                        await self.highrise.send_whisper(user.id, "Não há fundos suficientes ")
                        return

                    
                    try:
                        room_users = (await self.highrise.get_room_users()).content
                        user_ids = {room_user.username: room_user.id for room_user, _ in room_users}
                    except Exception as e:
                        await self.highrise.send_whisper(user.id, "Falha ao recuperar usuários da sala ")
                        logging.error(f"Ocorreu um erro ao recuperar usuários da sala : {e}")
                        return

                    user_id = user_ids.get(username)
                    if user_id:
                        try:
                            await self.highrise.tip_user(user_id, ",".join(tip))
                            await self.highrise.chat(f"Tipped @{username} {parts[2]}g!")
                        except Exception as e:
                            logging.error(f"Ocorreu um erro ao dar gorjeta ao usuário  {user_id}: {e}")
                    else:
                        await self.highrise.chat(f"Usuário @{username} não encontrado ")
                        
        if message.lower().startswith("!tipall ") and user.username in moderators:
              parts = message.split(" ")
              if len(parts) != 2:
                  await self.highrise.send_message(user.id, "💰Comando inválido")
                  return
              # Checks if the amount is valid
              try:
                  amount = int(parts[1])
              except:
                  await self.highrise.chat("💰Quantidade inválida")
                  return
              # Checks if the bot has the amount
              bot_wallet = await self.highrise.get_wallet()
              bot_amount = bot_wallet.content[0].amount
              if bot_amount < amount:
                  await self.highrise.chat("💰Não há fundos suficientes")
                  return
              # Get all users in the room
              room_users = await self.highrise.get_room_users()
              # Check if the bot has enough funds to tip all users the specified amount
              total_tip_amount = amount * len(room_users.content)
              if bot_amount < total_tip_amount:
                  await self.highrise.chat("💰Não há fundos suficientes para dar gorjeta a todos")
                  return
              # Tip each user in the room the specified amount
              for room_user, pos in room_users.content:
                  bars_dictionary = {
                      10000: "gold_bar_10k",
                      5000: "gold_bar_5000",
                      1000: "gold_bar_1k",
                      500: "gold_bar_500",
                      100: "gold_bar_100",
                      50: "gold_bar_50",
                      10: "gold_bar_10",
                      5: "gold_bar_5",
                      1: "gold_bar_1"
                  }
                  fees_dictionary = {
                      10000: 1000,
                      5000: 500,
                      1000: 100,
                      500: 50,
                      100: 10,
                      50: 5,
                      10: 1,
                      5: 1,
                      1: 1
                  }
                  # Convert the amount to a string of bars and calculate the fee
                  tip = []
                  remaining_amount = amount
                  for bar in bars_dictionary:
                      if remaining_amount >= bar:
                          bar_amount = remaining_amount // bar
                          remaining_amount = remaining_amount % bar
                          for i in range(bar_amount):
                              tip.append(bars_dictionary[bar])
                              total = bar + fees_dictionary[bar]
                  if total > bot_amount:
                      await self.highrise.chat("💰Não há fundos suficientes")
                      return
                  for bar in tip:
                      await self.highrise.tip_user(room_user.id, bar)                   
                      await self.highrise.chat(f"💰Deu para {room_user.username} {amount} {bar}!")

        if message.lower().startswith("!tipme ") and user.username in moderators:
                try:
                    amount_str = message.split(" ")[1]
                    amount = int(amount_str)
                    bars_dictionary = {
                        10000: "gold_bar_10k",
                        5000: "gold_bar_5000",
                        1000: "gold_bar_1k",
                        500: "gold_bar_500",
                        100: "gold_bar_100",
                        50: "gold_bar_50",
                        10: "gold_bar_10",
                        5: "gold_bar_5",
                        1: "gold_bar_1"
                    }
                    fees_dictionary = {
                        10000: 1000,
                        5000: 500,
                        1000: 100,
                        500: 50,
                        100: 10,
                        50: 5,
                        10: 1,
                        5: 1,
                        1: 1
                    }
                    # Get bot's wallet balance
                    bot_wallet = await self.highrise.get_wallet()
                    bot_amount = bot_wallet.content[0].amount
                    # Check if bot has enough funds
                    if bot_amount < amount:
                        await self.highrise.chat("💰Não há fundos suficientes na carteira do bot. ")
                        return
                    # Convert amount to bars and calculate total
                    tip = []
                    total = 0
                    for bar in sorted(bars_dictionary.keys(), reverse=True):
                        if amount >= bar:
                            bar_amount = amount // bar
                            amount %= bar
                            tip.extend([bars_dictionary[bar]] * bar_amount)
                            total += bar_amount * bar + fees_dictionary[bar]
                    if total > bot_amount:
                        await self.highrise.chat("💰Não há fundos suficientes para dar a gorjeta no valor especificado. ")
                        return
                    # Send tip to the user who issued the command
                    for bar in tip:
                        await self.highrise.tip_user(user.id, bar)
                    await self.highrise.chat(f"💰Você foi avisado  {amount_str}.")
                except (IndexError, ValueError):
                    await self.highrise.chat("💰Valor de gorjeta inválido. Por favor, especifique um número válido. ")   
                    await self.highrise.chat(f"💰Deu para {user.username} {amount} {bar}!")
           
        if message.lower().startswith(("!pescar","/pescar")):
            await self.highrise.send_emote("fishing-cast",user.id)
            await self.highrise.send_whisper(user.id,f"{user.username} você jogou a linha🎣...")
            await asyncio.sleep(2)
            await self.highrise.send_emote("fishing-idle",user.id)
            await self.highrise.send_whisper(user.id,f"{user.username} Você Está Pescando 🎣...")
            await asyncio.sleep(1)
            await self.highrise.send_whisper(user.id,f"{user.username} Você Está Pescando 🎣...")
            await asyncio.sleep(1)
            await self.highrise.send_whisper(user.id,f"{user.username} Você Está Pescando 🎣...")
            await asyncio.sleep(2)
            await self.highrise.react("clap",user.id)
            await self.highrise.send_emote("fishing-pull",user.id)
            await self.highrise.send_whisper(user.id,f"{user.username}\n{random.choice(pescar)}")
            
            
        if message.lower().startswith(("!play","/play")):
            await self.highrise.send_whisper(user.id,f"\n🧟‍♂️Os zombies estâo vindo...")
            await asyncio.sleep(2)
            await self.highrise.send_whisper(user.id,f"\n🧟‍♂️Os zombies estão chegando perto...")
            await asyncio.sleep(1)
            await self.highrise.send_whisper(user.id,f"\n🧟‍♂️Os zombies chegaram perto demais...")
            await asyncio.sleep(2)
            await self.highrise.send_whisper(user.id,f"\n{user.username}\n{random.choice(play)}")

        if message.lower().startswith(("!bomba","/bomba")):
            await self.highrise.send_emote("fishing-cast",user.id)
            await self.highrise.send_whisper(user.id,f"\n💣{user.username} você jogou a bomba nos mega zombies!!")
            await asyncio.sleep(2)
            await self.highrise.send_whisper(user.id,f"\n💣A bomba vai explodir em 3 segundos...")
            await asyncio.sleep(1)
            await self.highrise.send_whisper(user.id,f"\n💣A bomba vai explodir em 2 segundo...")
            await asyncio.sleep(2)
            await self.highrise.send_whisper(user.id,f"\n💣A bomba explodiu!!!")
            await self.highrise.send_whisper(user.id,f"\n{user.username}\n{random.choice(bomba)}")
            await self.highrise.send_whisper(user.id,f"\n{random.choice(play)}")
        if message.lower().startswith(("!facada","/facada")):
            await self.highrise.send_emote("mining-mine",user.id)
            await self.highrise.send_whisper(user.id,f"\n🔪vocé está esfaqueando os zombies...")
            await asyncio.sleep(1)
            await self.highrise.send_whisper(user.id,f"\n🔪vocé está esfaqueando os zombies...")
            await asyncio.sleep(1)
            await self.highrise.send_whisper(user.id,f"\n🔪vocé está esfaqueando os zombies...")
            await asyncio.sleep(2)
            await self.highrise.send_whisper(user.id,f"\n{user.username}\n{random.choice(facada)}")
            await self.highrise.send_whisper(user.id,f"\n{random.choice(play)}")

        if message.lower() == "/atirar":
           frase = random.choice(atirar)
           await self.highrise.send_whisper(user.id,frase)

        if message.lower() == "/loucura":
           frase = random.choice(louca)
           await self.highrise.send_whisper(user.id,frase)

        if message.lower() == "/casa cmg?":
           frase = random.choice(casa)
           await self.highrise.chat(frase)
            
        if message.startswith("/carpa"):
           await self.highrise.react("clap",user.id)
           await self.highrise.send_whisper(user.id,"🟡Você Pescou 1x Carpa Dourada🟡 VOCÊ GANHOU A MEDALHA : (MEGA PESCADOR)")
          
        if message.startswith("/camarão"):
           await self.highrise.react("clap",user.id)
           await self.highrise.send_whisper(user.id,"💎Você Pescou 1x Camarão De Diamante💎VOCÊ GANHOU A MEDALHA : (PESCADOR MASTER DIAMANTE )")                  

        if message.lower().startswith(("!curativo","/curativo")):
            await self.highrise.send_whisper(user.id,f"\n💉{user.username} você iniciou o curativo...")
            await asyncio.sleep(1)
            await self.highrise.react("heart",user.id)
            await self.highrise.react("heart",user.id)
            await self.highrise.send_whisper(user.id,f"💉{user.username} Você está se curando...")
            await self.highrise.react("heart",user.id)
            await self.highrise.react("heart",user.id)
            await asyncio.sleep(1)
            await self.highrise.send_whisper(user.id,f"💉{user.username} Você está se curando...")
            await asyncio.sleep(1)
            await self.highrise.react("heart",user.id)
            await self.highrise.send_whisper(user.id,f"💉{user.username} Você está se curando...")
            await asyncio.sleep(2)
            await self.highrise.react("heart",user.id)
            await self.highrise.react("heart",user.id)
            await self.highrise.send_whisper(user.id,f"\n💉{user.username}{random.choice(curativo)}")
            await self.highrise.send_whisper(user.id,f"\n{random.choice(play)}")
            
        if message.lower().startswith(("!escudo","/escudo")):
            await self.highrise.send_emote("fishing-cast",user.id)
            await self.highrise.send_whisper(user.id,f"\n🛡{user.username} você começou a ativar o escudo...")
            await asyncio.sleep(1)
            await self.highrise.send_whisper(user.id,f"\n🛡O escudo está sendo ativado...")
            await asyncio.sleep(1)
            await self.highrise.send_whisper(user.id,f"\n🛡O escudo está sendo ativado...")
            await asyncio.sleep(1)
            await self.highrise.send_whisper(user.id,f"\n🛡O escudo está sendo ativado...")
            await asyncio.sleep(2)
            await self.highrise.send_emote("emoji-flex",user.id)
            await self.highrise.react("heart",user.id)
            await self.highrise.react("heart",user.id)
            await self.highrise.send_whisper(user.id,f"🛡{user.username} você ativou o escudo...")
            await self.highrise.send_whisper(user.id,f"\n⚠️[Desativação do Escudo] em 5 Segungos...")
            await asyncio.sleep(5)
            await self.highrise.send_whisper(user.id,f"\n🛡❌️O Escudo foi desativado...")
            await self.highrise.send_whisper(user.id,f"\n{random.choice(play)}")

        if message.lower() == "/amor":
           frase = random.choice(amor)
           await self.highrise.send_whisper(user.id,frase)

        if message.lower() == "/odio":
           frase = random.choice(hate)
           await self.highrise.send_whisper(user.id,frase)
      
        if message.lower() == "/piada":
           frase = random.choice(piada)
           await self.highrise.chat(frase)

        if message.lower() == "/cantada":
           frase = random.choice(cantada)
           await self.highrise.chat(frase)
          
        if        message.startswith("/tele") or              message.startswith("/tp") or              message.startswith("/fly") or     message.startswith("!tele") or      message.startswith("!tp") or     message.startswith("!fly"):
          if user.username in moderators:            await self.teleporter(message)

        if        message.startswith("/") or              message.startswith("-") or              message.startswith(".") or          message.startswith("!"):
            await self.command_handler(user, message)
          
        if message.lower().lstrip().startswith(("!emote list","!list","/list","!lista","/lista","/emote list")):
          await self.highrise.send_whisper(user.id,"🕺🏻Lista de emotes gratis:\n\n1.wrong\n2.fashion\n3.gravity\n4.icecream\n5.casual\n6.kiss\n7.no\n8.sad\n9.yes\n10.laughing\n11.hello\n12.wave\n13.shy\n14.tired\n15.flirtywave\n16.greedy\n17.model\n18.bow\n19.curtsy")

        if message.lower().lstrip().startswith(("!emote list","!list","/list","!lista","/lista","/emote list")):
          await self.highrise.send_whisper(user.id,"\n20.snowball\n21.hot\n22.snowangel\n23.charging\n24.confused\n25.telekinesis\n26.float\n27.teleport\n28.maniac\n29.eneryball\n30.snake\n31.frog\n32.superpose\n33.cute\n34.pose7\n35.pose8\n36.pose1\n37.pose5\n38.pose3")
          await self.highrise.send_whisper(user.id,"\n39.cutey\n40.shuffle\n41.singalong\n42.enthused\n43.letsgoshopping\n44.russian\n45.pennywise\n46.dontstartnow\n47.blackpink\n48.celebrate\n49.gagging\n50.flex\n51.cursing\n52.thumbsup\n53.angry\n54.punk\n55.zombie\n56.sit\n57.fight")

        if message.lower().lstrip().startswith(("!emote list","!list","/list","!lista","/lista","/emote list")):
          await self.highrise.send_whisper(user.id,"\n58.macarena\n59.weird\n60.savage\n61.viralgroove\n62.uwu\n63.sayso\n64.stargazer\n65.pose9\n66.boxer\n67.airguitar\n68.penguin\n69.astronaut\n70.saunter\n71.creepy\n72.watch\n73.revelations\n74.bashful\n75.arabesque\n76.party")
          await self.highrise.send_whisper(user.id,"\n77.skating\n78.scritchy\n79.bitnervous\n80.timejump\n81.gottago\n82.jingle\n83.hyped\n84.sleigh\n85.surprise\n86.repose\n87.kawaii\n88.touch\n89.foryou\n90.pushit\n91.salute\n92.attention\n93.tiktok\n.94.smooch\n95.launch\n96.fairyfloat\n97.fairytwirl\n98.jetpack")
        
        if message.lower().lstrip().startswith(("!emote list","!list","/list","!lista","/lista","/emote list")):
          await self.highrise.send_emote(random.choice(emote))

        if        message.startswith("Feio") or      message.startswith("feio") or      message.startswith("veado") or message.startswith("Veado"):
            await self.highrise.chat(f"REPETE!!! {user.username} 🤬🤬")
            await self.highrise.send_emote("emote-swordfight")

        if        message.startswith("corno") or      message.startswith("Corno") or      message.startswith("Vagabundo") or message.startswith("vagabundo"):
            await self.highrise.chat(f"SEU PAI!!! {user.username} 🤬🤬")
            await self.highrise.send_emote("emote-swordfight")

        if        message.startswith("/pessoas") or      message.startswith("!pessoas"):
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Há  {len(room_users)} pessoas na sala ")
            await self.highrise.send_emote("dance-floss")
                      
        if        message.startswith("gostoso") or      message.startswith("Gostoso") or      message.startswith("GOSTOSO"):
            await self.highrise.send_emote("emote-blowkisses")
            await self.highrise.send_emote("idle-uwu", user.id)
            await self.highrise.chat(f"Voce tambem e gostoso(a) {user.username} 😳👉👈")

        if message.lower().lstrip().startswith(("emotes","!emotes","-emotes","/emotes")):
            await self.highrise.send_whisper(user.id, f"💡 Você pode usar emotes pagos gratuitamente, basta digitar o nome do emote no chat. Exemplo:\n\nswordfight\ngravity\nuwu\n\nPara ver todos os emotes gratuitos, use: !emote list")
            
        if message.lower().lstrip().startswith(("jogos","!jogos","Jogos","/jogos")):
            await self.highrise.send_whisper(user.id, f"🎮Você pode se distrair com esses comandos de jogos, basta digitar o nome do jogo no chat. Exemplo:\n\n/play\n/tarot\n/pescar\n/amor\n/odio\n/loucura\n/rps [pedra|papel|tesoura]\n/moeda [cara ou coroa]\n/ask [sua pergunta]")
    
        if message.lower().lstrip().startswith(("!help","/help","-help","help")):
            await self.highrise.send_whisper(user.id, f"\n💡Está prescisando de ajuda?\n\n!mod\n!jogos\n!general") 

        if message.lower().lstrip().startswith(("!mod","/mod","-mod","mod")):
            await self.highrise.send_whisper(user.id, f"\n💡Comandos de moderadores\n\n!bot\n!say [texto]\n!tipall [quantia]\n!tip @usuario [quantia]\n!tipme [quantia]\n!kick @usuario")
            await self.highrise.send_whisper(user.id, f"!ban @usuario\n!mute @usuario | !unmute @usuario\n!fit [1-11]\n!wallet\n!summon @usuario\n!emote all [emote]\n!emote all random\n/fly @usuario x,y,z\n![heart|wink|wave|clap|thumbs] 1-100")
            
            
        if message.lower().lstrip().startswith(("!general","/general","-general","general")):
            await self.highrise.send_whisper(user.id, f"\n💡General acesso gratuito a todos.\n\n-emote @usuario!\n!emote\n!emote list\n!jogos\ncardapio1\ncardapio2\n!loop [emote|1-98]\n/fly x,y,z\n!follow\n!userinfo @usuario\n!tele @usuario\n![heart|wink|wave|clap|thumbs]  @usuario 1-10")
            
        if        message.startswith("Lindo") or      message.startswith("LINDO") or      message.startswith("lindo"):
            await self.highrise.react("heart",user.id,)
            await self.highrise.chat(f"você tambem e muito lind(a) {user.username} 🥰🥰")
            await self.highrise.send_emote("emote-shy",user.id)
            await self.highrise.send_emote("emote-blowkisses")
          
        if        message.startswith("Bom dia") or      message.startswith("Bom Dia") or      message.startswith("bom dia") or message.startswith("BOM DIA"):
            await self.highrise.send_emote("emote-blowkisses")
            await self.highrise.send_whisper(user.id,f"Bom Dia {user.username} 😊🌅")

        if        message.startswith("Boa noite") or      message.startswith("boa noite") or      message.startswith("Boa Noite") or message.startswith("BOA NOITE"):
            await self.highrise.send_emote("emote-blowkisses")
            await self.highrise.send_whisper(user.id,f"Boa Noite {user.username} 😊🌃🌉")

        if        message.startswith("Boa tarde") or      message.startswith("boa tarde") or      message.startswith("Boa Tarde") or message.startswith("BOA TARDE"):
            await self.highrise.send_emote("emote-blowkisses")
            await self.highrise.send_whisper(user.id,f"Boa Tarde {user.username} ☀️")

        if        message.startswith("😡") or      message.startswith("🤬") or      message.startswith("😤") or             message.startswith("🤨") or             message.startswith("😒") or message.startswith("🙄"):
            await self.highrise.send_emote("emote-boxer",user.id)
   
        if        message.startswith("🤔") or      message.startswith("🧐") or      message.startswith("🥸") or             message.startswith("🫤") or message.startswith("😕"):
            await self.highrise.send_emote("emote-confused",user.id)

        if        message.startswith("🤣") or      message.startswith("😂") or             message.startswith("ja") or             message.startswith("Ha") or         message.startswith("Ka") or           message.startswith("Ja") or           message.startswith("ha") or          message.startswith("ks") or             message.startswith("kk") or             message.startswith("Kk") or message.startswith("😁") or message.startswith("😀"):
            await self.highrise.send_emote("emote-laughing",user.id)

        if        message.startswith("😗") or      message.startswith("😘") or      message.startswith("😙") or             message.startswith("💋") or             message.startswith("😚"):
            await self.highrise.send_emote("emote-kiss",user.id)
            await self.highrise.send_emote("emote-blowkisses")

        if        message.startswith("😊") or      message.startswith("🥰") or      message.startswith("😳") or message.startswith("🤗"):
            await self.highrise.send_emote("idle-uwu",user.id)
            await self.highrise.send_emote("emote-blowkisses")

        if        message.startswith("🤢") or      message.startswith("🤮") or      message.startswith("🤧") or             message.startswith("😵‍💫") or message.startswith("🤒"):
            await self.highrise.send_emote("emoji-gagging",user.id)

        if        message.startswith("😱") or      message.startswith("😬") or      message.startswith("😰") or             message.startswith("😫") or message.startswith("😨"):
            await self.highrise.send_emote("idle-nervous",user.id)

        if        message.startswith("😭") or      message.startswith("🥲") or      message.startswith("😓") or             message.startswith("😔") or message.startswith("😥"):
            await self.highrise.send_emote("emote-sad",user.id)
            
        if message.startswith("🤯"):
            await self.highrise.send_emote("emote-headblowup",user.id)

        if        message.startswith("☺️") or      message.startswith("🫣") or       message.startswith("😍") or      message.startswith("🥺") or message.startswith("🥹"):
            await self.highrise.send_emote("emote-shy2",user.id)

        if        message.startswith("😏") or     message.startswith("🙃") or     message.startswith("🤤") or     message.startswith("😋") or     message.startswith("😏") or message.startswith("😈"):
            await self.highrise.send_emote("emote-lust",user.id)           

        if        message.startswith("🥵") or message.startswith("🫠"):
            await self.highrise.send_emote("emote-hot",user.id)
                   
        if        message.startswith("!wrong") or   message.startswith("wrong") or      message.startswith("/wrong") or      message.startswith("Wrong") or message.startswith("1"):
            await self.highrise.send_emote("dance-wrong",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/fashion") or      message.startswith("fashion") or       message.startswith("!fashion") or      message.startswith("Fashion") or message.startswith("2"):
            await self.highrise.send_emote("emote-fashionista",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/gravity") or      message.startswith("gravity") or       message.startswith("!gravity") or      message.startswith("Gravity") or message.startswith("3"):
            await self.highrise.send_emote("emote-gravity",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/icecream") or                                message.startswith("icecream") or message.startswith("!icecream") or      message.startswith("Icecream") or message.startswith("4"):
            await self.highrise.send_emote("dance-icecream",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/casual") or  message.startswith("casual") or     message.startswith("!casual") or      message.startswith("Casual") or message.startswith("5"):
            await self.highrise.send_emote("idle-dance-casual",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/kiss") or      message.startswith("!kiss") or  message.startswith("kiss") or      message.startswith("Kiss") or message.startswith("6"):
            await self.highrise.send_emote("emote-kiss",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/no") or      message.startswith("no") or            message.startswith("!no") or      message.startswith("No") or message.startswith("7"):
            await self.highrise.send_emote("emote-no",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/sad") or      message.startswith("!sad") or    message.startswith("sad") or     message.startswith("Sad") or message.startswith("8"):
            await self.highrise.send_emote("emote-sad",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/yes") or      message.startswith("!yes") or    message.startswith("yes") or     message.startswith("Yes") or message.startswith("9"):
            await self.highrise.send_emote("emote-yes",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/lau") or   message.startswith("laughing") or   message.startswith("Laughing") or   message.startswith("/laughing") or   message.startswith("!laughing") or      message.startswith("!lau") or    message.startswith("Lau") or     message.startswith("lau") or message.startswith("10"):
            await self.highrise.send_emote("emote-laughing",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/hello") or message.startswith("hello") or      message.startswith("!hello") or      message.startswith("Hello") or message.startswith("11"):
            await self.highrise.send_emote("emote-hello",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/wave") or  message.startswith("wave") or     message.startswith("!wave") or      message.startswith("Wave") or message.startswith("12"):
            await self.highrise.send_emote("emote-wave",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/shy") or   message.startswith("shy") or      message.startswith("!shy") or      message.startswith("Shy") or message.startswith("13"):
            await self.highrise.send_emote("emote-shy",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/tired") or message.startswith("tired") or      message.startswith("!tired") or      message.startswith("Tired") or message.startswith("14"):
            await self.highrise.send_emote("emote-tired",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/flirt") or message.startswith("flirt") or message.startswith("flirtywave") or message.startswith("flirty") or      message.startswith("!flirt") or      message.startswith("Flirt") or          message.startswith("/Flirty") or           message.startswith("!Flirty") or           message.startswith("Flirty") or       message.startswith("!flirtywave") or    message.startswith("/flirtywave") or    message.startswith("Flirtywave") or message.startswith("15"):
            await self.highrise.send_emote("emote-lust",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/greedy") or      message.startswith("!greedy") or      message.startswith("Greedy") or message.startswith("greedy") or message.startswith("16"):
            await self.highrise.send_emote("emote-greedy",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/model") or      message.startswith("!model") or      message.startswith("Model") or  message.startswith("model") or message.startswith("17"):
            await self.highrise.send_emote("emote-model",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/bow") or      message.startswith("!bow") or      message.startswith("Bow") or    message.startswith("bow") or message.startswith("18"):
            await self.highrise.send_emote("emote-bow",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/curtsy") or      message.startswith("!curtsy") or      message.startswith("Curtsy") or message.startswith("curtsy") or message.startswith("19"):
            await self.highrise.send_emote("emote-curtsy",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/snowball") or      message.startswith("!snowball") or      message.startswith("Snowball") or                              message.startswith("snowball") or message.startswith("20"):
            await self.highrise.send_emote("emote-snowball",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/hot") or      message.startswith("!hot") or      message.startswith("Hot") or    message.startswith("hot") or message.startswith("21"):
            await self.highrise.send_emote("emote-hot",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/snowangel") or      message.startswith("!snowangel") or      message.startswith("Snowangel") or                              message.startswith("snowangel") or message.startswith("22"):
            await self.highrise.send_emote("emote-snowangel",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/charging") or      message.startswith("!charging") or      message.startswith("Charging") or                              message.startswith("charging") or message.startswith("23"):
            await self.highrise.send_emote("emote-charging",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/confused") or      message.startswith("!confused") or      message.startswith("Confused") or                              message.startswith("confused") or message.startswith("24"):
            await self.highrise.send_emote("emote-confused",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/telekinesis") or      message.startswith("!telekinesis") or      message.startswith("Telekinesis") or                            message.startswith("telekinesis") or message.startswith("25"):
            await self.highrise.send_emote("emote-telekinesis",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/float") or      message.startswith("!float") or      message.startswith("Float") or  message.startswith("float") or message.startswith("26"):
            await self.highrise.send_emote("emote-float",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/teleport") or      message.startswith("!teleport") or      message.startswith("Teleport") or                              message.startswith("teleport") or      message.startswith("27"):
            await self.highrise.send_emote("emote-teleporting",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/maniac") or      message.startswith("!maniac") or      message.startswith("Maniac") or message.startswith("maniac") or message.startswith("28"):
            await self.highrise.send_emote("emote-maniac",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/energyball") or      message.startswith("!energyball") or      message.startswith("Energyball") or                             message.startswith("eneryball") or message.startswith("29"):
            await self.highrise.send_emote("emote-energyball",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/snake") or      message.startswith("!snake") or      message.startswith("Snake") or  message.startswith("snake") or message.startswith("30"):
            await self.highrise.send_emote("emote-snake",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/frog") or      message.startswith("!frog") or      message.startswith("Frog") or   message.startswith("frog") or message.startswith("31"):
            await self.highrise.send_emote("emote-frog",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/superpose") or      message.startswith("!superpose") or      message.startswith("Superpose") or                              message.startswith("superpose") or message.startswith("32"):
            await self.highrise.send_emote("emote-superpose",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/cute") or      message.startswith("!cute") or      message.startswith("Cute") or   message.startswith("cute") or message.startswith("33"):
            await self.highrise.send_emote("emote-cute",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/pose7") or      message.startswith("!pose7") or      message.startswith("Pose7") or  message.startswith("pose7") or message.startswith("34"):
            await self.highrise.send_emote("emote-pose7",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/pose8") or      message.startswith("!pose8") or      message.startswith("Pose8") or  message.startswith("pose8") or message.startswith("35"):
            await self.highrise.send_emote("emote-pose8",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/pose1") or      message.startswith("!pose1") or      message.startswith("Pose1") or  message.startswith("pose1") or message.startswith("36"):
            await self.highrise.send_emote("emote-pose1",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/pose5") or      message.startswith("!pose5") or      message.startswith("Pose5") or  message.startswith("pose5") or message.startswith("37"):
            await self.highrise.send_emote("emote-pose5",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/pose3") or      message.startswith("!pose3") or      message.startswith("Pose3") or  message.startswith("pose3") or message.startswith("38"):
            await self.highrise.send_emote("emote-pose3",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/cutey") or      message.startswith("!cutey") or      message.startswith("Cutey") or  message.startswith("cutey") or message.startswith("39"):
            await self.highrise.send_emote("emote-cutey",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/tik10") or    message.startswith("shuffle") or    message.startswith("Shuffle") or   message.startswith("!shuffle") or    message.startswith("/shuffle") or    message.startswith("!tik10") or      message.startswith("Tik10") or  message.startswith("tik10") or message.startswith("40"):
            await self.highrise.send_emote("dance-tiktok10",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/sing") or      message.startswith("!sing") or          message.startswith("Sing") or           message.startswith("Singing") or       message.startswith("/singing") or   message.startswith("!singing") or                              message.startswith("singing") or                              message.startswith("!singalong")  or                             message.startswith("/singalong") or message.startswith("Singalong") or                             message.startswith("singalong") or message.startswith("41"):
            await self.highrise.send_emote("idle_singing",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/enthused") or      message.startswith("!enthused") or      message.startswith("Enthused") or                              message.startswith("enthused") or message.startswith("42"):
            await self.highrise.send_emote("idle-enthusiastic",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/shop") or      message.startswith("Letsgoshopping") or      message.startswith("letsgoshopping") or      message.startswith("/letsgoshopping") or      message.startswith("!letsgoshopping") or    message.startswith("!shop") or      message.startswith("Shop") or   message.startswith("shop") or   message.startswith("!shopping") or message.startswith("/shopping") or message.startswith("Shopping") or message.startswith("shopping") or message.startswith("43"):
            await self.highrise.send_emote("dance-shoppingcart",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/russian") or      message.startswith("!russian") or      message.startswith("Russian") or                              message.startswith("russian") or message.startswith("44"):
            await self.highrise.send_emote("dance-russian",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/pennywise") or      message.startswith("!pennywise") or      message.startswith("Pennywise") or                              message.startswith("pennywise") or message.startswith("45"):
            await self.highrise.send_emote("dance-pennywise",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/tik2") or      message.startswith("!tik2") or      message.startswith("Tik2") or   message.startswith("!dontstartnow") or   message.startswith("/dontstartnow") or   message.startswith("dontstartnow") or   message.startswith("Dontstartnow") or   message.startswith("tik2") or   message.startswith("46"):
            await self.highrise.send_emote("dance-tiktok2",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/blackpink") or      message.startswith("!blackpink") or      message.startswith("Blackpink") or                              message.startswith("blackpink") or message.startswith("47"):
            await self.highrise.send_emote("dance-blackpink",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/celebrate") or      message.startswith("!celebrate") or      message.startswith("Celebrate") or                              message.startswith("celebrate") or message.startswith("48"):
            await self.highrise.send_emote("emoji-celebrate",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/gagging") or      message.startswith("!gagging") or      message.startswith("Gagging") or                              message.startswith("gagging") or message.startswith("49"):
            await self.highrise.send_emote("emoji-gagging",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/flex") or      message.startswith("!flex") or      message.startswith("Flex") or   message.startswith("flex") or message.startswith("50"):
            await self.highrise.send_emote("emoji-flex",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/cursing") or      message.startswith("!cursing") or      message.startswith("Cursing") or                              message.startswith("cursing") or message.startswith("51"):
            await self.highrise.send_emote("emoji-cursing",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/thumbsup") or      message.startswith("!thumbsup") or      message.startswith("Thumbsup") or                              message.startswith("thumbsup") or message.startswith("52"):
            await self.highrise.send_emote("emoji-thumbsup",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/angry") or      message.startswith("!angry") or      message.startswith("Angry") or  message.startswith("angry") or message.startswith("53"):
            await self.highrise.send_emote("emoji-angry",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/punk") or      message.startswith("!punk") or      message.startswith("Punk") or   message.startswith("punk") or message.startswith("54"):
            await self.highrise.send_emote("emote-punkguitar",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/zombie") or      message.startswith("!zombie") or      message.startswith("Zombie") or message.startswith("zombie") or message.startswith("55"):
            await self.highrise.send_emote("emote-zombierun",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/sit") or      message.startswith("!sit") or      message.startswith("Sit") or    message.startswith("sit") or message.startswith("56"):
            await self.highrise.send_emote("idle-loop-sitfloor",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/fight") or      message.startswith("!fight") or      message.startswith("Fight") or  message.startswith("fight") or  message.startswith("!swordfight") or message.startswith("/swordfight") or message.startswith("Swordfight") or message.startswith("swordfight") or message.startswith("57"):
            await self.highrise.send_emote("emote-swordfight",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/ren") or      message.startswith("!ren") or      message.startswith("Ren") or    message.startswith("ren") or    message.startswith("!macarena") or     message.startswith("/macarena") or      message.startswith("Macarena") or message.startswith("macarena") or message.startswith("58"):
            await self.highrise.send_emote("dance-macarena",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/wei") or      message.startswith("!wei") or      message.startswith("Wei") or    message.startswith("wei") or message.startswith("!weird") or message.startswith("/weird") or message.startswith("Weird") or message.startswith("weird") or  message.startswith("59"):
            await self.highrise.send_emote("dance-weird",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/tik8") or      message.startswith("!tik8") or      message.startswith("Tik8") or           message.startswith("/savage") or           message.startswith("!savage") or           message.startswith("Savage") or message.startswith("tik8") or message.startswith("savage") or message.startswith("60"):
            await self.highrise.send_emote("dance-tiktok8",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/tik9") or      message.startswith("!tik9") or      message.startswith("Tik9") or           message.startswith("/viral") or           message.startswith("!viral") or           message.startswith("Viral") or  message.startswith("!viralgroove") or message.startswith("/viralgroove") or message.startswith("Viralgroove") or message.startswith("viralgroove") or message.startswith("tik9") or message.startswith("viral") or message.startswith("61"):
            await self.highrise.send_emote("dance-tiktok9",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/uwu") or      message.startswith("!uwu") or      message.startswith("Uwu") or    message.startswith("uwu") or message.startswith("62"):
            await self.highrise.send_emote("idle-uwu",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/tik4") or      message.startswith("!tik4") or      message.startswith("Tik4") or               message.startswith("/sayso") or               message.startswith("!sayso") or               message.startswith("Sayso") or  message.startswith("sayso") or message.startswith("tik4") or message.startswith("63"):
            await self.highrise.send_emote("idle-dance-tiktok4",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/star") or    message.startswith("star") or     message.startswith("!star") or      message.startswith("Star") or   message.startswith("!stargazer") or     message.startswith("/stargazer") or   message.startswith("Stargazer") or   message.startswith("stargazer") or message.startswith("64"):
            await self.highrise.send_emote("emote-stargazer",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/pose9") or      message.startswith("!pose9") or      message.startswith("Pose9") or  message.startswith("pose9") or message.startswith("65"):
            await self.highrise.send_emote("emote-pose9",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/boxer") or      message.startswith("!boxer") or      message.startswith("Boxer") or  message.startswith("boxer") or message.startswith("66"):
            await self.highrise.send_emote("emote-boxer",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/airguitar") or    message.startswith("!airguitar") or     message.startswith("airguitar") or      message.startswith("Airguitar") or   message.startswith("Guitar") or     message.startswith("guitar") or   message.startswith("!guitar") or   message.startswith("/guitar") or message.startswith("67"):
            await self.highrise.send_emote("idle-guitar",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/penguin") or      message.startswith("!penguin") or      message.startswith("Penguin") or   message.startswith("penguin") or message.startswith("68"):
            await self.highrise.send_emote("dance-pinguin",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/astronaut") or      message.startswith("!astronaut") or      message.startswith("Astronaut") or                                message.startswith("astronaut") or message.startswith("69"):
            await self.highrise.send_emote("emote-astronaut",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/saunter") or      message.startswith("!saunter") or      message.startswith("Saunter") or               message.startswith("/anime") or               message.startswith("!anime") or               message.startswith("Anime") or    message.startswith("anime") or   message.startswith("saunter") or   message.startswith("70"):
            await self.highrise.send_emote("dance-anime",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/creepy") or      message.startswith("!creepy") or      message.startswith("Creepy") or   message.startswith("creepy") or message.startswith("71"):
            await self.highrise.send_emote("dance-creepypuppet",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/watch") or      message.startswith("!watch") or      message.startswith("Watch") or    message.startswith("watch") or message.startswith("72"):
            await self.highrise.send_emote("emote-creepycute",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/revelations") or      message.startswith("!revelations") or      message.startswith("Revelations") or                                message.startswith("revelations") or message.startswith("73"):
            await self.highrise.send_emote("emote-headblowup",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/bashful") or      message.startswith("!bashful") or      message.startswith("Bashful") or  message.startswith("bashful") or message.startswith("74"):
            await self.highrise.send_emote("emote-shy2",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/arabesque") or      message.startswith("!arabesque") or      message.startswith("Arabesque") or                                message.startswith("arabesque") or message.startswith("75"):
            await self.highrise.send_emote("emote-pose10",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/party") or      message.startswith("!party") or      message.startswith("Party") or    message.startswith("party") or message.startswith("76"):
            await self.highrise.send_emote("emote-celebrate",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/skating") or      message.startswith("!skating") or      message.startswith("Skating") or  message.startswith("skating") or message.startswith("77"):
            await self.highrise.send_emote("emote-iceskating",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/scritchy") or      message.startswith("!scritchy") or      message.startswith("Scritchy") or message.startswith("scritchy") or message.startswith("78"):
            await self.highrise.send_emote("idle-wild",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/bitnervous") or      message.startswith("!bitnervous") or      message.startswith("Bitnervous") or               message.startswith("!nervous") or               message.startswith("/nervous") or               message.startswith("Nervous") or  message.startswith("nervous") or   message.startswith("bitnervous") or message.startswith("79"):
            await self.highrise.send_emote("idle-nervous",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/timejump") or      message.startswith("!timejump") or      message.startswith("Timejump") or message.startswith("timejump") or message.startswith("time") or   message.startswith("Time") or   message.startswith("!time") or   message.startswith("/time") or message.startswith("80"):
            await self.highrise.send_emote("emote-timejump",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/gottago") or      message.startswith("!gottago") or      message.startswith("Gottago") or message.startswith("gottago") or  message.startswith("81"):
            await self.highrise.send_emote("idle-toilet",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/jingle") or      message.startswith("!jingle") or      message.startswith("Jingle") or  message.startswith("jingle") or message.startswith("82"):
            await self.highrise.send_emote("dance-jinglebell",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/hyped") or      message.startswith("!hyped") or      message.startswith("Hyped") or   message.startswith("hyped") or message.startswith("83"):
            await self.highrise.send_emote("emote-hyped",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/sleigh") or      message.startswith("!sleigh") or        message.startswith("sleigh") or      message.startswith("Sleigh") or message.startswith("84"):
            await self.highrise.send_emote("emote-sleigh",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/surprise") or      message.startswith("!surprise") or      message.startswith("surprise") or      message.startswith("Surprise") or message.startswith("85"):
            await self.highrise.send_emote("emote-pose6",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")
          
        if        message.startswith("/repose") or      message.startswith("!repose") or        message.startswith("repose") or      message.startswith("Repose") or message.startswith("86"):
            await self.highrise.send_emote("sit-relaxed",user.id)
            await self.highrise.chat(f" Você vai gostar desse emote {user.username} 😍")

        if        message.startswith("/kawaii") or      message.startswith("!kawaii") or        message.startswith("kawaii") or       message.startswith("Kawaii") or message.startswith("87"):
            await self.highrise.send_emote("dance-kawai",user.id)

        if        message.startswith("/touch") or      message.startswith("!touch") or         message.startswith("touch") or      message.startswith("Touch") or message.startswith("88"):
            await self.highrise.send_emote("dance-touch",user.id)

        if        message.startswith("/foryou") or    message.startswith("!foryou") or  message.startswith("foryou") or   message.startswith("Foryou") or   message.startswith("/gift") or      message.startswith("!gift") or          message.startswith("gift") or      message.startswith("Gift") or message.startswith("89"):
            await self.highrise.send_emote("emote-gift",user.id)

        if        message.startswith("/pushit") or      message.startswith("!pushit") or        message.startswith("pushit") or      message.startswith("Pushit") or message.startswith("90"):
            await self.highrise.send_emote("dance-employee",user.id)

        if        message.startswith("salute") or      message.startswith("!salute") or        message.startswith("salute") or      message.startswith("Salute") or message.startswith("91"):
            await self.highrise.send_emote("emote-cutesalute",user.id)

        if        message.startswith("/attention") or      message.startswith("!attention") or        message.startswith("attention") or      message.startswith("Attention") or message.startswith("92"):
            await self.highrise.send_emote("emote-salute",user.id)                                                                   

        if        message.startswith("/tiktok") or      message.startswith("!tiktok") or        message.startswith("tiktok") or    message.startswith("Tiktok") or message.startswith("93"):
            await self.highrise.send_emote("dance-tiktok11",user.id)

        if        message.startswith("/smooch") or      message.startswith("!smooch") or        message.startswith("smooch") or    message.startswith("Smooch") or message.startswith("94"):
            await self.highrise.send_emote("emote-kissing-bound",user.id)

        if        message.startswith("/launch") or      message.startswith("!launch") or        message.startswith("launch") or   message.startswith("Launch") or message.startswith("95"):
            await self.highrise.send_emote("emote-launch",user.id)

        if        message.startswith("/fairyfloat") or      message.startswith("!fairyfloat") or        message.startswith("fairyfloat") or    message.startswith("Fairyfloat") or message.startswith("96"):
            await self.highrise.send_emote("idle-floating",user.id)

        if        message.startswith("/fairytwirl") or      message.startswith("!fairytwirl") or        message.startswith("fairytwirl") or    message.startswith("Fairytwirl") or message.startswith("97"):
            await self.highrise.send_emote("emote-looping",user.id)

        if        message.startswith("/jetpack") or      message.startswith("!jetpack") or        message.startswith("jetpack") or    message.startswith("Jetpack") or message.startswith("98"):
            await self.highrise.send_emote("hcc-jetpack",user.id)
              
        if              message.startswith("!emote all random") or                              message.startswith("/emote all random"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote(random.choice(emote), roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Random Emotes] para {len(room_users)} pessoas.")

        if              message.startswith("Jetpack All") or                              message.startswith("/emote all jetpack") or       message.startswith("!emote all jetpack"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("hcc-jetpack", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Jetpack] para {len(room_users)} pessoas.")

        if              message.startswith("Fairyfloat All") or                              message.startswith("/emote all fairyfloat") or       message.startswith("!emote all fairyfloat"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-floating", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Fairyfloat] para {len(room_users)} pessoas.")

        if              message.startswith("Fairytwirl All") or                              message.startswith("/emote all fairytwirl") or       message.startswith("!emote all fairytwirl"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-looping", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Fairytwirl] para {len(room_users)} pessoas.")

        if              message.startswith("Launch All") or                              message.startswith("/emote all launch") or       message.startswith("!emote all launch"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-launch", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Launch] para {len(room_users)} pessoas.")

        if              message.startswith("Smooch All") or                              message.startswith("/emote all smooch") or       message.startswith("!emote all smooch"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-kissing-bound", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Smooch] para {len(room_users)} pessoas.")

        if              message.startswith("Pushit All") or                              message.startswith("/emote all pushit") or       message.startswith("!emote all pushit"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-employee", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Pushit] para {len(room_users)} pessoas.")

        if              message.startswith("Gift All") or                              message.startswith("/emote all gift") or       message.startswith("!emote all gift"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-gift", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Gift] para {len(room_users)} pessoas.")

        if              message.startswith("Attention All") or                              message.startswith("/emote all attention") or       message.startswith("!emote all attention"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-salute", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Attention] para {len(room_users)} pessoas.")

        if              message.startswith("Salute All") or                              message.startswith("/emote all salute") or       message.startswith("!emote all salute"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-cutesalute", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Salute] para {len(room_users)} pessoas.")

        if              message.startswith("Tiktok All") or                              message.startswith("/emote all tiktok") or       message.startswith("!emote all tiktok"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok11", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Tiktok] para {len(room_users)} pessoas.")
          
        if              message.startswith("Touch All") or                              message.startswith("/emote all touch") or       message.startswith("!emote all touch"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-touch", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Touch] para {len(room_users)} pessoas.")
              
        if              message.startswith("Kawaii All") or                              message.startswith("/emote all kawaii") or       message.startswith("!emote all kawaii"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-kawai", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Kawaii] para {len(room_users)} pessoas.")
          
        if              message.startswith("Hot All") or                              message.startswith("/emote all hot") or       message.startswith("!emote all hot"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-hot", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Hot] para {len(room_users)} pessoas.")
      
      
        if              message.startswith("Curtsy All") or                              message.startswith("/emote all curtsy") or       message.startswith("!emote all curtsy"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-curtsy", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Curtsy] para {len(room_users)} pessoas.")

        if              message.startswith("Surprise All") or                              message.startswith("/emote all surprise") or       message.startswith("!emote all surprise"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose6", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Surprise] para {len(room_users)} pessoas.")

        if              message.startswith("Jingle All") or                              message.startswith("/emote all jingle") or       message.startswith("!emote all jingle"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-jinglebell", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Jingle] para {len(room_users)} pessoas.")

        if              message.startswith("Creepy All") or                              message.startswith("/emote all creepy") or       message.startswith("!emote all creepy"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-creepypuppet", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Creepy] para {len(room_users)} pessoas.")

        if              message.startswith("Nervous All") or message.startswith("Bitnervous All") or      message.startswith("!emote all bitnervous") or message.startswith("/emote all bitnervous") or                             message.startswith("/emote all nervous") or       message.startswith("!emote all nervous"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-nervous", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Bitnervous] para {len(room_users)} pessoas.")

        if              message.startswith("Scritchy All") or                              message.startswith("/emote all scritchy") or       message.startswith("!emote all scritchy"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-wild", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Scritchy] para {len(room_users)} pessoas.")
              
        if              message.startswith("Fashion All") or                              message.startswith("/emote all fashion") or       message.startswith("!emote all fashion"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-fashionista", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Fashion] para {len(room_users)} pessoas.")
                
        if              message.startswith("Wrong All") or                              message.startswith("/emote all wrong") or       message.startswith("!emote all wrong"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-wrong", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Wrong] para {len(room_users)} pessoas.")

        if              message.startswith("Cutey All") or                              message.startswith("/emote all cutey") or       message.startswith("!emote all cutey"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-cutey", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Cutey] para {len(room_users)} pessoas.")

        if              message.startswith("Hyped All") or                              message.startswith("/emote all hyped") or       message.startswith("!emote all hyped"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-hyped", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Hyped] para {len(room_users)} pessoas.")
                
        if              message.startswith("Superpose All") or                              message.startswith("/emote all superpose") or       message.startswith("!emote all superpose"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-superpose", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Superpose] para {len(room_users)} pessoas.")

        if              message.startswith("Punk All") or                              message.startswith("/emote all punk") or       message.startswith("!emote all punk"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-punkguitar", roomUser.id) 
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Punk] para {len(room_users)} pessoas.")
                
        if              message.startswith("Dontstartnow All") or message.startswith("Tiktok2 All") or      message.startswith("!emote all dontstartnow") or message.startswith("/emote all dontstartnow") or                             message.startswith("/emote all tiktok2") or       message.startswith("!emote all tiktok2"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok2", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Dontstartnow] para {len(room_users)} pessoas.")
                
                
        if              message.startswith("Savage All") or message.startswith("Tiktok8 All") or      message.startswith("!emote all savage") or message.startswith("/emote all savage") or                             message.startswith("/emote all tiktok8") or       message.startswith("!emote all tiktok8"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok8", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Savage] para {len(room_users)} pessoas.")
                
        if              message.startswith("Tiktok10 All") or                              message.startswith("/emote all tiktok10") or       message.startswith("!emote all tiktok10"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok10", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Tiktok10] para {len(room_users)} pessoas.")
                
        if              message.startswith("Viral All") or     message.startswith("!emotr all tiktok9") or        message.startswith("/emote all tiktok9") or    message.startswith("Tiktok9 All") or message.startswith("Viralgroove All") or      message.startswith("!emote all viral") or message.startswith("/emote all viralgroove") or                             message.startswith("/emote all viral") or       message.startswith("!emote all viralgroove"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok9", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Viralgroove] para {len(room_users)} pessoas.")
                
        if              message.startswith("Blackpink All") or                              message.startswith("/emote all blackpink") or       message.startswith("!emote all blackpink"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-blackpink", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Blackpink] para {len(room_users)} pessoas.")
                
        if              message.startswith("Gagging All") or                              message.startswith("/emote all gagging") or       message.startswith("!emote all gagging"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emoji-gagging", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Gagging] para {len(room_users)} pessoas.")

        if              message.startswith("Pose3 All") or                              message.startswith("/emote all pose3") or       message.startswith("!emote all pose3"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose3", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Pose3] para {len(room_users)} pessoas.")

        if              message.startswith("Pose7 All") or                              message.startswith("/emote all pose7") or       message.startswith("!emote all pose7"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose7", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Pose7] para {len(room_users)} pessoas.")

        if              message.startswith("Pose5 All") or                              message.startswith("/emote all pose5") or       message.startswith("!emote all pose5"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose5", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Pose5] para {len(room_users)} pessoas.")

        if              message.startswith("Pose1 All") or                              message.startswith("/emote all pose1") or       message.startswith("!emote all pose1"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose1", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Pose1] para {len(room_users)} pessoas.")

        if              message.startswith("Pose8 All") or                              message.startswith("/emote all pose8") or       message.startswith("!emote all pose8"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose8", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Pose8] para {len(room_users)} pessoas.")
     
        if              message.startswith("Enthused All") or                              message.startswith("/emote all enthused") or       message.startswith("!emote all enthused"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-enthusiastic", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Enthused] para {len(room_users)} pessoas.")
                
        if              message.startswith("Singing All") or message.startswith("Sing All") or      message.startswith("!emote all sing") or message.startswith("/emote all sing") or                             message.startswith("/emote all singing") or       message.startswith("!emote all singing"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle_singing", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Singing] para {len(room_users)} pessoas.")

        if              message.startswith("Teleport All") or                              message.startswith("/emote all teleport") or       message.startswith("!emote all teleport"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-teleporting", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Teleporting] para {len(room_users)} pessoas.")
                
        if              message.startswith("Telekinesis All") or                              message.startswith("/emote all telekinesis") or       message.startswith("!emote all telekinesis"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-telekinesis", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Telekinesis] para {len(room_users)} pessoas.")

        if              message.startswith("Casual All") or                              message.startswith("/emote all casual") or       message.startswith("!emote all casual"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-dance-casual", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Casual] para {len(room_users)} pessoas.")
                
        if              message.startswith("Icecream All") or                              message.startswith("/emote all icecream") or       message.startswith("!emote all icecream"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-icecream", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Icecream] para {len(room_users)} pessoas.")
                   
        if              message.startswith("Zombie All") or                              message.startswith("/emote all zombie") or       message.startswith("!emote all zombie"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-zombierun", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Zombie] para {len(room_users)} pessoas.")

        if              message.startswith("Celebrate All") or                              message.startswith("/emote all celebrate") or       message.startswith("!emote all celebrate"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emoji-celebrate", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Celebrate] para {len(room_users)} pessoas.")

        if              message.startswith("Kiss All") or                              message.startswith("/emote all kiss") or       message.startswith("!emote all kiss"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-kiss", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Kiss] para {len(room_users)} pessoas.")

        if              message.startswith("Snowangel All") or                              message.startswith("/emote all snowangel") or       message.startswith("!emote all snowangel"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-snowangel", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Snowangel] para {len(room_users)} pessoas.")

        if              message.startswith("Bow All") or                              message.startswith("/emote all bow") or       message.startswith("!emote all bow"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-bow", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Bow] para {len(room_users)} pessoas.")

        if              message.startswith("Ice All") or message.startswith("Skating All") or      message.startswith("!emote all ice") or message.startswith("/emote all skating") or                             message.startswith("/emote all ice") or       message.startswith("!emote all skating"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-iceskating", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Iceskating] para {len(room_users)} pessoas.")

        if              message.startswith("Confused All") or                              message.startswith("/emote all confused") or       message.startswith("!emote all confused"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-confused", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Confused] para {len(room_users)} pessoas.")

        if              message.startswith("Charging All") or                              message.startswith("/emote all charging") or       message.startswith("!emote all charging"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-charging", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Charging] para {len(room_users)} pessoas.")

        if              message.startswith("Weird All") or message.startswith("Wei All") or      message.startswith("!emote all wei") or message.startswith("/emote all wei") or                             message.startswith("/emote all weird") or       message.startswith("!emote all weird"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-weird", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Weird] para {len(room_users)} pessoas.")

        if              message.startswith("Greedy All") or                              message.startswith("/emote all greedy") or       message.startswith("!emote all greedy"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-greedy", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Greedy] para {len(room_users)} pessoas.")

        if              message.startswith("Cursing All") or                              message.startswith("/emote all cursing") or       message.startswith("!emote all cursing"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emoji-cursing", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Cursing] para {len(room_users)} pessoas.")

        if              message.startswith("Russian All") or                              message.startswith("/emote all russian") or       message.startswith("!emote all russian"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-russian", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Russian] para {len(room_users)} pessoas.")

        if              message.startswith("Repose All") or                              message.startswith("/emote all repose") or       message.startswith("!emote all repose"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("sit-relaxed", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Repose] para {len(room_users)} pessoas.")
                
        if              message.startswith("Shop All") or message.startswith("Shopping All") or      message.startswith("!emote all shopping") or message.startswith("/emote all shop") or                             message.startswith("/emote all shopping") or       message.startswith("!emote all shop"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-shoppingcart", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Shopping] para {len(room_users)} pessoas.")

        if              message.startswith("Macarena All") or message.startswith("Ren All") or      message.startswith("!emote all macarena") or message.startswith("/emote all macarena") or                             message.startswith("/emote all ren") or       message.startswith("!emote all   ren "):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-macarena", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Macarena] para {len(room_users)} pessoas.")

        if              message.startswith("Snake All") or                              message.startswith("/emote all snake") or       message.startswith("!emote all snake"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-snake", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Snake] para {len(room_users)} pessoas.")

        if              message.startswith("Model All") or                              message.startswith("/emote all model") or       message.startswith("!emote all model"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-model", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Model] para {len(room_users)} pessoas.")

        if              message.startswith("Sleigh All") or                              message.startswith("/emote all sleigh") or       message.startswith("!emote all sleigh"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-sleigh", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Sleigh] para {len(room_users)} pessoas.")

        if              message.startswith("Sayso All") or message.startswith("Tiktok4 All") or      message.startswith("!emote all sayso") or message.startswith("/emote all sayso") or                             message.startswith("/emote all tiktok4") or       message.startswith("!emote all tiktok4"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-dance-tiktok4", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Sayso] para {len(room_users)} pessoas.")

        if              message.startswith("Uwu All") or                              message.startswith("/emote all uwu") or       message.startswith("!emote all uwu"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-uwu", roomUser.id)
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Uwu] para {len(room_users)} pessoas.")

        if              message.startswith("Star All") or                              message.startswith("/emote all star") or       message.startswith("!emote all star"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-stargazer", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Stargazer] para {len(room_users)} pessoas.")

        if              message.startswith("Pose9 All") or                              message.startswith("/emote all pose9") or       message.startswith("!emote all pose9"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose9", roomUser.id)
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Pose9] para {len(room_users)} pessoas.")

        if              message.startswith("Boxer All") or                              message.startswith("/emote all boxer") or       message.startswith("!emote all boxer"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-boxer", roomUser.id)
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Boxer] para {len(room_users)} pessoas.")

        if              message.startswith("Airguitar All") or message.startswith("Guitar All") or      message.startswith("!emote all guitar") or message.startswith("/emote all airguitar") or                             message.startswith("/emote all guitar") or       message.startswith("!emote all airguitar"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-guitar", roomUser.id)
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Airguitar] para {len(room_users)} pessoas.")

        if              message.startswith("Penguin All") or message.startswith("Pinguin All") or      message.startswith("!emote all penguin") or message.startswith("/emote all penguin") or                             message.startswith("/emote all pinguin") or       message.startswith("!emote all pinguin"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-pinguin", roomUser.id)
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Penguin] para {len(room_users)} pessoas.")
            
        if              message.startswith("Astronaut All") or message.startswith("Zero All") or      message.startswith("!emote all zero") or message.startswith("/emote all zero") or                             message.startswith("/emote all astronaut") or       message.startswith("!emote all astronaut"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-astronaut", roomUser.id)
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Astronaut] para {len(room_users)} pessoas.")
                
        if              message.startswith("Saunter All") or   message.startswith("Anime All") or   message.startswith("!emote all anime") or   message.startswith("/emote all anime") or                              message.startswith("/emote all saunter") or       message.startswith("!emote all saunter"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-anime", roomUser.id)
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Saunter] para {len(room_users)} pessoas.")

        if              message.startswith("Flirt All") or     message.startswith("!emote all flirt") or    message.startswith("/emote all flirt") or    message.startswith("!emote all flirty") or     message.startswith("Flirtywave All") or    message.startswith("/emote all flirty") or    message.startswith("/emote all flirt") or                               message.startswith("/emote all flirtywave") or       message.startswith("!emote all flirtywave"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-lust", roomUser.id)
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Flirtywave] para {len(room_users)} pessoas.")

        if              message.startswith("Watch All") or                              message.startswith("/emote all watch") or       message.startswith("!emote all watch"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-creepycute", roomUser.id)
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Watch] para {len(room_users)} pessoas.")
              
        if              message.startswith("Revelations All") or                              message.startswith("/emote all revelations") or       message.startswith("!emote all revelations"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-headblowup", roomUser.id)
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Revelations] para {len(room_users)} pessoas.")
              
        if              message.startswith("Bashful All") or                              message.startswith("/emote all bashful") or       message.startswith("!emote all bashful"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-shy2", roomUser.id)
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Bashful] para {len(room_users)} pessoas.")

        if              message.startswith("Arabesque All") or                              message.startswith("/emote all arabesque") or       message.startswith("!emote all arabesque"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose10", roomUser.id)
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Arabesque] para {len(room_users)} pessoas.")
        
        if              message.startswith("Party All") or                              message.startswith("/emote all party") or       message.startswith("!emote all party"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-celebrate", roomUser.id)
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Party] para {len(room_users)} pessoas.")
              
        if              message.startswith("Time All") or                              message.startswith("/emote all time") or       message.startswith("!emote all time"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-timejump", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Time] para {len(room_users)} pessoas.")

        if              message.startswith("Gottago All") or                              message.startswith("/emote all gottago") or       message.startswith("!emote all gottago"):
          if user.username in moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-toilet", roomUser.id)
                room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"Enviando [Gottago] para {len(room_users)} pessoas.")
                  
        if message.startswith("/cardapio1"):
            await self.highrise.send_whisper(user.id,"esse é o nosso cardapio de bebidas espero que goste 😄")
                                     
        if message.startswith("/cardapio1"):
            await self.highrise.send_whisper(user.id,"/tequila , /gim , /vinho , /vinho-branco , /vodka , /whisky , /rum , /champanhe , /cachaça /conhaque , /cerveja , /coca-cola , /suco , /agua , /agua-de-coco , /toddy , /nescau")

        if message.startswith("/coca-cola"):  
            await self.highrise.send_whisper(user.id,f"{user.username} aqui está sua deliciosa coca cola gelada 🧊🥤 ")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/toddy"):  
            await self.highrise.send_whisper(user.id,f"{user.username} aki está seu delicioso toddy 🥛")
            await self.highrise.react("thumbs", user.id)
          
        if message.startswith("/suco"):  
            await self.highrise.send_whisper(user.id,f"{user.username} aqui está seu delicioso suco natural 🧃")
            await self.highrise.react("thumbs", user.id)
        if message.startswith("/agua"):  
            await self.highrise.send_whisper(user.id,f"🌊aqui está sua deliciosa agua {user.username} diretamente da toneira 🌊")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/agua-de-coco"):  
            await self.highrise.send_whisper(user.id,f"🥥aki está sua aguá de coco {user.username} aproveite que está deliciosa 🥥")
            await self.highrise.react("thumbs", user.id)
          
        if message.startswith("/nescau"):  
            await self.highrise.send_whisper(user.id,f"aqui está {user.username} seu delicioso nescau 🥛")
            await self.highrise.react("thumbs", user.id)
          
        if message.startswith("/tequila"):  
            await self.highrise.send_whisper(user.id,f"{user.username} se deliciando na Tequila 😄🥃")
            await self.highrise.react("thumbs", user.id)
          
        if message.startswith("/gim"):
            await self.highrise.send_whisper(user.id,f"vira vira todo o gim {user.username} 🥃")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/conhaque"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Seu conhaque {user.username} 🥃🥃")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/whisky"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está seu Whisky  {user.username} 🥃")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/rum"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está seu Rum 🥃 {user.username}")
            await self.highrise.react("thumbs", user.id)
          
        if message.startswith("/cachaça"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está a Sua Cachaça {user.username} não beba muito 🥃")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/vodka"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Sua  Vodka {user.username} ")
            await self.highrise.react("thumbs", user.id)
           
        if message.startswith("/champanhe"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Sua Champanhe {user.username} 🍾🥂")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/cerveja"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Sua Cerveja {user.username} 🍺")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/vinho-branco"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Seu Vinho-Branco {user.username}")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/vinho"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Seu Vinho {user.username}")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/cardapio2"):
            await self.highrise.send_whisper(user.id,"esse é o nosso cardapio de comidas e petiscos espero que goste 😄")
                                     
        if message.startswith("/cardapio2"):
            await self.highrise.send_whisper(user.id,"/camarão , /salada-de-alface , /salada-de-repolho , /macarrão , /pizza , /bolo-de-cenoura")

        if message.startswith("/cardapio2"):
            await self.highrise.send_whisper(user.id,"/bolo-de-morango , /açai , /sorvete , /cupcake , /sorvete , /batata-frita , /espetinho , /pão-de-alho")

        if message.startswith("/pizza"):  
            await self.highrise.send_whisper(user.id,f"{user.username} aqui está sua deliciosa pizza 🍕")
            await self.highrise.react("thumbs", user.id)
          
        if message.startswith("/bolo-de-morango"):
            await self.highrise.send_whisper(user.id,f"Aqui Está seu Delicioso Bolo de Morango {user.username} 🍰")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/salada-de-repolho"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Sua Deliciosa salada de repolho {user.username} 🥬🥬")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/camarão"):  
            await self.highrise.send_whisper(user.id,f"🍤Aqui Está seu Delicoso Camarão 🍤 {user.username} 🍤")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/macarrão"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está seu macarrão {user.username} aproveite 🍜🍝")
            await self.highrise.react("thumbs", user.id)
          
        if message.startswith("/salada-de-alface"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está a Sua salada de alface {user.username} com um pouco de tomates por cima 🥬🥗")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/bolo-de-cenoura"):  
            await self.highrise.send_whisper(user.id,f"aqui está seu bolo de cenoura  {user.username} 🥕🥮")
            await self.highrise.react("thumbs", user.id)
           
        if message.startswith("/açai"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Seu Açai {user.username} 🍨 Aproveite")
            await self.highrise.react("thumbs", user.id)
          
        if message.startswith("/sorvete"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Seu sorvete {user.username} 🍦🍨")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/pão-de-alho"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Sua pão de alho {user.username} 🥖🧄")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/batata-frita"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Sua Batata Frita {user.username} aproveite 🍟")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/espetinho"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Seu Espetinho {user.username} 🍢🍢")
            await self.highrise.react("thumbs", user.id)

        if message.startswith("/cupcake"):  
            await self.highrise.send_whisper(user.id,f"Aqui Está Seu cupcake {user.username} 🧁")
            await self.highrise.react("thumbs", user.id)
              
        if        message.startswith("/tp") or      message.startswith("!tp") or      message.startswith("/tele") or          message.startswith("Tp") or          message.startswith("Tele") or  message.startswith("!tele"):
          target_username =         message.split("@")[-1].strip()
          await                     self.teleport_to_user(user, target_username)

        if                            message.startswith("Summon") or         message.startswith("Summom") or         message.startswith("!summom") or        message.startswith("/summom") or        message.startswith("/summon") or  message.startswith("!summon"):
          if user.username in moderators:
           target_username = message.split("@")[-1].strip()
           await self.teleport_user_next_to(target_username, user)

        if message.lower().startswith(("!carteira","carteira","/carteira","wallet","/wallet","!wallet")):
          if user.username in moderators:
            wallet = (await self.highrise.get_wallet()).content
            await self.highrise.send_whisper(user.id,f"\nvalor disponivel na carteira:\n{wallet[0].amount} {wallet[0].type}")
            await self.highrise.send_emote("idle-floss")

        if message.startswith("!add"):
          if user.username in moderators:
            parts = message.split()
            if len(parts) != 3:
                await self.highrise.chat("Invalid promote command format.")
                return
            command, username, role = parts
            if "@" not in username:
                username = username
            else:
                username = username[1:]
            if role.lower() not in ["moderator", "designer"]:
                await self.highrise.chat("Invalid role, please specify a valid role.")
                return
            #check if user is in room
            room_users = (await self.highrise.get_room_users()).content
            for room_user, pos in room_users:
                if room_user.username.lower() == username.lower():
                    user_id = room_user.id
                    break
            if "user_id" not in locals():
                await self.highrise.chat("User not found, please specify a valid user and coordinate")
                return
            #promote user
            permissions = (await self.highrise.get_room_privilege(user_id))
            setattr(permissions, role.lower(), True)
            try:
                await self.highrise.change_room_privilege(user_id, permissions)
                await self.highrise.chat(f"{username} has been promoted to {role}.")
            except Exception as e:
                await self.highrise.chat(f"Error: {e}")
                return

        if message.startswith("!remove"):
          if user.username in moderators:
            parts = message.split()
            if len(parts) != 3:
                await self.highrise.chat("Invalid demote command format.")
                return
            command, username, role = parts
            if "@" not in username:
                username = username
            else:
                username = username[1:]
            if role.lower() not in ["moderator", "designer"]:
                await self.highrise.chat("Invalid role, please specify a valid role.")
                return
            #check if user is in room
            room_users = (await self.highrise.get_room_users()).content
            for room_user, pos in room_users:
                if room_user.username.lower() == username.lower():
                    user_id = room_user.id
                    break
            if "user_id" not in locals():
                await self.highrise.chat("User not found, please specify a valid user and coordinate")
                return
            #promote user
            permissions = (await self.highrise.get_room_privilege(user_id))
            setattr(permissions, role.lower(), False)
            try:
                await self.highrise.change_room_privilege(user_id, permissions)
                await self.highrise.chat(f"{username} has been demoted from {role}.")
            except Exception as e:
                await self.highrise.chat(f"Error: {e}")
                return
                
        if message.lower().startswith(("!say")):
          if user.username in moderators:
                text = message.replace("!say", "").strip()
                await self.highrise.chat(text)

        if message.lower().startswith(("/say")):
          if user.username in moderators:
                text = message.replace("/say", "").strip()
                await self.highrise.chat(text)

        if message.lower().startswith(("say")):
          if user.username in moderators:
                text = message.replace("say", "").strip()
                await self.highrise.chat(text)

        if message.lower().startswith(("-say")):
          if user.username in moderators:
                text = message.replace("-say", "").strip()
                await self.highrise.chat(text)
                       
        if message.startswith("!ban"):
          if user.username in moderators:
              parts = message.split()
              if len(parts) < 2:
                  await self.highrise.chat(user.id, "Use: !ban @username")
                  return

              mention = parts[1]
              username_to_ban = mention.lstrip('@')  # Remove the '@' symbol from the mention
              response = await self.highrise.get_room_users()
              users = [content[0] for content in response.content]  # Extract the User objects
              user_ids = [user.id for user in users]  # Extract the user IDs

              if username_to_ban.lower() in [user.username.lower() for user in users]:
                  user_index = [user.username.lower() for user in users].index(username_to_ban.lower())
                  user_id_to_ban = user_ids[user_index]
                  await self.highrise.moderate_room(user_id_to_ban, "ban", 3600)  # Ban for 1 hour
                  await self.highrise.chat(f"Banido  {mention} por 1 hora. ")
              else:
                  await self.highrise.send_whisper(user.id, f"usuario {mention} não está na sala. ")
              
        if message.startswith("!mute"):
          if user.username in moderators:
              parts = message.split()
              if len(parts) < 2:
                  await self.highrise.chat(user.id, "Use: !mute @username")
                  return

              mention = parts[1]
              username_to_mute = mention.lstrip('@')  # Remove the '@' symbol from the mention
              response = await self.highrise.get_room_users()
              users = [content[0] for content in response.content]  # Extract the User objects
              user_ids = [user.id for user in users]  # Extract the user IDs

              if username_to_mute.lower() in [user.username.lower() for user in users]:
                  user_index = [user.username.lower() for user in users].index(username_to_mute.lower())
                  user_id_to_mute = user_ids[user_index]
                  await self.highrise.moderate_room(user_id_to_mute, "mute",3600)  # Mute for 1 hour
                  await self.highrise.chat(f"{mention} foi mutado por 1 hora. ")
              else:
                  await self.highrise.send_whisper(user.id, f"usuario {mention} não está na sala. ")

        if message.startswith("!unmute"):
          if user.username in moderators:
              parts = message.split()
              if len(parts) < 2:
                  await self.highrise.chat(user.id, "Use: !unmute @username")
                  return

              mention = parts[1]
              username_to_mute = mention.lstrip('@')  # Remove the '@' symbol from the mention
              response = await self.highrise.get_room_users()
              users = [content[0] for content in response.content]  # Extract the User objects
              user_ids = [user.id for user in users]  # Extract the user IDs

              if username_to_mute.lower() in [user.username.lower() for user in users]:
                  user_index = [user.username.lower() for user in users].index(username_to_mute.lower())
                  user_id_to_mute = user_ids[user_index]
                  await self.highrise.moderate_room(user_id_to_mute, "mute",1)  # Mute for 1 hour
                  await self.highrise.chat(f"{mention} foi desmutado.")
              else:
                  await self.highrise.send_whisper(user.id, f"usuario {mention} não está na sala. ")

        if message.lower().startswith(("!bot","/bot")): 
          if user.username in moderators:
                response = await self.highrise.get_room_users()
                your_pos = None
                for content in response.content:
                    if content[0].id == user.id:
                        if isinstance(content[1], Position):
                            your_pos = content[1]
                            break
                if not your_pos:
                    await self.highrise.send_whisper(user.id, "Coordenadas inválidas!")
                    return
                await self.highrise.walk_to(your_pos)
              
        if message.startswith("!kick"):
          if user.username in moderators:
              pass
          else:
              await self.highrise.chat("Voce não tem permissao para usar esse comando.")
              return
          #separete message into parts
          parts = message.split()
          #check if message is valid "kick @username"
          if len(parts) != 2:
              await self.highrise.chat("formato de banimento errado.")
              return
          #checks if there's a @ in the message
          if "@" not in parts[1]:
              username = parts[1]
          else:
              username = parts[1][1:]
          #check if user is in room
          room_users = (await self.highrise.get_room_users()).content
          for room_user, pos in room_users:
              if room_user.username.lower() == username.lower():
                  user_id = room_user.id
                  break
          if "user_id" not in locals():
              await self.highrise.chat("usuario não encontrado, porfavor arrume a cordenada do codigo")
              return
          #kick user
          try:
              await self.highrise.moderate_room(user_id, "kick")
          except Exception as e:
              await self.highrise.chat(f"{e}")
              return
          #send message to chat
          await self.highrise.chat(f"{username} Foi Banido da sala!!")

        if message == "!fit 1" and user.username in moderators:
          shirt = ["shirt-n_room32019jerseywhite"]
          pant = ["pants-n_room22019longcutoffsdenim"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='hair_back-n_malenew16', account_bound=False, active_palette=39),
                  Item(type='clothing', amount=1, id='nose-n_03_b', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='hair_front-n_malenew16', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='face_hair-n_newbasicfacehairupper06', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id='face_hair-n_newbasicfacehairlower16', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='sock-n_starteritems2020whitesocks', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='shoes-n_room12019sneakersblack', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='mouth-basic2018openfullround', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id='eye-n_basic2018malediamondsleepy', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='eyebrow-n_basic2018newbrows14', account_bound=False, active_palette=-1),

          ])
          await self.highrise.chat(f"👕FIT[1] adicionado ao bot.") 
          

        if message == "!fit 2" and user.username in moderators:
          shirt = ["shirt-n_room12019cropsweaterwhite"]
          pant = ["pants-n_room12019rippedpantsblue"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=23),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='hair_back-n_basic2018mediumcurlymarilyn', account_bound=False, active_palette=39),
                  Item(type='clothing', amount=1, id='nose-n_01', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='hair_front-n_basic2018marilyncurls', account_bound=False, active_palette=39),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='blush-f_blush01', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='sock-n_starteritems2020whitesocks', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='shoes-n_room12019hightopsblack', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='mouth-n_basic2018toothyfullpeaked', account_bound=False, active_palette=24),
                  Item(type='clothing', amount=1, id='eye-n_basic2018pinkshadow2', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='eyebrow-n_08', account_bound=False, active_palette=-1),

          ])
          await self.highrise.chat(f"👕FIT[2] adicionado ao bot.")

        if message == "!fit 3"  and user.username in moderators:
          shirt = ["shirt-f_punklace"]
          pant = ["pants-n_room22019shortcutoffsdenim"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=4, id='nose-n_01', account_bound=False, active_palette=4),
                  Item(type='clothing', amount=1, id='mouth-basic2018openfullpeaked', account_bound=False, active_palette=8),

                  Item(type='clothing', amount=1, id='hair_front-n_basic2018straightbluntbangs', account_bound=False, active_palette=28),
                  Item(type='clothing', amount=1, id='hair_back-n_basic2018straighthighpony', account_bound=False, active_palette=28),

                  Item(type='clothing', amount=1, id='eyebrow-n_basic2018newbrows14', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='eye-n_basic2018dolleyes', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='shoes-n_starteritems2019flatsblack', account_bound=False, active_palette=0),
                  Item(type='clothing', amount=1, id='necklace-n_room32019locknecklace', account_bound=False, active_palette=-1),

Item(type='clothing', amount=1, id='earrings-n_room12019goldhoops', account_bound=False, active_palette=-1),


          ]) 
          await self.highrise.chat(f"👕FIT[3] adicionado ao bot.")

        if message == "!fit 4" and user.username in moderators:
          shirt = ["shirt-n_room22019bratoppink"]
          pant = ["pants-n_room22019undiespink"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=3),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='hair_back-n_basic2020overshoulderwavy', account_bound=False, active_palette=77),
                  Item(type='clothing', amount=1, id='nose-n_01_b', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='hair_front-n_basic2020overshoulderwavy', account_bound=False, active_palette=77),
                  Item(type='clothing', amount=1, id='earrings-n_room12019goldhoops', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='glasses-n_room32019smallshades', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='shoes-n_registrationavatars2023gothgirlshoes', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='mouth-n_basic2018pillowfullpeaked', account_bound=False, active_palette=9),
                  Item(type='clothing', amount=1, id='eye-n_basic2018falselashes', account_bound=False, active_palette=10),
                  Item(type='clothing', amount=1, id='eyebrow-n_26', account_bound=False, active_palette=-1),

          ])
          await self.highrise.chat(f"👕FIT[4] adicionado ao bot.")
            
        if message == "!fit 5" and user.username in moderators:
          shirt = ["shirt-n_room12019cropsweaterblack"]
          pant = ["skirt-n_room12019pleatedskirtgrey"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=4, id='nose-n_basic2018newnose15', account_bound=False, active_palette=4),
                  Item(type='clothing', amount=1, id='mouth-n_room22019sillymouth', account_bound=False, active_palette=-1),

                  Item(type='clothing', amount=1, id='hair_front-n_basic2020overshoulderwavy', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id='hair_back-n_basic2020overshoulderwavy', account_bound=False, active_palette=1),

                  Item(type='clothing', amount=1, id='eyebrow-n_basic2018newbrows16', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='eye-n_basic2018teardrop', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='shoes-n_registrationavatars2023gothgirlshoes', account_bound=False, active_palette=0),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle35', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle32', account_bound=False, active_palette=-1),

          ]) 
          await self.highrise.chat(f"👕FIT[5] adicionado ao bot.")       

        if message == "!fit 6" and user.username in moderators:
          shirt = ["shirt-n_room32019longlineteesweatshirtgrey"]
          pant = ["pants-n_starteritems2019cuffedjeansblue"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=4),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=4, id='hair_back-n_malenew19', account_bound=False, active_palette=80),
                  Item(type='clothing', amount=1, id='nose-n_basic2018newnose04', account_bound=False, active_palette=-1),

                  Item(type='clothing', amount=4, id='hair_front-n_malenew19', account_bound=False, active_palette=80),
                  Item(type='clothing', amount=1, id='watch-n_room32019blackwatch', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='shoes-n_room12019sneakersblack', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='mouth-basic2018whistlemouth', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='eye-n_basic2018malealmondsquint', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='eyebrow-n_04', account_bound=False, active_palette=-1),

          ])
          await self.highrise.chat(f"👕FIT[6] adicionado ao bot.")

        if message == "!fit 7" and user.username in moderators:
          shirt = ["shirt-n_registrationavatars2023arianadress"]
          pant = ["pants-n_room22019undiesblack"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=23),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=4, id='hair_back-n_basic2019poofbob', account_bound=False, active_palette=82),
                  Item(type='clothing', amount=1, id='nose-n_01', account_bound=False, active_palette=-1),

                  Item(type='clothing', amount=4, id='hair_front-n_basic2018straightbangslowpart', account_bound=False, active_palette=82),

Item(type='clothing', amount=1, id='earrings-n_room12019goldhoops', account_bound=False, active_palette=-1),
                
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='shoes-n_registrationavatars2023arianaboots', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='mouth-n_registrationavatars2023pinkmouth', account_bound=False, active_palette=3),
                  Item(type='clothing', amount=1, id='eye-n_registrationavatars2023gymgirleyes', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='eyebrow-n_08', account_bound=False, active_palette=-1),

          ])
          await self.highrise.chat(f"👕FIT[7] adicionado ao bot.")

        if message == "!fit 8" and user.username in moderators:
          shirt = ["shirt-n_room12019sweaterwithbuttondowngrey"]
          pant = ["pants-n_room12019formalslackskhaki"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=4, id='hair_back-n_malenew05', account_bound=False, active_palette=4),
                  Item(type='clothing', amount=1, id='eyebrow-n_06', account_bound=False, active_palette=-1),

                  Item(type='clothing', amount=4, id='hair_front-n_malenew04', account_bound=False, active_palette=4),
                
                  Item(type='clothing', amount=1, id='shoes-n_room12019sneakersblack', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='mouth-basic2018chippermouth', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='eye-m_12b', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='nose-n_03_b', account_bound=False, active_palette=-1),

          ])
          await self.highrise.chat(f"👕FIT[8] adicionado ao bot.")

        if message == "!fit 9" and user.username in moderators:
          shirt = ["shirt-n_winxudcrwrdsone2024winxblueshirt"]
          pant = ["skirt-n_winxudcrwrdsone2024pinkskirtstrawberrys"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=3),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=4, id='hair_back-n_basic2018wavypulledback', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id='nose-n_01', account_bound=False, active_palette=-1),

                  Item(type='clothing', amount=4, id='hair_front-n_basic2018sidebangspulledback', account_bound=False, active_palette=1),

Item(type='clothing', amount=1, id='earrings-n_room12019goldhoops', account_bound=False, active_palette=-1),
                
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='shoes-n_room12019sneakerspink', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='mouth-n_registrationavatars2023pinkmouth', account_bound=False, active_palette=3),
                  Item(type='clothing', amount=1, id='eye-n_basic2018liftedeyes', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='eyebrow-n_08', account_bound=False, active_palette=-1),

          ])
          await self.highrise.chat(f"👕FIT[9] adicionado ao bot.")

        if message == "!fit 10" and user.username in moderators:
          shirt = ["shirt-n_room32019croppedspaghettitankblack"]
          pant = ["pants-n_room32019highwasittrackshortsblack"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=23),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),

Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='hair_front-n_basic2018longstraighthalfpony', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id='hair_back-n_basic2018sleekstraightpony', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id='nose-n_01', account_bound=False, active_palette=-1),

                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle36', account_bound=False, active_palette=-1),

Item(type='clothing', amount=1, id='eye-n_basic2018liftedeyes', account_bound=False, active_palette=7),
                
                  Item(type='clothing', amount=1, id='eyebrow-n_08', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id='shoes-n_starteritems2019flatswhite', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='mouth-basic2018openthinpeaked', account_bound=False, active_palette=3),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),

          ])
          await self.highrise.chat(f"👕FIT[10] adicionado ao bot.")

        if message == "!fit 11" and user.username in moderators:
          shirt = ["shirt-n_registrationavatars2023furryshirt"]
          pant = ["pants-n_registrationavatars2023furrypants"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),

Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='hair_front-n_basic2018straightpulledback', account_bound=False, active_palette=2),
                  Item(type='clothing', amount=1, id='hair_back-n_basic2018straightlowpony', account_bound=False, active_palette=2),
                  Item(type='clothing', amount=1, id='nose-n_01', account_bound=False, active_palette=-1),

                  Item(type='clothing', amount=1, id='freckle-n_registrationavatars2023contour', account_bound=False, active_palette=-1),

Item(type='clothing', amount=1, id='eye-n_registrationavatars2023gymgirleyes', account_bound=False, active_palette=7),
                
                  Item(type='clothing', amount=1, id='eyebrow-n_08', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id='shoes-n_registrationavatars2023furrysneakers', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='mouth-n_registrationavatars2023pinkmouth', account_bound=False, active_palette=3),
                  Item(type='clothing', amount=1, id='hat-n_registrationavatars2023wolfears', account_bound=False, active_palette=-1),

Item(type='clothing', amount=1, id='bag-n_registrationavatars2023furrytail', account_bound=False, active_palette=-1),

          ])
          await self.highrise.chat(f"👕FIT[11] adicionado ao bot.")

        if message.lower().startswith(("!wink","/wink","-wink","wink","Wink")) and user.username in moderators: 
          try:

              parts = message.split()
              num_hearts = int(parts[-1])
              target_username = parts[1].strip('@').lower()

              if 1 <= num_hearts <= 100:
                  for _ in range(num_hearts):
                      target_user = None
                      response = await self.highrise.get_room_users()
                      for user_info in response.content:
                          if user_info[0].username.lower() == target_username:
                              target_user = user_info[0]
                              break

                      if target_user:
                          await self.highrise.react("wink", target_user.id)
                      else:
                          await self.highrise.chat(f"o usuário {target_username} Não esta disponível na sala. ")
              else:
                  await self.highrise.chat("quantia inválida!, use apenas 1-100!")
          except ValueError:
              await self.highrise.chat("![react|heart|wink|wave|clap|thumbs] @username quantia.")

        if message.lower().startswith(("!clap","/clap","-clap","clap","Clap")) and user.username in moderators: 
          try:

              parts = message.split()
              num_hearts = int(parts[-1])
              target_username = parts[1].strip('@').lower()

              if 1 <= num_hearts <= 100:
                  for _ in range(num_hearts):
                      target_user = None
                      response = await self.highrise.get_room_users()
                      for user_info in response.content:
                          if user_info[0].username.lower() == target_username:
                              target_user = user_info[0]
                              break

                      if target_user:
                          await self.highrise.react("clap", target_user.id)
                      else:
                          await self.highrise.chat(f"o usuário {target_username} Não esta disponível na sala. ")
              else:
                  await self.highrise.chat("quantia inválida!, use apenas 1-100!")
          except ValueError:
              await self.highrise.chat("![react|heart|wink|wave|clap|thumbs] @username quantia.")

        if message.lower().startswith(("!wave","/wave","-wave","wave","Wave")) and user.username in moderators: 
          try:

              parts = message.split()
              num_hearts = int(parts[-1])
              target_username = parts[1].strip('@').lower()

              if 1 <= num_hearts <= 100:
                  for _ in range(num_hearts):
                      target_user = None
                      response = await self.highrise.get_room_users()
                      for user_info in response.content:
                          if user_info[0].username.lower() == target_username:
                              target_user = user_info[0]
                              break

                      if target_user:
                          await self.highrise.react("wave", target_user.id)
                      else:
                          await self.highrise.chat(f"o usuário {target_username} Não esta disponível na sala. ")
              else:
                  await self.highrise.chat("quantia inválida!, use apenas 1-100!")
          except ValueError:
              await self.highrise.chat("![react|heart|wink|wave|clap|thumbs] @username quantia.")

        if message.lower().startswith(("!react","/react","-react","React","react")) and user.username in moderators: 
          try:

              parts = message.split()
              num_hearts = int(parts[-1])
              target_username = parts[1].strip('@').lower()

              if 1 <= num_hearts <= 100:
                  for _ in range(num_hearts):
                      target_user = None
                      response = await self.highrise.get_room_users()
                      for user_info in response.content:
                          if user_info[0].username.lower() == target_username:
                              target_user = user_info[0]
                              break

                      if target_user:
                          await self.highrise.react(random.choice(react), target_user.id)
                      else:
                          await self.highrise.chat(f"o usuário {target_username} Não esta disponível na sala. ")
              else:
                  await self.highrise.chat("quantia inválida!, use apenas 1-100!")
          except ValueError:
              await self.highrise.chat("![react|heart|wink|wave|clap|thumbs] @username quantia.")
              
        if message.lower().startswith(("!thumbs","/thumbs","-thumbs","Thumbs","thumbs")) and user.username in moderators: 
          try:

              parts = message.split()
              num_hearts = int(parts[-1])
              target_username = parts[1].strip('@').lower()

              if 1 <= num_hearts <= 100:
                  for _ in range(num_hearts):
                      target_user = None
                      response = await self.highrise.get_room_users()
                      for user_info in response.content:
                          if user_info[0].username.lower() == target_username:
                              target_user = user_info[0]
                              break

                      if target_user:
                          await self.highrise.react("thumbs", target_user.id)
                      else:
                          await self.highrise.chat(f"o usuário {target_username} Não esta disponível na sala. ")
              else:
                  await self.highrise.chat("quantia inválida!, use apenas 1-100!")
          except ValueError:
              await self.highrise.chat("![react|heart|wink|wave|clap|thumbs] @username quantia.")
              
        if message.lower().startswith(("!heart","/heart","-heart","heart","Heart","❤️")) and user.username in moderators: 
          try:

              parts = message.split()
              num_hearts = int(parts[-1])
              target_username = parts[1].strip('@').lower()

              if 1 <= num_hearts <= 100:
                  for _ in range(num_hearts):
                      target_user = None
                      response = await self.highrise.get_room_users()
                      for user_info in response.content:
                          if user_info[0].username.lower() == target_username:
                              target_user = user_info[0]
                              break

                      if target_user:
                          await self.highrise.react("heart", target_user.id)
                      else:
                          await self.highrise.chat(f"o usuário {target_username} Não esta disponível na sala. ")
              else:
                  await self.highrise.chat("quantia inválida!, use apenas 1-100!")
          except ValueError:
              await self.highrise.chat("![react|heart|wink|wave|clap|thumbs] @username quantia.")

        if message.lower().startswith(("!wink","/wink","-wink","wink","Wink")): 
          try:

              parts = message.split()
              num_hearts = int(parts[-1])
              target_username = parts[1].strip('@').lower()

              if 1 <= num_hearts <= 10:
                  for _ in range(num_hearts):
                      target_user = None
                      response = await self.highrise.get_room_users()
                      for user_info in response.content:
                          if user_info[0].username.lower() == target_username:
                              target_user = user_info[0]
                              break

                      if target_user:
                          await self.highrise.react("wink", target_user.id)
                      else:
                          await self.highrise.chat(f"o usuário {target_username} Não esta disponível na sala. ")
              else:
                  await self.highrise.chat("quantia inválida!, use apenas 1-10!\n\napenas moderadores podem dar quantias acima de 10!")
          except ValueError:
              await self.highrise.chat("![react|heart|wink|wave|clap|thumbs] @username quantia.")

        if message.lower().startswith(("!react","/react","-react","react","React")):

              parts = message.split()
              num_hearts = int(parts[-1])
              target_username = parts[1].strip('@').lower()

              if 1 <= num_hearts <= 10:
                  for _ in range(num_hearts):
                      target_user = None
                      response = await self.highrise.get_room_users()
                      for user_info in response.content:
                          if user_info[0].username.lower() == target_username:
                              target_user = user_info[0]
                              break

                      if target_user:
                          await self.highrise.react(random.choice(react), target_user.id)
                      else:
                          await self.highrise.chat(f"o usuário {target_username} Não esta disponível na sala. ")
              else:
                  await self.highrise.chat("quantia inválida!, use apenas 1-10!\n\napenas moderadores podem dar quantias acima de 10")
                  await self.highrise.chat("![react|heart|wink|wave|clap|thumbs] @username quantia.")
              
        if message.lower().startswith(("!clap","/clap","-clap","clap","Clap")): 

              parts = message.split()
              num_hearts = int(parts[-1])
              target_username = parts[1].strip('@').lower()

              if 1 <= num_hearts <= 10:
                  for _ in range(num_hearts):
                      target_user = None
                      response = await self.highrise.get_room_users()
                      for user_info in response.content:
                          if user_info[0].username.lower() == target_username:
                              target_user = user_info[0]
                              break

                      if target_user:
                          await self.highrise.react("clap", target_user.id)
                      else:
                          await self.highrise.chat(f"o usuário {target_username} Não esta disponível na sala. ")
              else:
                  await self.highrise.chat("quantia inválida!, use apenas 1-10!\n\napenas moderadores podem dar quantias acima de 10!") 
                  await self.highrise.chat("![react|heart|wink|wave|clap|thumbs] @username quantia.")

        if message.lower().startswith(("!wave","/wave","-wave","wave","Wave")): 
    
              parts = message.split()
              num_hearts = int(parts[-1])
              target_username = parts[1].strip('@').lower()

              if 1 <= num_hearts <= 10:
                  for _ in range(num_hearts):
                      target_user = None
                      response = await self.highrise.get_room_users()
                      for user_info in response.content:
                          if user_info[0].username.lower() == target_username:
                              target_user = user_info[0]
                              break

                      if target_user:
                          await self.highrise.react("wave", target_user.id)
                      else:
                          await self.highrise.chat(f"o usuário {target_username} Não esta disponível na sala. ")
              else:
                  await self.highrise.chat("quantia inválida!, use apenas 1-10!\n\napenas moderadores podem dar quantias acima de 10!")
                  await self.highrise.chat("![react|heart|wink|wave|clap|thumbs] @username quantia.")
              
        if message.lower().startswith(("!thumbs","/thumbs","-thumbs","Thumbs","thumbs")):

              parts = message.split()
              num_hearts = int(parts[-1])
              target_username = parts[1].strip('@').lower()

              if 1 <= num_hearts <= 10:
                  for _ in range(num_hearts):
                      target_user = None
                      response = await self.highrise.get_room_users()
                      for user_info in response.content:
                          if user_info[0].username.lower() == target_username:
                              target_user = user_info[0]
                              break

                      if target_user:
                          await self.highrise.react("thumbs", target_user.id)
                      else:
                          await self.highrise.chat(f"o usuário {target_username} Não esta disponível na sala. ")
              else:
                  await self.highrise.chat("quantia inválida!, use apenas 1-10!\n\napenas moderadores podem dar quantias acima de 10!")
                  await self.highrise.chat("![react|heart|wink|wave|clap|thumbs] @username quantia.")
              
        if message.lower().startswith(("!heart","/heart","-heart","heart","Heart","❤️")):
              parts = message.split()
              num_hearts = int(parts[-1])
              target_username = parts[1].strip('@').lower()

              if 1 <= num_hearts <= 10:
                  for _ in range(num_hearts):
                      target_user = None
                      response = await self.highrise.get_room_users()
                      for user_info in response.content:
                          if user_info[0].username.lower() == target_username:
                              target_user = user_info[0]
                              break

                      if target_user:
                          await self.highrise.react("heart", target_user.id)
                      else:
                          await self.highrise.chat(f"o usuário {target_username} Não esta disponível na sala. ")
              else:
                  await self.highrise.chat("quantia inválida!, use apenas 1-10!\n\napenas moderadores podem dar quantias acima de 10")
                  await self.highrise.chat("![react|heart|wink|wave|clap|thumbs] @username quantia.")
              
        if message.lower().lstrip().startswith(("-wrong","-fashion","-gravity","-icecream","-casual","-kiss","-no","-yes","-laughing","-hello","-wave","-shy","-tired","-flirty","-flirtywave","-confused","-charging","-hot","-snowball","-curtsy","-bow","-model","-greedy","-snowangel","-pose7","-cute","-superpose","-frog","-snake","-eneryball","-maniac","-teleport","-float","-singing","-telekinesis","-sing","-singalong","-shuffle","-tiktok10","-tik10","-cutey","-pose5","-pose3","-pose1","-pose8","-blackpink","-dontstartnow","-tik2","-tiktok2","-pennywise","-russian","-shopping","-shop","-letsgoshopping","-enthused","-celebrate","-gagging","-flex","-cursing","-thumbsup","-angry","-punk","-zombie","-sit","-fight","-swordfight","-macarena","-weird","-savage","-tiktok8","-tik8","-viralgroove","-viral","-tik9","-tiktok9","-saunter","-astronaut","-penguin","-airguitar","-guitar","-boxer","-pose9","-stargazer","-star","-sayso","-uwu","-jetpack","-fairytwirl","-fairyfloat","-launch","-smooch","-tiktok","-attention","-salute","-pushit","-foryou","-gift","-touch","-kawaii","-repose","-surprise","-sleigh","-hyped","-jingle","-gottago","-time","-timejump","-party","-thumbsub","-scritchy","-skating","-bitnervous","-creepy","-bashful","-revelations","-watch")):
                response = await self.highrise.get_room_users()
                users = [content[0] for content in response.content]
                usernames = [user.username.lower() for user in users]
                parts = message[1:].split()
                args = parts[1:]

                if len(args) < 1:
                    await self.highrise.send_whisper(user.id, f"Usage: {parts[0]} <@username>")
                    return
                elif args[0][0] != "@":
                    await self.highrise.send_whisper(user.id, "Invalid user format. Please use '@username'.")
                    return
                elif args[0][1:].lower() not in usernames:
                    await self.highrise.send_whisper(user.id, f"{args[0][1:]} is not in the room.")
                    return

                user_id = next((u.id for u in users if u.username.lower() == args[0][1:].lower()), None)
                if not user_id:
                    await self.highrise.send_whisper(user.id, f"User {args[0][1:]} not found")
                    return

                if message.lower().lstrip().startswith("-revelations"):
                        await self.highrise.send_emote("emote-headblowup'", user.id)
                        await self.highrise.send_emote("emote-headblowup'", user_id)

                if message.lower().lstrip().startswith("-bashful"):
                        await self.highrise.send_emote("emote-shy2", user.id)
                        await self.highrise.send_emote("emote-shy2", user_id)
                    
                if message.lower().lstrip().startswith("-thumbsub"):
                        await self.highrise.send_emote("emoji-thumbsup", user.id)
                        await self.highrise.send_emote("emoji-thumbsup", user_id)
                    
                if message.lower().lstrip().startswith("-scritchy"):
                        await self.highrise.send_emote("idle-wild", user.id)
                        await self.highrise.send_emote("idle-wild", user_id)

                if message.lower().lstrip().startswith("-bitnervous"):
                        await self.highrise.send_emote("idle-nervous", user.id)
                        await self.highrise.send_emote("idle-nervous", user_id)
            
                if message.lower().lstrip().startswith("-creepy"):
                        await self.highrise.send_emote("dance-creepypuppet", user.id)
                        await self.highrise.send_emote("dance-creepypuppet", user_id)

                if message.lower().lstrip().startswith("-party"):
                        await self.highrise.send_emote("emote-celebrate", user.id)
                        await self.highrise.send_emote("emote-celebrate", user_id)

                if message.lower().lstrip().startswith("-skating"):
                        await self.highrise.send_emote("emote-iceskating", user.id)
                        await self.highrise.send_emote("emote-iceskating", user_id)

                if message.lower().lstrip().startswith("-wrong"):
                        await self.highrise.send_emote("dance-wrong", user.id)
                        await self.highrise.send_emote("dance-wrong", user_id)

                if message.lower().lstrip().startswith("-fashion"):
                        await self.highrise.send_emote("emote-fashionista", user.id)
                        await self.highrise.send_emote("emote-fashionista", user_id)

                if message.lower().lstrip().startswith("-gravity"):              
                        await self.highrise.send_emote("emote-gravity", user.id)
                        await self.highrise.send_emote("emote-gravity", user_id)

                if message.lower().lstrip().startswith("-icecream"):
                        await self.highrise.send_emote("dance-icecream", user.id)
                        await self.highrise.send_emote("dance-icecream", user_id)

                if message.lower().lstrip().startswith("-casual"):
                        await self.highrise.send_emote("idle-dance-casual", user.id)
                        await self.highrise.send_emote("idle-dance-casual", user_id)

                if message.lower().lstrip().startswith("-kiss"):
                        await self.highrise.send_emote("emote-kiss", user.id)
                        await self.highrise.send_emote("emote-kiss", user_id)

                if message.lower().lstrip().startswith("-no"):
                        await self.highrise.send_emote("emote-no", user.id)
                        await self.highrise.send_emote("emote-no", user_id)

                if message.lower().lstrip().startswith("-sad"):
                        await self.highrise.send_emote("emote-sad", user.id)
                        await self.highrise.send_emote("emote-sad", user_id)

                if message.lower().lstrip().startswith("-yes"):
                        await self.highrise.send_emote("emote-yes", user.id)
                        await self.highrise.send_emote("emote-yes", user_id)

                if message.lower().lstrip().startswith("-laughing"):
                        await self.highrise.send_emote("emote-laughing", user.id)
                        await self.highrise.send_emote("emote-laughing", user_id)

                if message.lower().lstrip().startswith("-hello"):
                        await self.highrise.send_emote("emote-hello", user.id)
                        await self.highrise.send_emote("emote-hello", user_id)

                if message.lower().lstrip().startswith("-wave"):
                        await self.highrise.send_emote("emote-wave", user.id)
                        await self.highrise.send_emote("emote-wave", user_id)

                if message.lower().lstrip().startswith("-shy"):
                        await self.highrise.send_emote("emote-shy", user.id)
                        await self.highrise.send_emote("emote-shy", user_id)

                if message.lower().lstrip().startswith("-tired"):
                        await self.highrise.send_emote("emote-tired", user.id)
                        await self.highrise.send_emote("emote-tired", user_id)

                if message.lower().lstrip().startswith("-flirtywave"):
                        await self.highrise.send_emote("emote-lust", user.id)
                        await self.highrise.send_emote("emote-lust", user_id)

                if message.lower().lstrip().startswith("-flirty"):
                        await self.highrise.send_emote("emote-lust", user.id)
                        await self.highrise.send_emote("emote-lust", user_id)

                if message.lower().lstrip().startswith("-confused"):
                        await self.highrise.send_emote("emote-confused", user.id)
                        await self.highrise.send_emote("emote-confused", user_id)

                if message.lower().lstrip().startswith("-charging"):
                        await self.highrise.send_emote("emote-charging", user.id)
                        await self.highrise.send_emote("emote-charging", user_id)

                if message.lower().lstrip().startswith("-snowangel"):
                        await self.highrise.send_emote("emote-snowangel", user.id)
                        await self.highrise.send_emote("emote-snowangel", user_id)

                if message.lower().lstrip().startswith("-hot"):
                        await self.highrise.send_emote("emote-hot", user.id)
                        await self.highrise.send_emote("emote-hot", user_id)

                if message.lower().lstrip().startswith("-superpose"):
                        await self.highrise.send_emote("emote-superpose", user.id)
                        await self.highrise.send_emote("emote-superpose", user_id)

                if message.lower().lstrip().startswith("-frog"):
                        await self.highrise.send_emote("emote-frog", user.id)
                        await self.highrise.send_emote("emote-frog", user_id)

                if message.lower().lstrip().startswith("-cute"):
                        await self.highrise.send_emote("emote-cute", user.id)
                        await self.highrise.send_emote("emote-cute", user_id)

                if message.lower().lstrip().startswith("-pose7"):
                        await self.highrise.send_emote("emote-pose7", user.id)
                        await self.highrise.send_emote("emote-pose7", user_id)

                if message.lower().lstrip().startswith("-snake"):
                        await self.highrise.send_emote("emote-snake", user.id)
                        await self.highrise.send_emote("emote-snake", user_id)

                if message.lower().lstrip().startswith("-eneryball"):
                        await self.highrise.send_emote("emote-energyball", user.id)
                        await self.highrise.send_emote("emote-energyball", user_id)

                if message.lower().lstrip().startswith("-maniac"):
                        await self.highrise.send_emote("emote-maniac", user.id)
                        await self.highrise.send_emote("emote-maniac", user_id)

                if message.lower().lstrip().startswith("-teleport"):
                        await self.highrise.send_emote("emote-teleporting", user.id)
                        await self.highrise.send_emote("emote-teleporting", user_id)

                if message.lower().lstrip().startswith("-float"):
                        await self.highrise.send_emote("emote-float", user.id)
                        await self.highrise.send_emote("emote-float", user_id)

                if message.lower().lstrip().startswith("-telekinesis"):
                        await self.highrise.send_emote("emote-telekinesis", user.id)
                        await self.highrise.send_emote("emote-telekinesis", user_id)

                if message.lower().lstrip().startswith("-snowball"):
                        await self.highrise.send_emote("emote-snowball", user.id)
                        await self.highrise.send_emote("emote-snowball", user_id)

                if message.lower().lstrip().startswith("-curtsy"):
                        await self.highrise.send_emote("emote-curtsy", user.id)
                        await self.highrise.send_emote("emote-curtsy", user_id)

                if message.lower().lstrip().startswith("-bow"):
                        await self.highrise.send_emote("emote-bow", user.id)
                        await self.highrise.send_emote("emote-bow", user_id)

                if message.lower().lstrip().startswith("-model"):
                        await self.highrise.send_emote("emote-model", user.id)
                        await self.highrise.send_emote("emote-model", user_id)

                if message.lower().lstrip().startswith("-greedy"):
                        await self.highrise.send_emote("emote-greedy", user.id)
                        await self.highrise.send_emote("emote-greedy", user_id)

                if message.lower().lstrip().startswith("-sing"):
                        await self.highrise.send_emote("idle_singing", user.id)
                        await self.highrise.send_emote("idle_singing", user_id)

                if message.lower().lstrip().startswith("-shuffle"):
                        await self.highrise.send_emote("dance-tiktok10", user.id)
                        await self.highrise.send_emote("dance-tiktok10", user_id)

                if message.lower().lstrip().startswith("-singing"):
                        await self.highrise.send_emote("idle_singing", user.id)
                        await self.highrise.send_emote("idle_singing", user_id)

                if message.lower().lstrip().startswith("-singalong"):
                        await self.highrise.send_emote("idle_singing", user.id)
                        await self.highrise.send_emote("idle_singing", user_id)

                if message.lower().lstrip().startswith("-cutey"):
                        await self.highrise.send_emote("emote-cutey", user.id)
                        await self.highrise.send_emote("emote-cutey", user_id)

                if message.lower().lstrip().startswith("-tik10"):
                        await self.highrise.send_emote("dance-tiktok10", user.id)
                        await self.highrise.send_emote("dance-tiktok10", user_id)

                if message.lower().lstrip().startswith("-tiktok10"):
                        await self.highrise.send_emote("dance-tiktok10", user.id)
                        await self.highrise.send_emote("dance-tiktok10", user_id)

                if message.lower().lstrip().startswith("-pose5"):
                        await self.highrise.send_emote("emote-pose5", user.id)
                        await self.highrise.send_emote("emote-pose5", user_id)

                if message.lower().lstrip().startswith("-pose1"):
                        await self.highrise.send_emote("emote-pose1", user.id)
                        await self.highrise.send_emote("emote-pose1", user_id)

                if message.lower().lstrip().startswith("-pose8"):
                        await self.highrise.send_emote("emote-pose8", user.id)
                        await self.highrise.send_emote("emote-pose8", user_id)

                if message.lower().lstrip().startswith("-pose3"):
                        await self.highrise.send_emote("emote-pose3", user.id)
                        await self.highrise.send_emote("emote-pose3", user_id)

                if message.lower().lstrip().startswith("-blackpink"):
                        await self.highrise.send_emote("dance-blackpink", user.id)
                        await self.highrise.send_emote("dance-blackpink", user_id)

                if message.lower().lstrip().startswith("-dontstartnow"):
                        await self.highrise.send_emote("dance-tiktok2", user.id)
                        await self.highrise.send_emote("dance-tiktok2", user_id)

                if message.lower().lstrip().startswith("-tik2"):
                        await self.highrise.send_emote("dance-tiktok2", user.id)
                        await self.highrise.send_emote("dance-tiktok2", user_id)

                if message.lower().lstrip().startswith("-tiktok2"):
                        await self.highrise.send_emote("dance-tiktok2", user.id)
                        await self.highrise.send_emote("dance-tiktok2", user_id)

                if message.lower().lstrip().startswith("-pennywise"):
                        await self.highrise.send_emote("dance-pennywise", user.id)
                        await self.highrise.send_emote("dance-pennywise", user_id)

                if message.lower().lstrip().startswith("-russian"):
                        await self.highrise.send_emote("dance-russian", user.id)
                        await self.highrise.send_emote("dance-russian", user_id)

                if message.lower().lstrip().startswith("-shopping"):
                        await self.highrise.send_emote("dance-shoppingcart", user.id)
                        await self.highrise.send_emote("dance-shoppingcart", user_id)

                if message.lower().lstrip().startswith("-shop"):
                        await self.highrise.send_emote("dance-shoppingcart", user.id)
                        await self.highrise.send_emote("dance-shoppingcart", user_id)

                if message.lower().lstrip().startswith("-letsgoshopping"):
                        await self.highrise.send_emote("dance-shoppingcart", user.id)
                        await self.highrise.send_emote("dance-shoppingcart", user_id)

                if message.lower().lstrip().startswith("-enthused"):
                        await self.highrise.send_emote("idle-enthusiastic", user.id)
                        await self.highrise.send_emote("idle-enthusiastic", user_id)

                if message.lower().lstrip().startswith("-weird"):
                        await self.highrise.send_emote("dance-weird", user.id)
                        await self.highrise.send_emote("dance-weird", user_id)

                if message.lower().lstrip().startswith("-macarena"):
                        await self.highrise.send_emote("dance-macarena", user.id)
                        await self.highrise.send_emote("dance-macarena", user_id)

                if message.lower().lstrip().startswith("-swordfight"):
                        await self.highrise.send_emote("emote-swordfight", user.id)
                        await self.highrise.send_emote("emote-swordfight", user_id)

                if message.lower().lstrip().startswith("-fight"):
                        await self.highrise.send_emote("emote-swordfight", user.id)
                        await self.highrise.send_emote("emote-swordfight", user_id)

                if message.lower().lstrip().startswith("-celebrate"):
                        await self.highrise.send_emote("emoji-celebrate", user.id)
                        await self.highrise.send_emote("emoji-celebrate", user_id)

                if message.lower().lstrip().startswith("-gagging"):
                        await self.highrise.send_emote("emoji-gagging", user.id)
                        await self.highrise.send_emote("emoji-gagging", user_id)

                if message.lower().lstrip().startswith("-flex"):
                        await self.highrise.send_emote("emoji-flex", user.id)
                        await self.highrise.send_emote("emoji-flex", user_id)

                if message.lower().lstrip().startswith("-cursing"):
                        await self.highrise.send_emote("emoji-cursing", user.id)
                        await self.highrise.send_emote("emoji-cursing", user_id)

                if message.lower().lstrip().startswith("-thumbsup"):
                        await self.highrise.send_emote("emoji-thumbsup", user.id)
                        await self.highrise.send_emote("emoji-thumbsup", user_id)

                if message.lower().lstrip().startswith("-angry"):
                        await self.highrise.send_emote("emoji-angry", user.id)
                        await self.highrise.send_emote("emoji-angry", user_id)

                if message.lower().lstrip().startswith("-punk"):
                        await self.highrise.send_emote("emote-punkguitar", user.id)
                        await self.highrise.send_emote("emote-punkguitar", user_id)

                if message.lower().lstrip().startswith("-zombie"):
                        await self.highrise.send_emote("emote-zombierun", user.id)
                        await self.highrise.send_emote("emote-zombierun", user_id)

                if message.lower().lstrip().startswith("-sit"):
                        await self.highrise.send_emote("idle-loop-sitfloor", user.id)
                        await self.highrise.send_emote("idle-loop-sitfloor", user_id)

                if message.lower().lstrip().startswith("-savage"):
                        await self.highrise.send_emote("dance-tiktok8", user.id)
                        await self.highrise.send_emote("dance-tiktok8", user_id)

                if message.lower().lstrip().startswith("-tik8"):
                        await self.highrise.send_emote("dance-tiktok8", user.id)
                        await self.highrise.send_emote("dance-tiktok8", user_id)

                if message.lower().lstrip().startswith("-tiktok8"):
                        await self.highrise.send_emote("dance-tiktok8", user.id)
                        await self.highrise.send_emote("dance-tiktok8", user_id)

                if message.lower().lstrip().startswith("-sayso"):
                        await self.highrise.send_emote("idle-dance-tiktok4", user.id)
                        await self.highrise.send_emote("idle-dance-tiktok4", user_id)

                if message.lower().lstrip().startswith("-star"):
                        await self.highrise.send_emote("emote-stargazer", user.id)
                        await self.highrise.send_emote("emote-stargazer", user_id)

                if message.lower().lstrip().startswith("-uwu"):
                        await self.highrise.send_emote("idle-uwu", user.id)
                        await self.highrise.send_emote("idle-uwu", user_id)

                if message.lower().lstrip().startswith("-viral"):
                        await self.highrise.send_emote("dance-tiktok9", user.id)
                        await self.highrise.send_emote("dance-tiktok9", user_id)

                if message.lower().lstrip().startswith("-viralgroove"):
                        await self.highrise.send_emote("dance-tiktok9", user.id)
                        await self.highrise.send_emote("dance-tiktok9", user_id)

                if message.lower().lstrip().startswith("-tik9"):
                        await self.highrise.send_emote("dance-tiktok9", user.id)
                        await self.highrise.send_emote("dance-tiktok9", user_id)

                if message.lower().lstrip().startswith("-penguin"):
                        await self.highrise.send_emote("dance-pinguin", user.id)
                        await self.highrise.send_emote("dance-pinguin", user_id)

                if message.lower().lstrip().startswith("-airguitar"):
                        await self.highrise.send_emote("idle-guitar", user.id)
                        await self.highrise.send_emote("idle-guitar", user_id)

                if message.lower().lstrip().startswith("-guitar"):
                        await self.highrise.send_emote("idle-guitar", user.id)
                        await self.highrise.send_emote("idle-guitar", user_id)

                if message.lower().lstrip().startswith("-boxer"):
                        await self.highrise.send_emote("emote-boxer", user.id)
                        await self.highrise.send_emote("emote-boxer", user_id)

                if message.lower().lstrip().startswith("-pose9"):
                        await self.highrise.send_emote("emote-pose9", user.id)
                        await self.highrise.send_emote("emote-pose9", user_id)

                if message.lower().lstrip().startswith("-stargazer"):
                        await self.highrise.send_emote("emote-stargazer", user.id)
                        await self.highrise.send_emote("emote-stargazer", user_id)

                if message.lower().lstrip().startswith("-saunter"):
                        await self.highrise.send_emote("dance-anime", user.id)
                        await self.highrise.send_emote("dance-anime", user_id)

                if message.lower().lstrip().startswith("-astronaut"):
                        await self.highrise.send_emote("emote-astronaut", user.id)
                        await self.highrise.send_emote("emote-astronaut", user_id)

                if message.lower().lstrip().startswith("-timejump"):
                        await self.highrise.send_emote("emote-timejump", user.id)
                        await self.highrise.send_emote("emote-timejump", user_id)

                if message.lower().lstrip().startswith("-time"):
                        await self.highrise.send_emote("emote-timejump", user.id)
                        await self.highrise.send_emote("emote-timejump", user_id)

                if message.lower().lstrip().startswith("-gottago"):
                        await self.highrise.send_emote("idle-toilet", user.id)
                        await self.highrise.send_emote("idle-toilet", user_id)

                if message.lower().lstrip().startswith("-jingle"):
                        await self.highrise.send_emote("dance-jinglebell", user.id)
                        await self.highrise.send_emote("dance-jinglebell", user_id)

                if message.lower().lstrip().startswith("-jetpack"):
                        await self.highrise.send_emote("hcc-jetpack", user.id)
                        await self.highrise.send_emote("hcc-jetpack", user_id)

                if message.lower().lstrip().startswith("-fairytwirl"):
                        await self.highrise.send_emote("emote-looping", user.id)
                        await self.highrise.send_emote("emote-looping", user_id)

                if message.lower().lstrip().startswith("-fairyfloat"):
                        await self.highrise.send_emote("idle-floating", user.id)
                        await self.highrise.send_emote("idle-floating", user_id)

                if message.lower().lstrip().startswith("-smooch"):
                        await self.highrise.send_emote("emote-kissing-bound", user.id)
                        await self.highrise.send_emote("emote-kissing-bound", user_id)

                if message.lower().lstrip().startswith("-launch"):
                        await self.highrise.send_emote("emote-launch", user.id)
                        await self.highrise.send_emote("emote-launch", user_id)

                if message.lower().lstrip().startswith("-tiktok"):
                        await self.highrise.send_emote("dance-tiktok11", user.id)
                        await self.highrise.send_emote("dance-tiktok11", user_id)

                if message.lower().lstrip().startswith("-attention"):
                        await self.highrise.send_emote("emote-salute", user.id)
                        await self.highrise.send_emote("emote-salute", user_id)

                if message.lower().lstrip().startswith("-watch"):
                        await self.highrise.send_emote("emote-creepycute", user.id)
                        await self.highrise.send_emote("emote-creepycute", user_id)
                    
                if message.lower().lstrip().startswith("-salute"):
                        await self.highrise.send_emote("emote-cutesalute", user.id)
                        await self.highrise.send_emote("emote-cutesalute", user_id)

                if message.lower().lstrip().startswith("-pushit"):
                        await self.highrise.send_emote("dance-employee", user.id)
                        await self.highrise.send_emote("dance-employee", user_id)

                if message.lower().lstrip().startswith("-foryou"):
                        await self.highrise.send_emote("emote-gift", user.id)
                        await self.highrise.send_emote("emote-gift", user_id)

                if message.lower().lstrip().startswith("-gift"):
                        await self.highrise.send_emote("emote-gift", user.id)
                        await self.highrise.send_emote("emote-gift", user_id)

                if message.lower().lstrip().startswith("-touch"):
                        await self.highrise.send_emote("dance-touch", user.id)
                        await self.highrise.send_emote("dance-touch", user_id)

                if message.lower().lstrip().startswith("-kawaii"):
                        await self.highrise.send_emote("dance-kawai", user.id)
                        await self.highrise.send_emote("dance-kawai", user_id)

                if message.lower().lstrip().startswith("-repose"):
                        await self.highrise.send_emote("sit-relaxed", user.id)
                        await self.highrise.send_emote("sit-relaxed", user_id)

                if message.lower().lstrip().startswith("-surprise"):
                        await self.highrise.send_emote("emote-pose6", user.id)
                        await self.highrise.send_emote("emote-pose6", user_id)

                if message.lower().lstrip().startswith("-sleigh"):
                        await self.highrise.send_emote("emote-sleigh", user.id)
                        await self.highrise.send_emote("emote-sleigh", user_id)

                if message.lower().lstrip().startswith("-hyped"):
                        await self.highrise.send_emote("emote-hyped", user.id)
                        await self.highrise.send_emote("emote-hyped", user_id)
          
    async def on_message(self, user_id: str, conversation_id: str, is_new_conversation: bool) -> None:

        response = await self.highrise.get_messages(conversation_id)
        if isinstance(response, GetMessagesRequest.GetMessagesResponse):
            message = response.messages[0].content
            print (message)

        
        if message.lower().lstrip().startswith(("!general","/general","-general","general")):
            await asyncio.sleep(2)
            await self.highrise.send_message(conversation_id, f"\n💡General acesso gratuito a todos.\n\n-emote @usuario!\n!emote\n!emote list\n!jogos\ncardapio1\ncardapio2\n!loop [emote|1-98]\n/fly x,y,z\n!follow\n!userinfo @usuario\n!tele @usuario\n![heart|wink|wave|clap|thumbs]  @usuario 1-10")
            
        if message.lower().lstrip().startswith(("!mod","/mod","-mod","mod")):
            await asyncio.sleep(2)
            await self.highrise.send_message(conversation_id, f"\n💡Comandos de moderadores\n\n!bot\n!say [texto]\n!tipall [quantia]\n!tip @usuario [quantia]\n!tipme [quantia]\n!kick @usuario")
            await asyncio.sleep(1)
            await self.highrise.send_message(conversation_id, f"\n!ban @usuario\n!mute @usuario | !unmute @usuario\n!fit 1-11\n!wallet\n!summon @usuario\n!emote all [emote]\n!emote all random\n/fly @usuario x,y,z\n![heart|wink|wave|clap|thumbs] 1-100")

        if message.lower().lstrip().startswith(("emotes","!emotes","-emotes","/emotes")):
            await asyncio.sleep(2)
            await self.highrise.send_message(conversation_id, f"💡 Você pode usar emotes pagos gratuitamente, basta digitar o nome do emote no chat. Exemplo:\n\nswordfight\ngravity\nuwu\n\nPara ver todos os emotes gratuitos, use: !emote list")

        if message.lower().lstrip().startswith(("jogos","!jogos","Jogos","/jogos")):
            await asyncio.sleep(2)
            await self.highrise.send_message(conversation_id, f"🎮Você pode se distrair com esses comandos de jogos, basta digitar o nome do jogo no chat. Exemplo:\n\n/play\n/tarot\n/pescar\n/amor\n/odio\n/loucura\n/rps [pedra|papel|tesoura]\n/moeda [cara ou coroa]\n/ask [sua pergunta]")

        if message.lower().lstrip().startswith(("ola","olá","oi","Olá")):
            await asyncio.sleep(2)
            await self.highrise.send_message(conversation_id, f"🤖Ola prescisa de ajuda? Digite !help para ter acesso a nossas listas de comandos.")
            
        if message.lower().lstrip().startswith(("!help","/help","-help","help")):
            await asyncio.sleep(2)
            await self.highrise.send_message(conversation_id, f"\n💡Está prescisando de ajuda?\n\n!mod\n!jogos\n!general")
            
        if message.lower().lstrip().startswith(("!emote list","!list","/list","!lista","/lista","/emote list")):
            await asyncio.sleep(2)
            await self.highrise.send_message(conversation_id, f"🕺🏻Lista de emotes gratis:\n\n1.wrong\n2.fashion\n3.gravity\n4.icecream\n5.casual\n6.kiss\n7.no\n8.sad\n9.yes\n10.laughing\n11.hello\n12.wave\n13.shy\n14.tired\n15.flirtywave\n16.greedy\n17.model\n18.bow\n19.curtsy")
            await self.highrise.send_message(conversation_id, f"\n20.snowball\n21.hot\n22.snowangel\n23.charging\n24.confused\n25.telekinesis\n26.float\n27.teleport\n28.maniac\n29.eneryball\n30.snake\n31.frog\n32.superpose\n33.cute\n34.pose7\n35.pose8\n36.pose1\n37.pose5\n38.pose3")
            await self.highrise.send_message(conversation_id, f"\n39.cutey\n40.shuffle\n41.singalong\n42.enthused\n43.letsgoshopping\n44.russian\n45.pennywise\n46.dontstartnow\n47.blackpink\n48.celebrate\n49.gagging\n50.flex\n51.cursing\n52.thumbsup\n53.angry\n54.punk\n55.zombie\n56.sit\n57.fight")
            await self.highrise.send_message(conversation_id, f"\n58.macarena\n59.weird\n60.savage\n61.viralgroove\n62.uwu\n63.sayso\n64.stargazer\n65.pose9\n66.boxer\n67.airguitar\n68.penguin\n69.astronaut\n70.saunter\n71.creepy\n72.watch\n73.revelations\n74.bashful\n75.arabesque\n76.party")
            await self.highrise.send_message(conversation_id, f"\n77.skating\n78.scritchy\n79.bitnervous\n80.timejump\n81.gottago\n82.jingle\n83.hyped\n84.sleigh\n85.surprise\n86.repose\n87.kawaii\n88.touch\n89.foryou\n90.pushit\n91.salute\n92.attention\n93.tiktok\n.94.smooch\n95.launch\n96.fairyfloat\n97.fairytwirl\n98.jetpack")
            
    async def teleport(self, user: User, position: Position):
        try:
            await self.highrise.teleport(user.id, position)
        except Exception as e:
            print(f"Caught Teleport Error: {e}")

    async def teleport_to_user(self, user: User, target_username: str) -> None:
        try:
            room_users = await self.highrise.get_room_users()
            for target, position in room_users.content:
                if target.username.lower() == target_username.lower():
                    z = position.z
                    new_z = z - 1
                    await self.teleport(user, Position(position.x, position.y, new_z, position.facing))
                    break
        except Exception as e:
            print(f"An error occurred while teleporting to {target_username}: {e}")

    async def teleport_user_next_to(self, target_username: str, requester_user: User) -> None:
        try:
            # Get the position of the requester_user
            room_users = await self.highrise.get_room_users()
            requester_position = None
            for user, position in room_users.content:
                if user.id == requester_user.id:
                    requester_position = position
                    break

            # Find the target user and their position
            for user, position in room_users.content:
                if user.username.lower() == target_username.lower():
                    z = requester_position.z
                    new_z = z + 1  # Example: Move +1 on the z-axis (upwards)
                    await self.teleport(user, Position(requester_position.x, requester_position.y, new_z, requester_position.facing))
                    break
        except Exception as e:
            print(f"An error occurred while teleporting {target_username} next to {requester_user.username}: {e}")
          
    async def teleporter(self, message: str)-> None:
        """
            Teleports the user to the specified user or coordinate
            Usage: /teleport <username> <x,y,z>
                                                                """
        #separates the message into parts
        #part 1 is the command "/teleport"
        #part 2 is the name of the user to teleport to (if it exists)
        #part 3 is the coordinates to teleport to (if it exists)
        try:
            command, username, coordinate = message.split(" ")
        except:
            
            return
        
        #checks if the user is in the room
        room_users = (await self.highrise.get_room_users()).content
        for user in room_users:
            if user[0].username.lower() == username.lower():
                user_id = user[0].id
                break
        #if the user_id isn't defined, the user isn't in the room
        if "user_id" not in locals():
            
            return
            
        #checks if the coordinate is in the correct format (x,y,z)
        try:
            x, y, z = coordinate.split(",")
        except:
          
            return
        
        #teleports the user to the specified coordinate
        await self.highrise.teleport(user_id = user_id, dest = Position(float(x), float(y), float(z)))

    async def command_handler(self, user: User, message: str):
        parts = message.split(" ")
        command = parts[0][1:]
        functions_folder = "functions"
        # Check if the function exists in the module
        for file_name in os.listdir(functions_folder):
            if file_name.endswith(".py"):
                module_name = file_name[:-3]  # Remove the '.py' extension
                module_path = os.path.join(functions_folder, file_name)
                
                # Load the module
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                
                # Check if the function exists in the module
                if hasattr(module, command) and callable(getattr(module, command)):
                    function = getattr(module, command)
                    await function(self, user, message)
        
        # If no matching function is found
        return              

         
    async def on_whisper(self, user: User, message: str) -> None:
        print(f"{user.username} whispered: {message}")

        if        message.startswith("/tele") or              message.startswith("/tp") or              message.startswith("/fly") or     message.startswith("!tele") or      message.startswith("!tp") or     message.startswith("!fly"):
          if user.username in moderators:
            await self.teleporter(message)

        if        message.startswith("/") or              message.startswith("-") or              message.startswith(".") or          message.startswith("!"):
            await self.command_handler(user, message)

        if                            message.startswith("Summon") or         message.startswith("Summom") or         message.startswith("!summom") or        message.startswith("/summom") or        message.startswith("/summon") or  message.startswith("!summon"):
          if user.username in moderators:
           target_username = message.split("@")[-1].strip()
           await self.teleport_user_next_to(target_username, user)

        if message.lower().startswith("!tipall ") and user.username in moderators:
              parts = message.split(" ")
              if len(parts) != 2:
                  await self.highrise.send_message(user.id, "💰Comando inválido!")
                  return
              # Checks if the amount is valid
              try:
                  amount = int(parts[1])
              except:
                  await self.highrise.chat("💰Quantidade inválida!")
                  return
              # Checks if the bot has the amount
              bot_wallet = await self.highrise.get_wallet()
              bot_amount = bot_wallet.content[0].amount
              if bot_amount < amount:
                  await self.highrise.chat("💰Não há gorjetas suficientes")
                  return
              # Get all users in the room
              room_users = await self.highrise.get_room_users()
              # Check if the bot has enough funds to tip all users the specified amount
              total_tip_amount = amount * len(room_users.content)
              if bot_amount < total_tip_amount:
                  await self.highrise.chat("💰Não há gorjetas suficientes para dar a  todos! ")
                  return
              # Tip each user in the room the specified amount
              for room_user, pos in room_users.content:
                  bars_dictionary = {
                      10000: "gold_bar_10k",
                      5000: "gold_bar_5000",
                      1000: "gold_bar_1k",
                      500: "gold_bar_500",
                      100: "gold_bar_100",
                      50: "gold_bar_50",
                      10: "gold_bar_10",
                      5: "gold_bar_5",
                      1: "gold_bar_1"
                  }
                  fees_dictionary = {
                      10000: 1000,
                      5000: 500,
                      1000: 100,
                      500: 50,
                      100: 10,
                      50: 5,
                      10: 1,
                      5: 1,
                      1: 1
                  }
                  # Convert the amount to a string of bars and calculate the fee
                  tip = []
                  remaining_amount = amount
                  for bar in bars_dictionary:
                      if remaining_amount >= bar:
                          bar_amount = remaining_amount // bar
                          remaining_amount = remaining_amount % bar
                          for i in range(bar_amount):
                              tip.append(bars_dictionary[bar])
                              total = bar + fees_dictionary[bar]
                  if total > bot_amount:
                      await self.highrise.chat("💰Não há gorjetas suficientes!")
                      return
                  for bar in tip:
                      await self.highrise.tip_user(room_user.id, bar)           
                      await self.highrise.chat(f"💰{room_user.username} Recebeu uma gorjeta de {amount} golds!")
                              
        if message.lower().startswith(("!carteira","carteira","/carteira","wallet","/wallet","!wallet")):
          if user.username in moderators:
            wallet = (await self.highrise.get_wallet()).content
            await self.highrise.send_whisper(user.id,f"\nvalor disponivel na carteira:\n{wallet[0].amount} {wallet[0].type}")
            await self.highrise.send_emote("idle-floss")

        if message.lower().startswith(("!say")):
          if user.username in moderators:
                text = message.replace("!say", "").strip()
                await self.highrise.chat(text)

        if message.lower().startswith(("/say")):
          if user.username in moderators:
                text = message.replace("/say", "").strip()
                await self.highrise.chat(text)

        if message.lower().startswith(("say")):
          if user.username in moderators:
                text = message.replace("say", "").strip()
                await self.highrise.chat(text)

        if message.lower().startswith(("-say")):
          if user.username in moderators:
                text = message.replace("-say", "").strip()
                await self.highrise.chat(text)
              
    async def on_tip(self, sender: User, receiver: User, tip: CurrencyItem | Item) -> None:
        print (f"{sender.username} tipped {receiver.username} an amount of {tip.amount}")
        
        await self.highrise.chat(f"💰{sender.username} deu para {receiver.username} {tip.amount} golds!")
        
    async def on_user_move(self, user: User, pos: Position) -> None:
        print (f"{user.username} moved to {pos}")

    async def on_emote(self, user: User, emote_id: str, receiver: User | None) -> None:
        print(f"{user.username} emoted: {emote_id}")  
        
    async def on_user_leave(self, user: User) -> None:
        print(f"{user.username} saiu da sala")
        await self.highrise.chat(f"Volta @{user.username}! 😭")
        await self.highrise.send_emote(random.choice(emote))

        await asyncio.sleep(100)
        await self.highrise.chat(f"🎀Estão gostando do bot?\n\n🎀Faça uma postagem usando a hastag: #iMooseMoo")
