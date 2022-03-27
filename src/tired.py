from flask import Flask
import newspaper
from sentence_transformers import SentenceTransformer, util
import json
import nltk

app = Flask('app')


@app.route('/')
def generate_articles():

	# The various News Sources we will like to web scrape from
	wp = newspaper.build('https://www.washingtonpost.com/politics/', memoize_articles=False, language='en')
	fox = newspaper.build("https://www.foxnews.com/politics", memoize_articles=False, language='en')

	#sentence similarity delclarations
	chosen_two = [None,None]
	current_sim_threshold = 0
	model = SentenceTransformer('all-MiniLM-L6-v2')
	count = 0.00000

	#find similarity between each left and right article
	for left_article in wp.articles:
	
	    left_article.download()
	    try:
	        left_article.parse()
	        left_article.nlp()
	
	        if "politics" in left_article.source_url and left_article.title != None and left_article.summary != None:
	            left_emb = model.encode(left_article.summary)
	
	            for right_article in fox.articles:
	                right_article.download()
	                try:
	                    right_article.parse()
	                    right_article.nlp()
	
	                    if "politics" in right_article.source_url and right_article.title != None and right_article.summary != None:
	                        right_emb = model.encode(right_article.summary)
	                        cos_sim = util.cos_sim(left_emb, right_emb)
	                        if current_sim_threshold <= cos_sim.item():
	                            chosen_two[0] = left_article
	                            chosen_two[1] = right_article
	                            current_sim_threshold = cos_sim
	                except:
	                    print('URL Problem. Cannot parse')
	                    break
	    except:
	        print('URL Problem. Cannot parse')
	        break

	#place in json format
	left_dictionary = {
	        'Title': chosen_two[0].title,
	        'Text': chosen_two[0].text,
	        'Summary': chosen_two[0].summary,
	        'Publish Date': chosen_two[0].publish_date,
	        'Source': chosen_two[0].source_url
	        }
	
	right_dictionary = {
	        'Title': chosen_two[1].title,
	        'Text': chosen_two[1].text,
	        'Summary': chosen_two[1].summary,
	        'Publish Date': chosen_two[1].publish_date,
	        'Source': chosen_two[1].source_url
	        }
	
	left_data = json.dumps(left_dictionary, indent=5)
	right_data = json.dumps(right_dictionary, indent=5)

	#upload to json file
	with open("left.json", "w") as outfile:
	    outfile.write(left_data)
	outfile.close()
	
	with open("right.json", "w") as outfile:
	    outfile.write(right_data)
	outfile.close()


app.run(host='0.0.0.0', port=8080)