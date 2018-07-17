if get(s:, 'loaded', 0)
    finish
endif
let s:loaded = 1

let g:ncm2_webcomplete_enabled = get(g:, 'ncm2_webcomplete_enabled',  1)

let g:ncm2_webcomplete#proc = yarp#py3('ncm2_webcomplete')

let g:ncm2_webcomplete#source = get(g:, 'ncm2_webcomplete#look_source', {
            \ 'name': 'web',
            \ 'priority': 6,
            \ 'mark': 'web',
            \ 'on_complete': 'ncm2_webcomplete#on_complete',
            \ 'on_warmup': 'ncm2_webcomplete#on_warmup'
            \ })

let g:ncm2_webcomplete#source = extend(g:ncm2_webcomplete#source,
            \ get(g:, 'ncm2_webcomplete#source_override', {}),
            \ 'force')

function! ncm2_webcomplete#init()
    call ncm2#register_source(g:ncm2_webcomplete#source)
endfunction

function! ncm2_webcomplete#on_warmup(ctx)
    call g:ncm2_webcomplete#proc.jobstart()
endfunction

function! ncm2_webcomplete#on_complete(ctx)
    let s:is_enabled = get(b:, 'ncm2_webcomplete_enabled',
                \ get(g:, 'ncm2_webcomplete_enabled', 1))
    if ! s:is_enabled
        return
    endif
    call g:ncm2_webcomplete#proc.try_notify('on_complete', a:ctx)
endfunction
