import click

from server import get_connection


@click.group()
def server():
    pass


@server.command()
@click.argument('host')
# @click.password_option()
@click.argument('password')
@click.pass_context
def connect(ctx, host, password):
    click.echo('Connection...')
    ctx.obj = get_connection(host, password)
    click.echo(click.style('Successful!', fg='green'))
    click.echo(ctx)


@server.command()
@click.pass_context
def info(ctx):
    click.echo(ctx)


if __name__ == '__main__':
    server()
