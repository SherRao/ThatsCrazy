import typer;
import ml;
import speech as sr;
cli = typer.Typer();

@cli.command()
def blog():
    titlePrompt = typer.style("🎤  What is the title of your blog post? Please speak the answer outloud.", fg=typer.colors.GREEN, bold=True);
    typer.echo(titlePrompt);

    title = sr.listen();
    title_accurate = verify_input(title);
    while(not title_accurate):
        tryAgainPrompt = typer.style("🎤  Try again! What is the title of your blog post? Please speak the answer outloud.", fg=typer.colors.YELLOW, bold=True);
        typer.echo(tryAgainPrompt);
        title = sr.listen();
        title_accurate = verify_input(title);

    audiencePrompt = typer.style("🎤  Who is your audience? Please speak the answer outloud.", fg=typer.colors.GREEN, bold=True);
    typer.echo(audiencePrompt);

    audience = sr.listen();
    audience_accurate = verify_input(audience);
    while(not audience_accurate):
        tryAgainPrompt = typer.style("🎤  Try again! Who is your audience? Please speak the answer outloud.", fg=typer.colors.YELLOW, bold=True);
        typer.echo(tryAgainPrompt);
        audience = sr.listen();
        audience_accurate = verify_input(audience);

    tonePrompt = typer.style("🎤  What is the tone of your blog post? Please speak the answer outloud.", fg=typer.colors.GREEN, bold=True);
    typer.echo(tonePrompt);

    tone = sr.listen();
    tone_accurate = verify_input(tone);
    while(not tone_accurate):
        tryAgainPrompt = typer.style("🎤  Try again! What is the tone of your blog post? Please speak the answer outloud.", fg=typer.colors.YELLOW, bold=True);
        typer.echo(tryAgainPrompt);
        tone = sr.listen();
        tone_accurate = verify_input(tone);

    result = ml.blog_post(title["result"], audience["result"], tone["result"])[12:-2];
    output_result(result);
    return;

@cli.command()
def freestyle():
    promptText = typer.style("🎤  What do you want the first line of your song hook to be? Please speak the answer outloud", fg=typer.colors.GREEN, bold=True);
    typer.echo(promptText);

    first_line = sr.listen();
    first_line_accurate = verify_input(first_line);
    while(not first_line_accurate):
        tryAgainPrompt = typer.style("🎤  Try again! What do you want the first line of your song hook to be? Please speak the answer outloud", fg=typer.colors.YELLOW, bold=True);
        typer.echo(tryAgainPrompt);
        first_line = sr.listen();
        first_line_accurate = verify_input(first_line);

    result = ml.freestyle_bot(first_line["result"])[12:-2];
    output_result(result);
    return;

@cli.command()
def summarizer():
    promptText = typer.style("🎤  What do you want to summarize? Please speak the answer outloud", fg=typer.colors.GREEN, bold=True);
    typer.echo(promptText);

    text = sr.listen();
    text_accurate = verify_input(text);
    while(not text_accurate):
        tryAgainPrompt = typer.style("🎤  Try again! What do you want to summarize? Please speak the answer outloud", fg=typer.colors.YELLOW, bold=True);
        typer.echo(tryAgainPrompt);
        text = sr.listen();
        text_accurate = verify_input(text);

    result = ml.summarizer(text["result"])[12:-2];
    output_result(result);
    return;

def verify_input(input: object):
    typer.echo();
    if("error" in input):
        errorPromptText = typer.style("❌  Something went wrong: ", fg=typer.colors.RED, bold=True);
        errorPromptText2 = typer.style(input["error"], fg=typer.colors.BRIGHT_RED, bold=False)
        typer.echo(errorPromptText + errorPromptText2);
        return False;

    thinkPrompt = typer.style("❓  We think you said: " + input["result"], fg=typer.colors.CYAN, bold=True);
    typer.echo(thinkPrompt);

    promptText = typer.style("❓  Is this correct? (y/n): ", fg=typer.colors.CYAN, bold=True);
    result = typer.prompt(promptText, default="y").lower();
    return result == "y";

def output_result(result: object):
    resultText = typer.style("🥳  We got a response!", fg=typer.colors.GREEN, bold=True);
    typer.echo();
    typer.echo(resultText);
    typer.echo(result);
    sr.speak("Your result is. " + result);

if __name__ == "__main__":
    typer.echo(typer.style("", fg=typer.colors.RESET, bg=typer.colors.RESET));
    cli();
