from src.app import replace_all, repl_dict


def test_replace_all():
    text = "!MF, this is a !mf test"
    result = replace_all(text, repl_dict)

    assert result == "motherfucker, this is a motherfucking test"
