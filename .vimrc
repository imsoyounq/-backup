set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'VundleVim/Vundle.vim'
Plugin 'scrooloose/nerdtree'
Plugin 'scrooloose/syntastic'
Plugin 'scrooloose/nerdcommenter'

Plugin 'tpope/vim-fugitive'

Plugin 'altercation/vim-colors-solarized'
Plugin 'majutsushi/tagbar'
Plugin 'godlygeek/tabular'

" EasyMotion - Allows <leader><leader>(b|e) to jump to (b)eginning or (end) of words.
Plugin 'easymotion/vim-easymotion'
" Ctrl-P - Fuzzy file search
Plugin 'kien/ctrlp.vim'
" Remove extraneous whitespace when edit mode is exited
"Plugin 'thirtythreeforty/lessspace.vim'
" LaTeX editing
Plugin 'LaTeX-Box-Team/LaTeX-Box'
" Status bar mods

"Plugin 'bling/vim-airline'
Plugin 'airblade/vim-gitgutter'
" Tab completion
Plugin 'ervandew/supertab'
Plugin 'davidhalter/jedi-vim'
call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line

set shiftwidth=4
set tabstop=4
set ruler
set visualbell
set scrolloff=5
highlight linernr ctermbg=darkblue

set expandtab
set smarttab
set softtabstop=4
set showcmd
set cursorline
set wildmenu " visual autocomplete for command menu
set lazyredraw          " redraw only when we need to.
set showmatch

set laststatus=2
set cindent
set smartindent
set autoindent
set hi=1000
set title

"set mouse=a

set hls
set scs

"colorscheme evening
colorscheme elflord
"colorscheme murphy

syntax on
filetype plugin indent on

set hlsearch
set nobackup
set tags=tags;/
set ignorecase
set smartcase

set ai
set rnu 
set nu

map<F2> gT
map<F3> gt
map<F4> :w <CR> :! gcc -g -lm -Wall % && ./a.out<CR>
map<F5> :w <CR> :! g++ % -O2 -lm -std=c++11 && time ./a.out && rm -rf ./a.out*<CR>
map<F6> :w <CR> :! python %<CR>
map<F10> :e ++enc=euc-kr<CR> :set fileencoding=utf-8<CR> :set f=unix<CR>
set pastetoggle=<F9>
