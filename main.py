import typer;
from rich import print;
from speechRecognition import listen;
cli = typer.Typer();

@cli.command()
def blog():
    print("[bold green]title[/bold green]: ");
    title = listen();
    verify_input(title);

    print("[bold green]content[/bold green]: ");
    audience = listen();
    verify_input(audience);

    print("[bold green]audience[/bold green]: ");
    tone = listen();
    verify_input(tone);
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

def verify_input(input: str):
    result = typer.prompt("You said: " + input + ". [bold red]Is this correct? (y/n)").lower();
    return result == "y";

if __name__ == "__main__":
    cli();
