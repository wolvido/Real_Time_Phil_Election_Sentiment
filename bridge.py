from model import freqs,theta,predict_tweet

def predict(tweet):
    y_hat = predict_tweet(tweet, freqs, theta)
    if y_hat > 0.5:
        print('Positive sentiment')
    else: 
        print('Negative sentiment')

predict("hallelujah")