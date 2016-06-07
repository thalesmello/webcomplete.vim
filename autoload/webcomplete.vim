let s:script = expand('<sfile>:h:h') . "/sh/webcomplete"

" Gathers completions of the words in the
" currently opened word in chrome
function! webcomplete#gather_candidates()
	let completions = system('sh ' . s:script)
	if v:shell_error != 0
		return []
	endif
	return split(completions, '\n')
endfunction
