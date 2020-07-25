from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from .forms import TweetForm
from .models import Tweet

import psycopg2 as sql

def index(request):
    template = get_template('Tweets/index.html')
    context = None
    return HttpResponse(template.render(context, request))

def make_tweet(request):

    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['Title']
            content = form.cleaned_data['Content']
            new_tweet = Tweet(Title=title, Content=content)
            new_tweet.save()
        return redirect('/show/')
    else:
        form = TweetForm()

    return render(request, 'Tweets/make_tweet.html', {'form': form})

def show_tweets(request):

    conn = sql.connect(user = 'fxlnjkqd',
        password = 'hO9EXKi9DXEzZLUupaiKGMN9jqMAzZSA',
        host = '35.246.126.180',
        port = '5432',
        database = 'fxlnjkqd')
    c = conn.cursor()
    c.execute('SELECT * FROM Tweets_tweet;')
    data = c.fetchall()
    print(data)

    return render(request, 'Tweets/show_tweets.html', {'data': data})
