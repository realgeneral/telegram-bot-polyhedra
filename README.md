# <h1 align="center"> Telegram bot Polyhedra</h1>
 
<br />

## Бот выполняет:


 1. #### Минт nft:

  *  _Greenfield Testnet_  (на BNB Chain) 
  *  _ZkLightClient_  (на BNB Chain) 
  *  _ZkBridge on opBNB_  (на BNB Chain) 
  *  _Mainnet Alpha_  (на Core) 
  *  _Pandra_  (на BNB Chain, Polygon, Core, Celo) 

 2. #### Кроссчейн nft сендер (zknft):  
  *  _ZkLightClient nft_  из BSC в opBNB 
  *  _ZkBridge on opBNB nft_  из BSC в opBNB 
  *  _Mainnet Alpha nft_  из Core в Polygon 
  *  _CodeConqueror (Pandra)_ nft  из BSC в Core 
  *  _PixelProwler (Pandra) nft_  из Polygon в BSC 
  *  _MelodyMaven (Pandra) nft_  из Core в Polygon 
  *  _EcoGuardian (Pandra) nft_  из Celo в BSC 

 3. #### Отправка сообщения (zkMessenger):  
  *  _из BSC в Polygon_  

#### Замечания
 - Чтобы сминтить в сети Core необходимо раскинуть по кошелькам немного core 
 - Также необходим газ в opBNB
 - nft в сети назначения при бридже не клеймятся, это можно сделать руками, взяв хеш транзакции и зайдя в [Redeem](https://zkbridge.com/zknft)
 - Необходим [API key от moralis](https://docs.moralis.io/web3-data-api/evm/get-your-api-key)
<br />

## Запуск без использования Docker 
Определите переменную окружения BOT_TOKEN, либо укажите в явном виде в файле `app/create_bot.py`

### Запуск на Windows OS
```sh
pip install --no-cache-dir --upgrade -r requirements.txt
python3 -m app.main
```

### Запуск на UNIX-подобных ОS (Ubuntu, Debian, macOS, Fedora и других) 
```sh
./script.sh
```
<br />

## Запуск с использованием Docker 
Будет позже...