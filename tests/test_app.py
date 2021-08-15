from src.app import replace_all, repl_dict, get_help_message


def test_replace_all():
    text = "!MF, this is a !mf test"
    result = replace_all(text, repl_dict)

    assert result == "motherfucker, this is a motherfucking test"


def test_get_help_message():
    result = get_help_message()

    all_match = True
    for k, v in repl_dict.items():
        if k not in result or v not in result:
            all_match = False
            break

    assert all_match
