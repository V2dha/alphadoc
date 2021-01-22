from click.testing import CliRunner
from alphadoc.main import main

def test_main(): 
    runner = CliRunner()
    result = runner.invoke(main, ['tests/sample.py'])
    assert result.exit_code == 0
    assert "Function 1 : top_level_functions\n-----------------------\nFunction 2 : parse_ast\n-----------------------\nFunction 3 : get_func\n-----------------------\n" in result.output

