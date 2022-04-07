# IMPORTANDO BIBLIOTECAS
from urllib.request import urlopen
import json

# IMPORTANDO BIBLIOTECAS PARA O DISCORD
# USAR: pip install requests discord discord-webhook
from discord_webhook import DiscordWebhook, DiscordEmbed

# DEFININDO URL
url = "https://economia.awesomeapi.com.br/last/USD-BRL"

# FAZENDO REQUEST E GUARDANDO A RESPOSTA
response = urlopen(url)

# GUARDANDO RESPOSTA USANDO JSON.LOADS
data_json = json.loads(response.read())

# DEFININDO VARIÁVEIS
nome = data_json['USD']['name']
data = data_json['USD']['create_date']
valor_compra = data_json['USD']['bid']
valor_venda = data_json['USD']['ask']
variacao = data_json['USD']['varBid']

# INICIANDO MONTAGEM DA MENSAGEM PARA ENVIAR PARA O DISCORD
webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/XXXXXXXXXXXX/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
embed = DiscordEmbed(title='COTAÇÃO', description='%s em %s' %(nome, data), color='03b2f8')
embed.set_author(name='Bot Doidão da Coffops', icon_url='https://coffops.com/wp-content/uploads/2020/09/cropped-logo-coffops-transparente-1.png')
embed.add_embed_field(name='Valor de Compra',value='%s' %(valor_compra))
embed.add_embed_field(name='Valor de Venda',value='%s' %(valor_venda))
embed.add_embed_field(name='Variação',value='%s' %(variacao))

webhook.add_embed(embed)
response = webhook.execute(embed)
