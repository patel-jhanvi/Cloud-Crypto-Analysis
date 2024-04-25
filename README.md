# Cloud-Crypto-Analysis


#Cryptocurrency Data Analysis Project

## Overview

The Cryptocurrency Data Analysis Project aims to gather, store, and analyze real-time cryptocurrency market data. By leveraging AWS services, including Lambda, S3, and Athena, this project provides insights into market trends, price volatility, and trading volumes of leading cryptocurrencies sourced from the CoinGecko API.

## Objectives

- **Data Collection:** Collect real-time cryptocurrency data from the CoinGecko API (https://docs.coingecko.com/reference/introduction).
- **Data Storage:** Store the collected data efficiently in Amazon S3 for historical analysis.
- **Data Analysis:** Analyze the stored data using Amazon Athena to extract insights on price trends, market capitalization, and trading volumes.

  ## Architecture

  ![image](https://github.com/patel-jhanvi/Cloud-Crypto-Analysis/assets/61945134/4461e7d8-e896-4117-9f8b-39bd1b82409d)


## Implementation Steps

### 1. Set up AWS Account

- Go to the [AWS Management Console](https://aws.amazon.com/console/) and sign up for an account if you haven't already.
- Follow the instructions to create your account and set up billing information.

### 2. Configure AWS Services

#### Lambda

- Navigate to the Lambda console and create a new function.
- Choose a runtime (e.g., Node.js, Python).
  
#### S3

- Go to the S3 console and create a new bucket to store cryptocurrency market data.

#### Athena

- Navigate to the Athena console and set up a new query to execute SQL queries against the stored data.

### 3. Develop Lambda Functions

Write Lambda functions to interact with the CoinGecko API and store data in S3. Below is an example Lambda function in Node.js to fetch data from CoinGecko and store it in S3:

```javascript
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
```

### 4. Data Storage

Configure S3 buckets to store the collected cryptocurrency market data. Ensure proper permissions and policies are set up for the S3 buckets.

### 5. Data Analysis

Utilize Athena to execute SQL queries against the stored data. Write SQL queries to extract insights on price trends, market capitalization, and trading volumes.

## SQL Queries

```sql
-- Query for price trends of Bitcoin
SELECT 
    date_trunc('day', timestamp) AS day,
    avg(price) AS average_price
FROM 
    cryptocurrency_data
WHERE 
    symbol = 'BTC'
GROUP BY 
    day
ORDER BY 
    day;

-- Query for trading volumes of Ethereum
SELECT 
    date_trunc('day', timestamp) AS day,
    sum(volume) AS total_volume
FROM 
    cryptocurrency_data
WHERE 
    symbol = 'ETH'
GROUP BY 
    day
ORDER BY 
    day;
```


## Conclusion

By following these detailed implementation steps, you can set up, collect, store, and analyze real-time cryptocurrency market data effectively using AWS services.


