from transformers import pipeline

# Load summarization pipeline with Facebook BART model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Your long text
text = """
Hi, this is AJ with another effortless English podcast.
So today is Monday and I'm here in San Francisco.
I'm back in San Francisco.
Last week we were in Texas. We were at a teaching conference and the leader of the teaching conference was Blaine Ray.
And first I just want to say some nice things about Blaine Ray because he's a super nice person. 
He's a fantastic teacher. He's a great teacher trainer. He really helps teachers become better and better. 
And I went to Moe went and Kristen went and Joe went. We all learned a lot.
We will all improve our teaching as a result of going to the conference. So thank you Blaine Ray.
You are great. See the next thing that happened last week was that our computers crashed. Oh no, oh no.
Yes our website crashed. So what happened? First we got too many visitors. We got a lot of traffic.
People watching the videos and trying to comment all suddenly same time. So that crashed our site.
Our website went down. But you know that's okay. That's not a terrible problem. Usually you can recover quickly. But the next problem was that our backup file, our website backup had a problem.
The website host, Bluehost, Pugh. Terrible. Don't use them. Bluehost, their backup file was bad. It had some, it was corrupt is what they say. But it basically had some problems. It was broken a little bit.
So we could not get the website up again quickly. So finally our computer engineer, his name is Vic Medcalf. He worked hard, he worked, he worked. Trying to talk to Bluehost again and again. Finally he got a good backup file. Then we moved everything to new computers, new servers and a new web host.
Doing expensive, high quality and professional. So now we are ready for a lot of traffic suddenly. And that's good because our English is coming soon. Our one day only sale. Unfortunately we must change the date again. We were hoping for tomorrow. But because our website crashed last week we need to delay. Our English just one more week. So the new date, the final date, the one day only sale for Power English is now August 4th. 
August 4th, that's next Tuesday, August 4th. One day only Power English sale. Now to get Power English you must be on my email list. You must join the 7 Rules email course. Because what happens at 12.01 am. Just after midnight in New York City, that's New York City time, I will send an email to everybody in the 7 Rules email list. That actually will be almost 1 million people. Because our friends, Kristen and Joe, they are also sending emails. Anyway, you will get an email and it will have a link inside. 

"""

# Generate summary
summary = summarizer(text, max_length=100, min_length=20, do_sample=False)

# Print result
print("Summary:", summary[0]['summary_text'])
