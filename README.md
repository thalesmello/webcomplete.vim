# webcomplete.vim

A Deoplete source for Neovim that completes words from the currently open web
page in your browser

![demo](./demo.gif)

# Installation

On Neovim, with [vim-plug](https://github.com/junegunn/vim-plug):

```
Plug 'Shougo/deoplete.nvim' | Plug 'thalesmello/webcomplete.vim'
```

The completions will appear during insert mode.

# Limitations

* Currently works on Mac OS because of the `osascript` command line utility,
  which is used to fetch text from the page
* Assumes you have only one browser window opened. If there is more than one
  window open, it picks just one of them.
* Currently works only on Chrome, but it's easy to include support for other
  browsers by modifying the script.

# Contributing

If you would like to contribute to the project by supporting your browser or
operating system, I would be happy to accept pull requests.

# Inspiration

The project was only possible with the [help of Reddit user 18252](https://www.reddit.com/r/commandline/comments/4j73um/any_way_of_getting_the_text_of_open_chrome_pages/d34ftzx)
and by looking at [tmux-complete.vim](https://github.com/wellle/tmux-complete.vim) as reference when implementing this plugin.
