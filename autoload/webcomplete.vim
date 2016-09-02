let s:script = expand('<sfile>:h:h') . "/sh/webcomplete"

function! webcomplete#complete(findstart, base)
  if a:findstart
    return webcomplete#findstart()
  else
    return webcomplete#completions(a:base)
  endif
endfunction

function! webcomplete#findstart()
  let line = getline('.')
  let start = col('.') - 1

  while start > 0 && line[start - 1] =~ '\a'
      let start -= 1
  endwhile

  return start
endfunction

function! webcomplete#completions(base)
  let command  =  'sh ' . shellescape(s:script)
  let command .= '| grep ' . shellescape(a:base)

  let completions = system(command)

  if v:shell_error != 0
      return []
  endif

  return split(completions, '\n')
endfunction
