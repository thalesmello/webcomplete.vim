# webcomplete.vim

A Vim plugin that completes words from the currently open web page in your
browser.

Currently works with:

- Chrome on Mac OS.
- [Qutebrowser](https://github.com/qutebrowser/qutebrowser) on Linux and MacOS.
- Firefox [in a fork](https://github.com/kimat/webcomplete.vim).

![demo](./demo.gif)

# Installation

With [vim-plug](https://github.com/junegunn/vim-plug):

```
Plug 'thalesmello/webcomplete.vim'
```

## Using with deoplete

[`deoplete`](https://github.com/Shougo/deoplete.nvim/) is an awesome asynchronous
completion engine for Neovim. `webcomplete` works with `deoplete` out of the box.
Just start typing to see suggestions of words comming from your browser.

- `g:deoplete#sources#webcomplete#script`: Execute this command-line string
  to get a list of words instead of default internal `sh/webcomplete`. You may
  add arguments to the string, e.g. `cat /tmp/words.txt`.

## Using with ncm2

[`ncm2`](https://github.com/ncm2/ncm2/) is also supported. Once `ncm2` is configured
in your configuration files, the completions for webcomplete should be enabled by
default.

- `g:ncm2_webcomplete_script`: Same as option for deoplete, but for ncm2.

## Using with coc

[`coc`](https://github.com/neoclide/coc.nvim) is also supported. Once `coc` is configured
in your configuration files, the completions for webcomplete should be enabled by
default.

- `g:coc_webcomplete_script`: Same as option for deoplete, but for coc.

## Using with `completefunc` or `omnifunc`

Vim allows you to define a `completefunc` or an `omnifunc` to give you
completions during insert mode. `webcomplete` provides you with a function that
you can plug into these built in features.

To set it up, use either of the two lines below:
```
" Use <C-X><C-U> in insert mode to get completions
set completefunc=webcomplete#complete

" Use <C-X><C-O> in insert mode to get completions
set omnifunc=webcomplete#complete
```

## Using with Google Chrome

Currently this plugin only supports Google Chrome on Mac OS.

To use it, you must enable "Allow JavaScript from Apple Events" in View >
Developer submenu.

## Using with Qutebrowser

Set one of the `_webcomplete_script` variables (described above) to
`$plugin_dir/sh/qutebrowser/webcomplete`, where `$plugin_dir` is the location
of this plugin.

## Using with Firefox

Currently there is no official support for Firefox, but there is a
[fork with Firefox support](https://github.com/kimat/webcomplete.vim)

# Limitations

* Currently works on Mac OS because of the `osascript` command line utility,
  which is used to fetch text from the page
* Assumes you have only one browser window opened. If there is more than one
  window open, it picks the most recently used.
* Currently works only on Chrome, but it's possible to use with other browsers.

# Contributing

If you would like to contribute to the project by supporting your browser or
operating system, I would be happy to accept pull requests.

# Inspiration

The project was only possible with the [help of Reddit user 18252](https://www.reddit.com/r/commandline/comments/4j73um/any_way_of_getting_the_text_of_open_chrome_pages/d34ftzx)
and by looking at [tmux-complete.vim](https://github.com/wellle/tmux-complete.vim) as reference when implementing this plugin.
