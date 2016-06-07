" Gathers completions of the words in the
" currently opened word in chrome
function! webcomplete#gather_candidates()
	let completions = system('webcomplete')
	if v:shell_error != 0
		return []
	endif
	return split(completions, '\n')
endfunction
