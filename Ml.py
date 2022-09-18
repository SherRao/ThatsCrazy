import cohere
co = cohere.Client('tafccigkrHkGNU4KGeIx4Bk0xqjWQDe1xQZIGjg3')



def blog_post(title,audience,tone):
    prompt=str('This program will generate an introductory paragraph to a blog post given a blog title, audience, and tone of voice.\n--\nBlog Title: Best Activities in Toronto\nAudience: Millennials\nTone of Voice: Lighthearted\nFirst Paragraph: Looking for fun things to do in Toronto? When it comes to exploring Canada\'s largest city, there\'s an ever-evolving set of activities to choose from. Whether you\'re looking to visit a local museum or sample the city\'s varied cuisine, there is plenty to fill any itinerary. In this blog post, I\'ll share some of my favorite recommendations\n--\nBlog Title: Mastering Dynamic Programming\nAudience: Developers\nTone: Informative\nFirst Paragraph: In this piece, we\'ll help you understand the fundamentals of dynamic programming, and when to apply this optimization technique. We\'ll break down bottom-up and top-down approaches to solve dynamic programming problems.\n-'),
    prompt+='-\nBlog Title: '+title+'\n',
    prompt+='Audience: '+audience+'\n',
    prompt+='Tone of Voice: '+tone+'\n',
    prompt+="First Paragraph: ",
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
    print('Prediction: {}'.format(response.generations[0].text))
    
def Freestyle_bot(first_line):
    x=str('This program will generate a hook to a song given the first line.\n--\nFirst Line: Hey, I just met you, and this is crazy\nHook: Hey, I just met you, and this is crazy, But here\'s my number, so call me, maybe It\'s hard to look right at you, baby But here\'s my number, so call me, maybe Hey, I just met you, and this is crazy But here\'s my number, so call me, maybe And all the other boys try to chase me But here\'s my number, so call me, maybe\n--\nFirst Line: Sweet Caroline \nHook: Sweet Caroline Good times never seemed so good I\'ve been inclined. To believe they never would. To believe they never would, Oh no no\n--\nFirst Line: I\'m on my way Driving at 90 down those country lanes \nHook: I\'m on my way Driving at 90 down those country lanes Singing to Tiny Dancer And I miss the way you make me feel, and it\'s real When we watched the sunset over the castle on the hill\n--\nFirst Line: \'Cause all of me loves all of you\nHook: \'Cause all of me loves all of you Love your curves and all your edges All your perfect imperfections Give your all to me, I\'ll give my all to you You\'re my end and my beginning Even when I lose, I\'m winning\n--\nFirst Line: Cause baby, you\'re a firework \nHook: Cause baby, you\'re a firework Come on, show \'em what you\'re worth Make \'em go, \"Oh, oh, oh\" As you shoot across the sky Baby, you\'re a firework Come on, let your colors burst Make \'em go, \"Oh, oh, oh\" You\'re gonna leave \'em all in awe, awe, awe\n--\nFirst Line: \'Cause he seems like he\'s good for you\nHook: \'Cause he seems like he\'s good for you And he makes you feel like you should And all your friends say he\'s the one His love for you is true (hey)\n\n--\nFirst Line: Just gonna stand there and watch me burn\nHook: Just gonna stand there and watch me burn? Well, that\'s alright, because I like the way it hurts Just gonna stand there and hear me cry? Well, that\'s alright, because I love the way you lie I love the way you lie I love the way you lie\n--\nFirst Line: I\'m gonna pop some tags\nHook: I\'m gonna pop some tags Only got twenty dollars in my pocket I, I, I\'m hunting, looking for a come-up This is fucking awesome\n--\nFirst Line:I blame it on the model broad with the Hollywood smile\nHook: I blame it on the model broad with the Hollywood smile, ow Stripper booty and a rack like wow Brain like Berkeley Met her at Coachella I went to see Jigga, she went to see Z Trip Perfect\n--\nFirst Line: But girl I can\'t feel my face\nHook: But girl I can\'t feel my face What are we smokin\' anyway? She said don\'t let the high go to waste But can you taste a little taste Novacane, baby, baby Novacane, baby, I want you\n--\nFirst Line: Yeah, I be yelling out money over everything\nHook: Yeah, I be yelling out money over everything, money on my mind Then she wanna ask when it got so empty Tell her I apologize it happened over time She says they missed the old drake, girl don\'t tempt me\n--\nFirst Line: Jetson came in with a FN Two girls with him\nHook: Jetson came in with a FN Two girls with him, told me he ain\'t got a preference (yeah) Sat them both down and I asked a few questions Met last week and they already best friends (oh-ooh) Already best friends (friends) Met last week and they already best friends (best friends) Met last week and they already best friends (oh-oh)\n--\nFirst Line: '),
    x+=str(first_line),
    x+="\n Hook:",
    response = co.generate(
        model='xlarge',
        prompt = str(x),
        max_tokens=250,
        temperature=0.6,
        k=0,
        p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop_sequences=["--"],
        return_likelihoods='NONE')
    print('Prediction: {}'.format(response.generations[0].text))
Freestyle_bot(first_line)
