from behave import step


@step('Entrar na página "{page}"')
def test(context, page):
    try:
        context.browser.get(page)
    except:
        assert False, 'Error to load page'
