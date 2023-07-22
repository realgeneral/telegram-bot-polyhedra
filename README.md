# <h1 align="center"> Telegram bot Polyhedra</h1>
 
<br />

## Бот выполняент:


 1. #### Минт nft:

  *   Greenfield Testnet  (на BNB Chain) 
  *  ZkLightClient  (на BNB Chain) 
  *  ZkBridge on opBNB  (на BNB Chain) 
  *  Mainnet Alpha  (на Core) 
  *  Pandra  (на BNB Chain, Polygon, Core, Celo) 

 2. #### Кроссчейн nft сендер (zknft):  
  *  ZkLightClient nft  из BSC в opBNB 
  *  ZkBridge on opBNB nft  из BSC в opBNB 
  *  Mainnet Alpha nft  из Core в Polygon 
  *  CodeConqueror (Pandra) nft  из BSC в Core 
  *  PixelProwler (Pandra) nft  из Polygon в BSC 
  *  MelodyMaven (Pandra) nft  из Core в Polygon 
  *  EcoGuardian (Pandra) nft  из Celo в BSC 

 3. #### Отправка сообщения (zkMessenger):  
  *  из BSC в Polygon  

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