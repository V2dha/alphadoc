from main import main
from click.testing import CliRunner

def test_main(): 
    runner = CliRunner()
    result = runner.invoke(main)
    assert result.exit_code == 0
    assert 'Selected convention style for your code is PEP-8\n' in result.output

# def test_hello_world():
#   runner = CliRunner()
#   result = runner.invoke(hello)
#   assert result.exit_code == 0
#   assert result.output == 'hello'