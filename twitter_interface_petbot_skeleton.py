from petbot import Pet

class twitter_pet_interface():

    def __init__(self):
        self.initFile=''
        try:
            Pet(self.initFile)
        except IOError:
            Pet()
            print 'Init Values not found, initializing Pet class with default values'

        self.tweet_user_mapping(self.check_replies())
        self.increment_pet_hunger()
        self.update_profile_pic()
        self.main_status_tweet()
        self.write_pet_status()

    def check_replies(self):
        #gets data with twitter API reply call

        #loads data looks for user and tweet

        #parses data into map with dictionary--user: list of tweets

        #returns dict

    def tweet_user_mapping(self, user_mapping):
        #parse mapping

        #loop through all tweets per user

        #tweet pet's responses at users
        
    def increment_pet_hunger():
        #since this program is called every 5? minutes, increment pet hunger everytime

    def update_profile_pic(self):
        #get pet's mood

        #get pet's hunger

        #if elif statement for mood and hunger for images

        #http post call with encoded image data


    def main_status_tweet(self):

        #get pet's status
    
    def write_pet_status(self):
    
      #get pet's mood
      #get pet's hunger
      #write to initFile specified at the beginning
