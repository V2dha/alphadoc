import click
import autopep8


@click.command()
#basic options
@click.option('--convention', default='PEP-8', help='Convention that you want to use for your code. Options right now available are PEP-8 and PEP-257', type=str)

def main(convention):
    """
    Python-cli is a tool to help you document your code better 
    aligning to the PEP convention styles!
    """
    click.echo('Selected convention style for your code is {}'.format(convention))

if __name__ == "__main__":
    main()