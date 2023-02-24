import typer

from typing import Optional
from core import (
    subdomain_parser,
    list_all_target,
    list_subdomains,
)

app = typer.Typer()


@app.command()
def add_subdomains(
    target: str = typer.Argument(..., "--target", "-t", help="Name of target"),
    subdomains: str = typer.Argument(..., "--file", "-f", help="File with subdomains"),
):
    """
    Add subdomains to target
    """
    subdomain_parser(target, subdomains)


@app.command()
def list_all_targets() -> None:
    """
    List all targets
    """
    list_all_target()


@app.command()
def list_subdomains(
    target: str = typer.Argument(..., "--target", "-t", help="Name of target")
):
    """
    List subdomains of target
    """
    list_subdomains(target)