if get(s:, 'loaded', 0)
    finish
endif
let s:loaded = 1

let g:coc_webcomplete_enabled = get(g:, 'coc_webcomplete_enabled',  1)

let g:coc_webcomplete_script = get(g:, 'coc_webcomplete_script',
            \ expand('<sfile>:h:h:h:h') . "/sh/webcomplete")

function! coc#source#webcomplete#init() abort
    return {
                \ 'priority': 1,
                \ 'shortcut': 'WEB',
                \ }
endfunction

function! coc#source#webcomplete#complete(opt, callback) abort
    let Callback = function('s:ListToDict', [a:callback]) " wrap callback
    let s:is_enabled = get(b:, 'coc_webcomplete_enabled',
                \ get(g:, 'coc_webcomplete_enabled', 1))
    if ! s:is_enabled
        return
    endif
    call coc#source#webcomplete#gather_candidates(Callback)
endfunction

function! s:ListToDict(callback, items)
    let res = []
    for item in a:items
        call add(res, {'word' : item})
    endfor
    call a:callback(res)
endfunction

function! s:on_stdout_nvim(job_id, data, event) dict
    let self.output[-1] .= a:data[0]
    call extend(self.output, a:data[1:])
endfunction

function! s:on_exit_nvim(job_id, data, event) dict
    " drop the last (empty) item
    let candidates = self.output[: -2]
    call self.callback(candidates)
endfunction

function! s:on_output_vim(channel, message) dict
    call add(self.output, a:message)
endfunction

function! s:on_exit_vim(job, status) dict
    " drop the first (empty) item
    let candidates = self.output[1 :]
    call self.callback(candidates)
endfunction

function! coc#source#webcomplete#gather_candidates(callback)
    let command = g:coc_webcomplete_script
    let context = {
                \ 'output':   [''],
                \ 'callback': a:callback,
                \ }

    if has('nvim')
        call jobstart(command, {
                    \ 'on_stdout': function('s:on_stdout_nvim', context),
                    \ 'on_exit':   function('s:on_exit_nvim', context),
                    \ })
    else
        call job_start(command, {
                    \ 'out_cb':  function('s:on_output_vim', context),
                    \ 'exit_cb': function('s:on_exit_vim', context),
                    \ })
    endif
endfunction
