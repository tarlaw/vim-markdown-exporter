import vim
import markdown2

MD_EXTRAS = {
    'inline-css': {
        'sup': 'color:#6D6D6D; font-size:1ex;',
        'inline-code': 'color: #000000; font-family: monospace,monospace; padding: 0.1em 0.2em; ' \
            'margin: 0.1em; font-size: 85%; background-color: #F5F5F5; border-radius: 3px; ' \
            'border: 1px solid #cccccc;',
        'body': ';',
        'blockquote': 'border-left: .5ex solid #BFBFBF; margin-left: 0px; padding-left: 1em; ' \
            'margin-top: 1.4285em; margin-bottom: 1.4285em; ',
        'footnotes': 'border-top: 1px solid #9AB39B; font-size: 80%;',
        'tr:even': 'border: 1px solid #DDD; padding: 6px 13px; background-color: #F8F8F8;',
        'pre': 'color: #000000; font-family: monospace,monospace; font-size: 0.9em; ' \
            'white-space: pre-wrap; word-wrap: break-word; border: 1px solid #cccccc; ' \
            'border-radius: 3px; overflow: auto; padding: 6px 10px; margin-bottom: 10px;',
        'h1': 'margin-bottom: 1em; margin-top: 1.2em;',
        'td': 'border: 1px solid #DDD; padding: 6px 13px;',
        'hr': 'color: #9AB39B; background-color: #9AB39B; height: 1px; border: none;',
        'th': 'border: 1px solid #DDD; padding: 6px 13px;',
        'code': 'color: black; font-family: monospace,monospace; font-size: 0.9em;',
        'table': 'border-collapse: collapse; border-spacing: 0; margin: 1em;',
        'tr:odd': 'border: 1px solid #DDD; padding: 6px 13px;'
    },
    'fenced-code-blocks': {
        'noclasses': True,
        'cssclass': '',
        'style': 'github'
    },
    'metadata': None,
    'cuddled-lists': None,
    'code-friendly': None,
    'markdown-in-html': None,
    'footnotes': None,
    'tables': None,
}

#
def MarkdownToHTML(title, content):
    body = markdown2.markdown(content, extras = MD_EXTRAS)

    contentHTML = '<html><head><title>'
    contentHTML += title
    contentHTML += '</title><body>'
    contentHTML += body
    contentHTML += '</body></html>'

    return contentHTML

#
def MarkdownExport(path):
    lines = vim.current.buffer[:]

    content = ''
    title = ''
    if len(lines) > 0:
        title = lines.pop(0).strip()
        while len(lines) >0:
            if lines[0].strip() == '':
                lines.pop(0)
            else:
                break

    for line in lines:
        content += ('%s\n' % line)

    contentHTML = MarkdownToHTML(title, content)

    open(path, 'w').write(contentHTML)
