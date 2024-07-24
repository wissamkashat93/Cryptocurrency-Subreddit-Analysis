import pandas as pd
import os
from dotenv import load_dotenv
import json
import re
import requests


class RedditAPI:
    def __init__(self):
        self.client_id = os.getenv("CLIENT_ID")
        self.secret_token = os.getenv("SECRET_TOKEN")
        self.reddit_password = os.getenv("PASSWORD")
        self.headers = {'User-Agent': 'ADSAPI/0.0.1'}
        self.access_token = self._get_access_token()

    def _get_access_token(self):
        auth = requests.auth.HTTPBasicAuth(self.client_id, self.secret_token)
        data = {
            "grant_type": "password",
            'username': "justinm329",
            'password': self.reddit_password
        }
        res = requests.post('https://www.reddit.com/api/v1/access_token',
                            auth=auth, data=data, headers=self.headers)
        access_token = res.json()['access_token']
        self.headers['Authorization'] = f'Bearer {access_token}'
        return access_token
    
    def _get_reddit_data(self, endpoint):
        res = requests.get(endpoint, headers=self.headers, params={'limit': '100'})
        return res
    
    def get_crypto_curr_data(self):
        crypto_request = self._get_reddit_data('https://oauth.reddit.com/r/CryptoCurrency/hot')
        crypto_json = crypto_request.json()
        crypto_df = pd.DataFrame()
        for post in crypto_json['data']['children']:
            new_df = pd.DataFrame({
                'approved_date': [post['data']['approved_at_utc']],
                'thread_id': [post['kind'] + " _ " + post['data']['id']],
                'subreddit': [post['data']['subreddit']],
                'title': [post['data']['title']],
                "body": [post['data']['selftext']],
                'upvote_ratio': [post['data']['upvote_ratio']],
                'ups': [post['data']['ups']],
                'downs': [post['data']['downs']],
                'score':  [post['data']['score']]
            })
            crypto_df = pd.concat([crypto_df, new_df], ignore_index=True)
        return crypto_df
    

    def get_crypto_markets_data(self):
        crypto_df = pd.DataFrame()
        crypto_markets_request = self._get_reddit_data('https://oauth.reddit.com/r/CryptoMarkets/hot')
        markets_json = crypto_markets_request.json()
        for post in markets_json['data']['children']:
            new_df = pd.DataFrame({
                'approved_date': [post['data']['approved_at_utc']],
                'thread_id': [post['kind'] + " _ " + post['data']['id']],
                'subreddit': [post['data']['subreddit']],
                'title': [post['data']['title']],
                "body": [post['data']['selftext']],
                'upvote_ratio': [post['data']['upvote_ratio']],
                'ups': [post['data']['ups']],
                'downs': [post['data']['downs']],
                'score':  [post['data']['score']]
            })
            crypto_df = pd.concat([crypto_df, new_df], ignore_index=True)
        return crypto_df
    
    def get_bitcoin_data(self):
        crypto_df = pd.DataFrame()
        bitcoin_request = self._get_reddit_data('https://oauth.reddit.com/r/Bitcoin/hot')
        bitcoin_json = bitcoin_request.json()
        for post in bitcoin_json['data']['children']:
            new_df = pd.DataFrame({
                'approved_date': [post['data']['approved_at_utc']],
                'thread_id': [post['kind'] + " _ " + post['data']['id']],
                'subreddit': [post['data']['subreddit']],
                'title': [post['data']['title']],
                "body": [post['data']['selftext']],
                'upvote_ratio': [post['data']['upvote_ratio']],
                'ups': [post['data']['ups']],
                'downs': [post['data']['downs']],
                'score':  [post['data']['score']]
            })
            crypto_df = pd.concat([crypto_df, new_df], ignore_index=True)
        return crypto_df
    
    def get_eth_data(self):
        crypto_df = pd.DataFrame()
        eths_request = self._get_reddit_data('https://oauth.reddit.com/r/Ethereum/hot')
        eth_json = eths_request.json()
        for post in eth_json['data']['children']:
            new_df = pd.DataFrame({
                'approved_date': [post['data']['approved_at_utc']],
                'thread_id': [post['kind'] + " _ " + post['data']['id']],
                'subreddit': [post['data']['subreddit']],
                'title': [post['data']['title']],
                "body": [post['data']['selftext']],
                'upvote_ratio': [post['data']['upvote_ratio']],
                'ups': [post['data']['ups']],
                'downs': [post['data']['downs']],
                'score':  [post['data']['score']]
            })
            crypto_df = pd.concat([crypto_df, new_df], ignore_index=True)
        return crypto_df
    
    def get_binance_data(self):
        crypto_df = pd.DataFrame()
        binance_request = self._get_reddit_data('https://oauth.reddit.com/r/binance/hot')
        binance_json = binance_request.json()
        for post in binance_json['data']['children']:
            new_df = pd.DataFrame({
                'approved_date': [post['data']['approved_at_utc']],
                'thread_id': [post['kind'] + " _ " + post['data']['id']],
                'subreddit': [post['data']['subreddit']],
                'title': [post['data']['title']],
                "body": [post['data']['selftext']],
                'upvote_ratio': [post['data']['upvote_ratio']],
                'ups': [post['data']['ups']],
                'downs': [post['data']['downs']],
                'score':  [post['data']['score']]
            })
            crypto_df = pd.concat([crypto_df, new_df], ignore_index=True)
        return crypto_df
    
    def get_solana_data(self):
        crypto_df = pd.DataFrame()
        solana_request = self._get_reddit_data('https://oauth.reddit.com/r/Solana/hot')
        solana_json = solana_request.json()
        for post in solana_json['data']['children']:
            new_df = pd.DataFrame({
                'approved_date': [post['data']['approved_at_utc']],
                'thread_id': [post['kind'] + " _ " + post['data']['id']],
                'subreddit': [post['data']['subreddit']],
                'title': [post['data']['title']],
                "body": [post['data']['selftext']],
                'upvote_ratio': [post['data']['upvote_ratio']],
                'ups': [post['data']['ups']],
                'downs': [post['data']['downs']],
                'score':  [post['data']['score']]
            })
            crypto_df = pd.concat([crypto_df, new_df], ignore_index=True)
        return crypto_df
    
    def get_ripple_data(self):
        crypto_df = pd.DataFrame()
        ripple_request = self._get_reddit_data('https://oauth.reddit.com/r/Ripple/hot')
        ripple_json = ripple_request.json()
        for post in ripple_json['data']['children']:
            new_df = pd.DataFrame({
                'approved_date': [post['data']['approved_at_utc']],
                'thread_id': [post['kind'] + " _ " + post['data']['id']],
                'subreddit': [post['data']['subreddit']],
                'title': [post['data']['title']],
                "body": [post['data']['selftext']],
                'upvote_ratio': [post['data']['upvote_ratio']],
                'ups': [post['data']['ups']],
                'downs': [post['data']['downs']],
                'score':  [post['data']['score']]
            })
            crypto_df = pd.concat([crypto_df, new_df], ignore_index=True)
        return crypto_df
    
    def get_cardano_data(self):
        crypto_df = pd.DataFrame()
        cardano_request = self._get_reddit_data('https://oauth.reddit.com/r/cardano/hot')
        cardano_json = cardano_request.json()
        for post in cardano_json['data']['children']:
            new_df = pd.DataFrame({
                'approved_date': [post['data']['approved_at_utc']],
                'thread_id': [post['kind'] + " _ " + post['data']['id']],
                'subreddit': [post['data']['subreddit']],
                'title': [post['data']['title']],
                "body": [post['data']['selftext']],
                'upvote_ratio': [post['data']['upvote_ratio']],
                'ups': [post['data']['ups']],
                'downs': [post['data']['downs']],
                'score':  [post['data']['score']]
            })
            crypto_df = pd.concat([crypto_df, new_df], ignore_index=True)
        return crypto_df
    
    def get_tronix_data(self):
        crypto_df = pd.DataFrame()
        tronix_request = self._get_reddit_data('https://oauth.reddit.com/r/Tronix/hot')
        tronix_json = tronix_request.json()
        for post in tronix_json['data']['children']:
            new_df = pd.DataFrame({
                'approved_date': [post['data']['approved_at_utc']],
                'thread_id': [post['kind'] + " _ " + post['data']['id']],
                'subreddit': [post['data']['subreddit']],
                'title': [post['data']['title']],
                "body": [post['data']['selftext']],
                'upvote_ratio': [post['data']['upvote_ratio']],
                'ups': [post['data']['ups']],
                'downs': [post['data']['downs']],
                'score':  [post['data']['score']]
            })
            crypto_df = pd.concat([crypto_df, new_df], ignore_index=True)
        return crypto_df
    
    def get_chainlink_data(self):
        crypto_df = pd.DataFrame()
        chainlink_request = self._get_reddit_data('https://oauth.reddit.com/r/Chainlink/hot')
        chainlink_json = chainlink_request.json()
        for post in chainlink_json['data']['children']:
            new_df = pd.DataFrame({
                'approved_date': [post['data']['approved_at_utc']],
                'thread_id': [post['kind'] + " _ " + post['data']['id']],
                'subreddit': [post['data']['subreddit']],
                'title': [post['data']['title']],
                "body": [post['data']['selftext']],
                'upvote_ratio': [post['data']['upvote_ratio']],
                'ups': [post['data']['ups']],
                'downs': [post['data']['downs']],
                'score':  [post['data']['score']]
            })
            crypto_df = pd.concat([crypto_df, new_df], ignore_index=True)
        return crypto_df