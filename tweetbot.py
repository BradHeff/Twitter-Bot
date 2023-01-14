import json
import os
import sys

if "linux" in sys.platform:
    os.environ["LC_AL"] = "C.UTF-8"
    os.environ["LANG"] = "C.UTF-8"
else:
    os.environ["LC_AL"] = "en_US.utf-8"
    os.environ["LANG"] = "en_US.utf-8"

import gpt_2_simple as gpt2
import numpy as np
import tweepy


class TweetBot():    
    def __init__(self):
        super(TweetBot, self).__init__()
        

    def generate_text(self,
        checkpoint_dir,
        length,
        temperature,
        destination_path,
        prefix,
        return_as_list,
    ):
        sess = gpt2.start_tf_sess()
        gpt2.load_gpt2(sess, checkpoint_dir=checkpoint_dir)
        text = gpt2.generate(
            sess,
            checkpoint_dir=checkpoint_dir,
            length=length,
            temperature=temperature,
            destination_path=destination_path,
            prefix=prefix,
            return_as_list=return_as_list,
        )
        return text


    def tweet(self, 
        checkpoint_dir,
        twitter_credential_path,
        length,
        temperature,
        prefix,
        delimiter,
    ):
        print(os.getcwd())
        # Parse the credentials for the twitter bot
        with open(twitter_credential_path, "r") as json_file:
            twitter_creds = json.load(json_file)

        # Set the credentials based on the credentials file
        CONSUMER_KEY = twitter_creds["consumer_key"]
        CONSUMER_SECRET = twitter_creds["consumer_secret"]
        ACCESS_KEY = twitter_creds["access_key"]
        ACCESS_SECRET = twitter_creds["access_secret"]

        # Authenticate with the Twitter API
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        api = tweepy.API(auth)

        # Generate some text
        generated_text = self.generate_text(
            checkpoint_dir, length, temperature, None, prefix, return_as_list=True
        )

        split_text = generated_text[0].split(delimiter)

        # Filter out all examples which are longer than twitter's 280 character limit
        valid_text = [x for x in split_text if len(x) <= 280]

        # TWEET!!!
        current_tweet = np.random.choice(valid_text, 1)
        api.update_status(current_tweet[0])
        print(current_tweet)

    
    def finetune(self, 
        model_name,
        text_path,
        checkpoint_dir,
        num_steps,
        sample_length,
        save_every,
    ):

        # Download the model if it is not present
        if not os.path.isdir(os.path.join("models", model_name)):
            print(f"Downloading {model_name} model...")
            gpt2.download_gpt2(model_name=model_name)

        sess = gpt2.start_tf_sess()

        if save_every is None:
            save_every = int(num_steps / 4)

        gpt2.finetune(
            sess,
            text_path,
            model_name=model_name,
            steps=num_steps,
            sample_length=sample_length,
            save_every=save_every,
            checkpoint_dir=checkpoint_dir,
        )  # steps is max number of training steps

        gpt2.generate(sess, checkpoint_dir=checkpoint_dir)

    def generate(self, 
        checkpoint_dir,
        length,
        temperature,
        destination_path,
        prefix,
    ):
        text = self.generate_text(checkpoint_dir, length, temperature, destination_path, prefix, False)        
        print(text)
    
    def post_tweet(self, checkpoint_dir, twitter_credential_path):
        self.tweet(checkpoint_dir, twitter_credential_path, 1024, 0.8, None, "\n==========\n")


if __name__ == "__main__":
    # TweetBot().finetune("355M", "./output.csv", "checkpoint", 3000, 1024, None)
    #TweetBot().post_tweet("checkpoint","twitter.json")

    TweetBot().generate("checkpoint", 1023, 1.0, None, None)
