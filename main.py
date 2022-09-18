import typer;
import rich;
# import ml;
from speechRecognition import listen;
cli = typer.Typer();

@cli.command()
def blog():
    rich.print("🎤 [bold green]What is the title of your blog post? Please speak the answer outloud.[/bold green]");
    title = listen();
    title_accurate = verify_input(title);
    while(not title_accurate):
        rich.print("🎤 [bold green]Try again! What is the title of your blog post? Please speak the answer outloud.[/bold green]");
        title = listen();
        title_accurate = verify_input(title);

    rich.print("🎤 [bold green]Perfect! What audience is this blog for? Please speak the answer outloud.[/bold green]");
    audience = listen();
    audience_accurate = verify_input(audience);
    while(not audience_accurate):
        rich.print("🎤 [bold green]Try again! What audience is this blog for? Please speak the answer outloud.[/bold green]");
        audience = listen();
        audience_accurate = verify_input(audience);

    rich.print("🎤 [bold green]Lastly - what do you want the tone of the blog post to be? Please speak the answer outloud.[/bold green]");
    tone = listen();
    tone_accurate = verify_input(tone);
    while(not tone_accurate):
        rich.print("🎤 [bold green]Try again! What do you want the tone of the blog post to be? Please speak the answer outloud.[/bold green]");
        tone = listen();
        tone_accurate = verify_input(tone);

    # ml.blog_post(title.result, audience.result, tone.result);
    pass;

@cli.command()
def sentiment():
    text = listen();
    verify_input(text);
    pass;

@cli.command()
def freestyle():
    first_line = listen();
    verify_input(first_line);
    pass;

@cli.command()
def summarizer():
    text = listen();
    verify_input(text);
    pass;

def verify_input(input: object):
    if("error" in input):
        rich.print("❌ An error occured: " + input["error"]);
        return False;

    rich.print("✅ [bold orange]We think you said: " + input["result"] + "[/bold orange]");
    result = typer.prompt("Is this correct? (y/n): ").lower();
    return result == "y";

if __name__ == "__main__":
    cli();
