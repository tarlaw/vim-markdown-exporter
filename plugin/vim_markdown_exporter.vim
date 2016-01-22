python import sys
python import vim
python sys.path.append(vim.eval('expand("<sfile>:h")'))

function! Vim_MarkdownExport(arg1)
python << endOfPython
from vim_markdown_exporter import MarkdownExport
exportPath = vim.eval("a:arg1")
MarkdownExport(exportPath)
endOfPython
endfunction

command! -nargs=1 MarkdownExport call Vim_MarkdownExport(<f-args>)

