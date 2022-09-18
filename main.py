import typer;
import rich;
import ml;
import speech as sr;
cli = typer.Typer();

@cli.command()
def blog():
    rich.print("🎤 [bold green]What is the title of your blog post? Please speak the answer outloud.[/bold green]");
    title = sr.listen();
    title_accurate = verify_input(title);
    while(not title_accurate):
        rich.print("🎤 [bold green]Try again! What is the title of your blog post? Please speak the answer outloud.[/bold green]");
        title = sr.listen();
        title_accurate = verify_input(title);

    rich.print("🎤 [bold green]Perfect! What audience is this blog for? Please speak the answer outloud.[/bold green]");
    audience = sr.listen();
    audience_accurate = verify_input(audience);
    while(not audience_accurate):
        rich.print("🎤 [bold green]Try again! What audience is this blog for? Please speak the answer outloud.[/bold green]");
        audience = sr.listen();
        audience_accurate = verify_input(audience);

    rich.print("🎤 [bold green]Lastly - what do you want the tone of the blog post to be? Please speak the answer outloud.[/bold green]");
    tone = sr.listen();
    tone_accurate = verify_input(tone);
    while(not tone_accurate):
        rich.print("🎤 [bold green]Try again! What do you want the tone of the blog post to be? Please speak the answer outloud.[/bold green]");
        tone = sr.listen();
        tone_accurate = verify_input(tone);

    result = ml.blog_post(title["result"], audience["result"], tone["result"])[:-2];
    rich.print();
    rich.print("✅ [bold green]We got a response![/bold green]");
    rich.print(result);
    sr.speak("Your result is. " + result)
    return;

@cli.command()
def freestyle():
    rich.print("🎤 [bold green]What do you want the first line of your song hook to be? Please speak the answer outloud[/bold green]");
    first_line = sr.listen();
    first_line_accurate = verify_input(first_line);
    while(not first_line_accurate):
        rich.print("🎤 [bold green]Try again! What do you want the first line of your song hook to be? Please speak the answer outloud.[/bold green]");
        first_line = sr.listen();
        first_line_accurate = verify_input(first_line);

    result = ml.freestyle_bot(first_line["result"])[:-2];
    rich.print();
    rich.print("✅ [bold green]We got a response![/bold green]");
    rich.print(result);
    sr.speak("Your result is. " + result)
    return;

@cli.command()
def summarizer():
    rich.print("🎤 [bold green]What do you want to summarize? Please speak the answer outloud.[/bold green]");
    text = sr.listen();
    text_accurate = verify_input(text);
    while(not text_accurate):
        rich.print("🎤 [bold green]Try again! What do you want to summarize? Please speak the answer outloud.[/bold green]");
        text = sr.listen();
        text_accurate = verify_input(text);

    result = ml.summarizer(text["result"])[:-2];
    rich.print();
    rich.print("✅ [bold green]We got a response![/bold green]");
    rich.print(result);
    sr.speak("Your result is. " + result)
    return;

def verify_input(input: object):
    rich.print();
    if("error" in input):
        rich.print("❌ [bold red]Something went wrong: " + input["error"] + "[/bold red]");
        return False;

    rich.print("[bold orange]We think you said: " + input["result"] + "[/bold orange]");
    result = typer.prompt("Is this correct? (y/n): ").lower();
    return result == "y";

if __name__ == "__main__":
    cli();
