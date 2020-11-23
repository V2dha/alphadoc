from click.testing import CliRunner
from main import main
from docstring import get_docstring

def test_main(): 
    runner = CliRunner()
    result = runner.invoke(main, ['alphadoc/comment.py'])
    assert result.exit_code == 0
    assert "Function 1 : get_comments\n-----------------------\nFunction 2 : get_comment_blocks\n-----------------------\nFunction 3 : get_doc_blocks\n-----------------------\n" in result.output

