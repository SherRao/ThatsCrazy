import cohere
co = cohere.Client('tafccigkrHkGNU4KGeIx4Bk0xqjWQDe1xQZIGjg3')



def blog_post(title,audience,tone):
    prompt='This program will generate an introductory paragraph to a blog post given a blog title, audience, and tone of voice.\n--\nBlog Title: Best Activities in Toronto\nAudience: Millennials\nTone of Voice: Lighthearted\nFirst Paragraph: Looking for fun things to do in Toronto? When it comes to exploring Canada\'s largest city, there\'s an ever-evolving set of activities to choose from. Whether you\'re looking to visit a local museum or sample the city\'s varied cuisine, there is plenty to fill any itinerary. In this blog post, I\'ll share some of my favorite recommendations\n--\nBlog Title: Mastering Dynamic Programming\nAudience: Developers\nTone: Informative\nFirst Paragraph: In this piece, we\'ll help you understand the fundamentals of dynamic programming, and when to apply this optimization technique. We\'ll break down bottom-up and top-down approaches to solve dynamic programming problems.\n-',
    print(prompt)
    prompt+='-\nBlog Title: '+title+'\n',
    prompt+='Audience: '+audience+'\n',
    prompt+='Tone of Voice: '+tone+'\n',
    prompt+="First Paragraph:",
    response = co.generate(
    model='xlarge',
    prompt=prompt,
   
    max_tokens=100,
    temperature=0.8,
    k=0,
    p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop_sequences=["--"],
    return_likelihoods='NONE')
    #print('Prediction: {}'.format(response.generations[0].text))
    
def freestyle_bot(first_line):
    
    prompt=f"""This program will generate a hook to a song given the first line.
--
First Line: Hey, I just met you, and this is crazy
Hook: Hey, I just met you, and this is crazy, But here's my number, so call me, maybe It's hard to look right at you, baby But here's my number, so call me, maybe Hey, I just met you, and this is crazy But here's my number, so call me, maybe And all the other boys try to chase me But here's my number, so call me, maybe
--
First Line: Sweet Caroline
Hook: Sweet Caroline Good times never seemed so good I've been inclined. To believe they never would. To believe they never would, Oh no no   
--
First Line: I'm on my way Driving at 90 down those country lanes
Hook: I'm on my way Driving at 90 down those country lanes Singing to Tiny Dancer And I miss the way you make me feel, and it's real When we watched the sunset over the castle on the hill
--
First Line: 'Cause all of me loves all of you
Hook: 'Cause all of me loves all of you Love your curves and all your edges All your perfect imperfections Give your all to me, I'll give my all to you You're my end and my beginning Even when I lose, I'm winning
--
First Line: Cause baby, you're a firework
Hook: Cause baby, you're a firework Come on, show 'em what you're worth Make 'em go, "Oh, oh, oh" As you shoot across the sky Baby, you're a firework Come on, let your colors burst Make 'em go, "Oh, oh, oh" You're gonna leave 'em all in awe, awe, awe
--
First Line: 'Cause he seems like he's good for you
Hook: 'Cause he seems like he's good for you And he makes you feel like you should And all your friends say he's the one His love for you is true (hey)

--
First Line: Just gonna stand there and watch me burn
Hook: Just gonna stand there and watch me burn? Well, that's alright, because I like the way it hurts Just gonna stand there and hear me cry? 
Well, that's alright, because I love the way you lie I love the way you lie I love the way you lie
--
First Line: I'm gonna pop some tags
Hook: I'm gonna pop some tags Only got twenty dollars in my pocket I, I, I'm hunting, looking for a come-up This is fucking awesome
--
First Line:I blame it on the model broad with the Hollywood smile
Hook: I blame it on the model broad with the Hollywood smile, ow Stripper booty and a rack like wow Brain like Berkeley Met her at Coachella I went to see Jigga, she went to see Z Trip Perfect
--
First Line: But girl I can't feel my face
Hook: But girl I can't feel my face What are we smokin' anyway? She said don't let the high go to waste But can you taste a little taste Novacane, baby, baby Novacane, baby, I want you
--
First Line: Yeah, I be yelling out money over everything
Hook: Yeah, I be yelling out money over everything, money on my mind Then she wanna ask when it got so empty Tell her I apologize it happened 
over time She says they missed the old drake, girl don't tempt me
--
First Line: Jetson came in with a FN Two girls with him
Hook: Jetson came in with a FN Two girls with him, told me he ain't got a preference (yeah) Sat them both down and I asked a few questions Met last week and they already best friends (oh-ooh) Already best friends (friends) Met last week and they already best friends (best friends) Met last week and they already best friends (oh-oh)
--
First Line: {first_line}
Hook:"""
    response = co.generate(
        model='xlarge',
        prompt = prompt,
        max_tokens=150,
        temperature=1,
        k=0,
        p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop_sequences=["--"],
        return_likelihoods='NONE')
    print('Prediction: {}'.format(response.generations[0].text))



def summarizer(input):
    prompt=f"""Passage: Is Wordle getting tougher to solve? Players seem to be convinced that the game has gotten harder in recent weeks ever since The New York Times bought it from developer Josh Wardle in late January. The Times has come forward and shared that this likely isn’t the case. That said, the NYT did mess with the back end code a bit, removing some offensive and sexual language, as well as some obscure words There is a viral thread claiming that a confirmation bias was at play. One Twitter user went so far as to claim the game has gone to “the dusty section of the dictionary” to find its latest words.

TLDR: Wordle has not gotten more difficult to solve.
--
Passage: ArtificialIvan, a seven-year-old, London-based payment and expense management software company, has raised $190 million in Series C funding led by ARG Global, with participation from D9 Capital Group and Boulder Capital. Earlier backers also joined the round, including Hilton Group, Roxanne Capital, Paved Roads Ventures, Brook Partners, and Plato Capital.

TLDR: ArtificialIvan has raised $190 million in Series C funding.
--
Passage: I'm a server. I haven't worked since the 14th, but was officially laid off on the 18th. Where I am, temporary layoff is only 60 days. If we are not back by then, we lose our jobs permanently. It couldn't have come at a worse time since we have new management and there's been some murmurs about getting new staff. I was about to lose my apartment (unrelated) but my landlord phoned me up to let me know that he is no 
longer making me leave and not to worry about April rent. He also gave me $150 to go buy groceries. He's a bro. I'm trying to get through to EI, which is all online right now, but the site keeps crashing so I'm unable to make a claim right now.
TLDR: I was about to lose my apartment (unrelated) but my landlord phoned me up to let me know that he is no longer making me leave. I'm trying to get through to EI, which is all online right now, but the site keeps crashing.
--
Passage: I was laid off from my 5 year graphic design job, working for a screen printing and promotional products company. About half of our business involves schools, sports, and events. Obviously none of that is happening currently, so our business has stagnated. They are going to 
try to operate with a skeleton crew for the next couple months. The hope is to bring everyone back eventually, but I'm not optimistic.        
TLDR: I was laid off from my 5 year graphic design job, working for a screen printing and promotional products company. They are going to try 
to operate with a skeleton crew for the next couple months. The hope is to bring everyone back eventually, but I'm not optimistic.
--
Passage: My grandmother is from Ireland (I live in the US) and honestly probably should've kicked the bucket years ago. She absolutely hates England, and my brother and I have had a running joke for years that she's holding on through sheer spite to see the queen die first. I found out about the queen because he texted me saying "guess grandma is kicking the bucket next week"
TLDR: He found out about it because he texted me saying "guess grandma is kicking the bucket next week". My grandmother is from Ireland and absolutely hates England, and my brother and I have had a running joke that she's holding on through sheer spite to see the queen die first.    
--
Passage: Butterfingers are super gross now, bought one out of a vending machine and thought it was bad, googled it to find a bunch of people complaining about it. How do you screw up so bad? It’s probably cheaper but I’d think you’d lose enough sales to counter that. I won’t buy one 
again for sure.
TLDR: Supermarket produce in general. Puts the cart before the horse and its worn people down until they don't know what 'real' food tastes like. Some go so far as to 'flavor inject' it after with industrial flavors, like 'purple' (artificial concord grape) like the Grapple.
--
Passage: {input}
TLDR:"""
    response = co.generate(
        model='xlarge',
        prompt= prompt,
        max_tokens=100,
        temperature=0.8,
        k=0,
        p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop_sequences=["--"],
        return_likelihoods='NONE')
    print('Prediction: {}'.format(response.generations[0].text))
#freestyle_bot("Life is missery, I am sad, why do I love you so much")
#summarizer("To be fair, you have to have a very high IQ to understand Rick and Morty. The humor is extremely subtle, and without a solid grasp of theoretical physics most of the jokes will go over a typical viewer's head. There's also Rick's nihilistic outlook, which is deftly woven into his characterisation - his personal philosophy draws heavily fromNarodnaya Volya literature, for instance. The fans understand this stuff; they have the intellectual capacity to truly appreciate the depths of these jokes, to realize that they're not just funny- they say something deep about LIFE.")
#blog_post("elon musk","children","sarcastic")