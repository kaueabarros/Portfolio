import csv
import connection
dct_arr = [
  {'ticket': 0, 
    'order': 1, 
    'time': 2, 
    'symbol': 3, 
    'volume': 4, 
    'type': 5, 
    'direction': 6, 
    'price': 7, 
    'stop loss': 8, 
    'take profit': 9, 
    'commission': 10, 
    'swap': 11, 
    'profit': 12, 
    'mae': 13, 
    'mfe': 14, 
    'comment': 15, 
    'sl triggered': 16, 
    'tp triggered': 17, 
    'account': 18, 
    'currency': 19, 
    'verified': 20, 
    'change': 21}]

con=connection.Conexao('localhost','portfolio','postgres','5K3FEawk]M')
cabecalho = list(dct_arr[0].keys())
with open('.\csv\demo_history.csv',mode='r',newline='',encoding='utf-8') as metatrader:
  operation = csv.DictReader(metatrader,  delimiter=',',fieldnames=cabecalho)
  for row in operation:
    if row['type'] == 'sell':
        codtype = 1
    else:
        codtype = 2
    if row['direction'] == 'in':
        coddirection = 1
    else:
        coddirection = 2
    if row['tp triggered'] == 'False':
        bittptriggered = 0
    else:
        bittptriggered = 1
    if row['sl triggered'] == 'False':
        bitsltriggered = 0
    else:
        bitsltriggered = 1
    if row['verified'] == 'False':
        bitverified = 0
    else:
        bitverified = 1
    sql = """
          insert into portfolio.dadosmetatrader (
            account,
            ticket,
            "order",
            datetime,
            symbol,
            volume,
            type,
            codtype,
            direction,
            coddirection,
            price,
            stoploss,
            takeprofit,
            commission,
            swap,
            profit,
            mae,
            mfe,
            comment,
            tptriggered,
            sltriggered,
            currency,
            verified,
            change)           
            values
          ('%s',
           '%s',
           '%s',
           '%s',
           '%s',
           '%s',
           '%s',
           '%s',
           '%s',
           '%s',
           '%s',
           '%s',
           '%s',
           '%s',
           '%s',
           '%s',
           '%s',
           '%s',
           '%s',
           '%s',
           '%s',
           '%s',
           '%s',
           '%s');
          """ % (
            row['account'],
            row['ticket'],
            row['order'],
            row['time'],
            row['symbol'],
            row['volume'],
            row['type'],
            codtype,
            row['direction'],
            coddirection,
            row['price'],
            row['stop loss'],
            row['take profit'],
            row['commission'],
            row['swap'],
            row['profit'],
            row['mae'],
            row['mfe'],
            row['comment'],
            bittptriggered,
            bitsltriggered,
            row['currency'],
            bitverified,
            row['change']           
        )
    print(sql)
    if con.manipular(sql):
        print('inserido com sucesso!')