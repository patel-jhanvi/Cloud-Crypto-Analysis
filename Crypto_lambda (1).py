
''' Author : Jhanvi Patel
This code is made for _
The purpose of this code is to help students, researchers and other community members as kickstarter to their code or in any way to help them. Please do not hesitate to contact me for any suggestions. 
Feel free to have a look at my other codes as well at {https://github.com/patel-jhanvi} '''

import http.client
import json
import boto3
from datetime import datetime

def fetch_crypto_data(crypto_id):
    conn = http.client.HTTPSConnection("api.coingecko.com")
    params = (
        "/api/v3/simple/price"
        f"?ids={crypto_id}"
        "&vs_currencies=usd"
        "&include_market_cap=true"
        "&include_24hr_vol=true"
        "&include_24hr_change=true"
        "&include_last_updated_at=true"
    )
    conn.request("GET", params)
    res = conn.getresponse()
    data = res.read()
    conn.close()
    print(f"Raw API response for {crypto_id}: {data}")  # Temporary print for debugging
    return json.loads(data.decode("utf-8"))

def lambda_handler(event, context):
    cryptos = ["bitcoin", "ethereum", "tether", "binancecoin"]
    bucket_name = 'crypto--new'  
    timestamp = datetime.now().strftime('%Y-%m-%d-%H%M%S')
    s3 = boto3.client('s3')
    object_key = f"crypto-data/{timestamp}.json"
    
    lines = []
    
    for crypto in cryptos:
        data = fetch_crypto_data(crypto)
        if data and crypto in data:
            crypto_data = data[crypto]
            line = json.dumps({
                "Name": crypto,
                "Type": f"struct<{crypto}_usd:double,{crypto}_usd_market_cap:double,{crypto}_usd_24h_vol:double,{crypto}_usd_24h_change:double,{crypto}_last_updated_at:int>",
                "Comment": ""
            })
            lines.append(line)
        else:
            print(f"Error: Data for {crypto} not found in response")
    
    body = "\n".join(lines)
    
    s3.put_object(Bucket=bucket_name, Key=object_key, Body=body)
    
    return { 
        'statusCode': 200,
        'body': json.dumps('Data successfully fetched and stored in S3')
    }
